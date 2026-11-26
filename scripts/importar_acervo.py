#!/usr/bin/env python3
"""
Importa o acervo jurídico do Lex Unum para o Neon.

Fonte: base aberta "advocacia-aberta" (github.com/emidio-trancoso/advocacia-aberta),
fixada num commit específico para a importação ser reproduzível.
  - Legislação: 277 diplomas (CF, ADCT, códigos, estatutos e leis), texto do Planalto.
  - Precedentes: súmulas STF/STJ/vinculantes, temas de repercussão geral (STF),
    temas repetitivos (STJ), Jurisprudência em Teses (STJ), Informativo STF e
    espelhos de acórdãos dos órgãos uniformizadores do STJ.

Usa só a biblioteca padrão do Python 3.9+ e a API HTTP do Neon (porta 443),
então funciona em qualquer rede que acesse sites HTTPS.

Uso:
  export NEON_DATABASE_URL='postgresql://usuario:senha@ep-xxxx.sa-east-1.aws.neon.tech/neondb?sslmode=require'
  python3 scripts/importar_acervo.py              # importa tudo
  python3 scripts/importar_acervo.py --so leis    # só legislação
  python3 scripts/importar_acervo.py --dry-run --fonte /caminho/para/data   # testa sem gravar
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

COMMIT = "0173d1f9b08c8cc15c67f6de11dd6311c7d2f5df"
RAW = ("https://raw.githubusercontent.com/emidio-trancoso/advocacia-aberta/"
       f"{COMMIT}/ferramentas/pesquisa/vade-mecum/data/")
API_LISTA = ("https://api.github.com/repos/emidio-trancoso/advocacia-aberta/contents/"
             f"ferramentas/pesquisa/vade-mecum/data?ref={COMMIT}")

LOTE_BYTES = 1_500_000  # tamanho máximo aproximado de cada lote enviado ao Neon


# ----------------------------------------------------------------- fonte
class Fonte:
    def __init__(self, pasta=None):
        self.pasta = Path(pasta) if pasta else None

    def listar_leis(self):
        if self.pasta:
            return sorted(p.name for p in self.pasta.glob("lei_*.json"))
        with urllib.request.urlopen(API_LISTA, timeout=60) as r:
            itens = json.load(r)
        return sorted(i["name"] for i in itens if i["name"].startswith("lei_") and i["name"].endswith(".json"))

    def ler(self, nome):
        if self.pasta:
            return json.loads((self.pasta / nome).read_text(encoding="utf-8"))
        for tentativa in range(4):
            try:
                with urllib.request.urlopen(RAW + nome, timeout=120) as r:
                    return json.load(r)
            except (urllib.error.URLError, TimeoutError):
                if tentativa == 3:
                    raise
                time.sleep(2 * (tentativa + 1))


# ----------------------------------------------------------------- neon
class Neon:
    def __init__(self, url):
        self.url = url
        host = urllib.parse.urlparse(url).hostname
        if not host:
            sys.exit("NEON_DATABASE_URL inválida.")
        self.endpoint = f"https://{host}/sql"

    def sql(self, query, params=None):
        corpo = json.dumps({"query": query, "params": params or []}).encode("utf-8")
        req = urllib.request.Request(self.endpoint, data=corpo, method="POST", headers={
            "Content-Type": "application/json",
            "Neon-Connection-String": self.url,
        })
        for tentativa in range(4):
            try:
                with urllib.request.urlopen(req, timeout=180) as r:
                    return json.load(r)
            except urllib.error.HTTPError as e:
                msg = e.read().decode("utf-8", "replace")[:500]
                if e.code < 500 or tentativa == 3:
                    raise RuntimeError(f"Neon respondeu {e.code}: {msg}") from None
            except (urllib.error.URLError, TimeoutError):
                if tentativa == 3:
                    raise
            time.sleep(3 * (tentativa + 1))


class Destino:
    """Envia linhas em lotes com INSERT ... SELECT FROM jsonb_to_recordset."""

    def __init__(self, neon, dry_run):
        self.neon = neon
        self.dry = dry_run
        self.contagem = {}

    def enviar(self, tabela, colunas, tipos, linhas, conflito):
        cols = ", ".join(colunas)
        defs = ", ".join(f"{c} {t}" for c, t in zip(colunas, tipos))
        upd = ", ".join(f"{c} = excluded.{c}" for c in colunas if c not in conflito)
        q = (f"INSERT INTO public.{tabela} ({cols}) SELECT {cols} FROM jsonb_to_recordset($1::jsonb) AS x({defs}) "
             f"ON CONFLICT ({', '.join(conflito)}) DO UPDATE SET {upd}")
        lote, tam = [], 0
        for l in linhas:
            s = len(json.dumps(l, ensure_ascii=False).encode("utf-8"))
            if lote and tam + s > LOTE_BYTES:
                self._flush(q, tabela, lote)
                lote, tam = [], 0
            lote.append(l)
            tam += s
        if lote:
            self._flush(q, tabela, lote)

    def _flush(self, q, tabela, lote):
        if not self.dry:
            self.neon.sql(q, [json.dumps(lote, ensure_ascii=False)])
        self.contagem[tabela] = self.contagem.get(tabela, 0) + len(lote)


# ----------------------------------------------------------------- transformação
ORDINAL = re.compile(r"((?:Art\.|§)\s*[\d.]*\d(?:-[A-Z]+)?)\s?o\b")


def limpa(t):
    if t is None:
        return None
    t = ORDINAL.sub(r"\1º", str(t))
    return t.strip() or None


def categoria(codigo, nome, norma):
    n = (nome or "").lower()
    if codigo in ("CF", "ADCT"):
        return "Constituição"
    if n.startswith("código") or n.startswith("consolidação"):
        return "Códigos"
    if n.startswith("estatuto"):
        return "Estatutos"
    if (norma or "").startswith("Lei Complementar"):
        return "Leis complementares"
    if (norma or "").startswith(("Decreto", "Decreto-Lei")):
        return "Decretos e decretos-lei"
    return "Leis"


def nivel(h, *chaves):
    for k in chaves:
        num = h.get(k)
        nome = h.get(k + "_name")
        if num or nome:
            return " — ".join(x for x in (str(num) if num else None, nome) if x)
    return None


def link(links, *chaves):
    if isinstance(links, dict):
        for k in chaves:
            if links.get(k):
                return links[k]
        for v in links.values():
            if isinstance(v, str) and v.startswith("http"):
                return v
    return None


def importar_leis(fonte, destino):
    arquivos = fonte.listar_leis()
    print(f"Legislação: {len(arquivos)} diplomas")
    for i, nome in enumerate(arquivos, 1):
        d = fonte.ler(nome)
        m = d["_meta"]
        codigo = m["codigo"]
        artigos = list(d["artigos"].values())
        destino.enviar("leis",
                       ["codigo", "nome", "norma", "url", "total_artigos", "capturado_em", "categoria"],
                       ["text", "text", "text", "text", "int", "timestamptz", "text"],
                       [{"codigo": codigo, "nome": m.get("nome"), "norma": m.get("lei"), "url": m.get("url_base"),
                         "total_artigos": len(artigos), "capturado_em": m.get("gerado_em"),
                         "categoria": categoria(codigo, m.get("nome"), m.get("lei"))}],
                       ["codigo"])
        linhas = []
        for ordem, a in enumerate(artigos, 1):
            h = a.get("hierarchy") or {}
            linhas.append({
                "lei_codigo": codigo, "numero": str(a["numero"]), "ordem": ordem, "texto": limpa(a.get("texto")) or "",
                "url": a.get("url"),
                "titulo": nivel(h, "livro", "parte", "title", "titulo"),
                "capitulo": nivel(h, "chapter", "capitulo"),
                "secao": nivel(h, "section", "secao"),
            })
        destino.enviar("dispositivos",
                       ["lei_codigo", "numero", "ordem", "texto", "url", "titulo", "capitulo", "secao"],
                       ["text", "text", "int", "text", "text", "text", "text", "text"],
                       linhas, ["lei_codigo", "numero"])
        print(f"  [{i}/{len(arquivos)}] {codigo}: {len(linhas)} artigos")


PREC_COLS = ["id", "tipo", "tribunal", "numero", "titulo", "texto", "detalhes", "area", "situacao", "data_ref", "url", "extra"]
PREC_TIPOS = ["text"] * 11 + ["jsonb"]


def p(**kw):
    kw = {k: (limpa(v) if isinstance(v, str) else v) for k, v in kw.items()}
    kw["extra"] = {k: v for k, v in (kw.get("extra") or {}).items() if v not in (None, "", [], {})} or None
    return {c: kw.get(c) for c in PREC_COLS}


def importar_precedentes(fonte, destino):
    def vals(nome, chave):
        d = fonte.ler(nome)[chave]
        return list(d.values()) if isinstance(d, dict) else d

    def env(rotulo, linhas):
        destino.enviar("precedentes", PREC_COLS, PREC_TIPOS, linhas, ["id"])
        print(f"  {rotulo}: {len(linhas)}")

    print("Precedentes:")
    env("Súmulas vinculantes", [p(
        id=f"SV-{s['numero']}", tipo="sumula_vinculante", tribunal="STF", numero=str(s["numero"]),
        titulo=f"Súmula Vinculante {s['numero']}", texto=s.get("enunciado"), area=s.get("ramo"),
        situacao=s.get("status"), data_ref=s.get("data"), url=s.get("url"),
        extra={"precedentes": s.get("precedentes")}) for s in vals("sumulas_vinculantes.json", "sumulas")])

    env("Súmulas STF", [p(
        id=f"STF-SUM-{s['numero']}", tipo="sumula_stf", tribunal="STF", numero=str(s["numero"]),
        titulo=f"Súmula {s['numero']} do STF", texto=s.get("enunciado"), area=s.get("area"),
        situacao=s.get("status"), data_ref=s.get("data"), url=s.get("url"),
        extra={"precedentes": s.get("precedentes")}) for s in vals("sumulas_stf.json", "sumulas")])

    env("Súmulas STJ", [p(
        id=f"STJ-SUM-{s['numero']}", tipo="sumula_stj", tribunal="STJ", numero=str(s["numero"]),
        titulo=f"Súmula {s['numero']} do STJ", texto=s.get("enunciado"), area=s.get("area"),
        situacao=s.get("status"), data_ref=s.get("data"), url=s.get("url"),
        extra={"tema": s.get("tema"), "orgao": s.get("orgao")}) for s in vals("sumulas_stj.json", "sumulas")])

    env("Temas de repercussão geral (STF)", [p(
        id=f"STF-RG-{t['numero']}", tipo="tema_rg_stf", tribunal="STF", numero=str(t["numero"]),
        titulo=t.get("titulo"), texto=t.get("tese") or None, detalhes=t.get("descricao"),
        situacao=t.get("situacao"), data_ref=t.get("dataJulgamento"), url=link(t.get("links"), "paginaTema"),
        extra={"leadingCase": t.get("leadingCase"), "relator": t.get("relator"), "repercussao": t.get("repercussao"),
               "dataTese": t.get("dataTese"), "observacao": t.get("observacao"), "links": t.get("links")})
        for t in vals("temas_rg_stf.json", "temas")])

    env("Temas repetitivos (STJ)", [p(
        id=f"STJ-TR-{t['numero']}", tipo="tema_repetitivo_stj", tribunal="STJ", numero=str(t["numero"]),
        titulo=t.get("questao"), texto=t.get("teseFirmada") or None,
        area=(t.get("assuntos") or [None])[-1], situacao=t.get("situacao"), data_ref=t.get("dataJulgamento"),
        url=link(t.get("links"), "paginaTema"),
        extra={"processo": t.get("processo"), "relator": t.get("relator"), "orgaoJulgador": t.get("orgaoJulgador"),
               "dataAfetacao": t.get("dataAfetacao"), "assuntos": t.get("assuntos"), "links": t.get("links")})
        for t in vals("flash_temas_stj.json", "temas")])

    env("Jurisprudência em Teses (STJ)", [p(
        id=f"STJ-JT-{t['id']}", tipo="tese_stj", tribunal="STJ", numero=f"{t['edicao']}.{t['tese_numero']}",
        titulo=f"Edição {t['edicao']} — {t.get('edicao_titulo')}", texto=t.get("enunciado"),
        area=t.get("ramo_direito"), data_ref=t.get("data_publicacao"), url=t.get("url"),
        extra={"qtd_julgados": t.get("qtd_julgados"), "rito_especial": t.get("rito_especial")})
        for t in vals("jt_stj.json", "teses")])

    env("Informativo STF", [p(
        id=f"STF-INF-{i['id']}", tipo="informativo_stf", tribunal="STF", numero=str(i.get("edicao")),
        titulo=i.get("titulo"), texto=i.get("teseJulgado") or i.get("resumo"),
        detalhes=i.get("resumo") if i.get("teseJulgado") else None,
        area=(i.get("ramoDireito") or "").replace(";", "; ") or None, situacao=i.get("situacao"),
        data_ref=i.get("dataJulgamento"), url=link(i.get("links"), "edicao"),
        extra={"processo": " ".join(x for x in (i.get("classeProcesso"), i.get("numeroProcesso")) if x),
               "relator": i.get("relator"), "orgaoJulgador": i.get("orgaoJulgador"), "materia": i.get("materia"),
               "repercussaoGeral": i.get("repercussaoGeral"), "temaRG": i.get("temaRG"),
               "legislacao": i.get("legislacao"), "links": i.get("links")})
        for i in vals("informativo_stf.json", "informativos")])

    env("Acórdãos uniformizadores (STJ)", [p(
        id=f"STJ-AC-{e['id']}", tipo="acordao_stj", tribunal="STJ",
        numero=" ".join(x for x in (e.get("classe"), e.get("numeroProcesso")) if x),
        titulo=" ".join(x for x in (e.get("classe"), e.get("numeroProcesso")) if x) + (f" — {e['orgao']}" if e.get("orgao") else ""),
        texto=e.get("teseJuridica") or e.get("ementa"), detalhes=e.get("ementa") if e.get("teseJuridica") else None,
        area=e.get("orgao"), data_ref=e.get("dataPublicacao"), url=link(e.get("links"), "consultaProcessual"),
        extra={"classe": e.get("descricaoClasse"), "relator": e.get("relator"), "tema": e.get("tema"),
               "numeroRegistro": e.get("numeroRegistro"), "jurisprudenciaCitada": e.get("jurisprudenciaCitada"),
               "referenciasLegislativas": e.get("referenciasLegislativas"), "links": e.get("links")})
        for e in vals("espelhos_stj.json", "espelhos")])


# ----------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--so", choices=["leis", "precedentes"], help="importa só uma parte")
    ap.add_argument("--fonte", help="pasta local com os JSON (em vez de baixar do GitHub)")
    ap.add_argument("--dry-run", action="store_true", help="transforma os dados sem gravar no banco")
    args = ap.parse_args()

    url = os.environ.get("NEON_DATABASE_URL")
    if not url and not args.dry_run:
        sys.exit("Defina NEON_DATABASE_URL com a connection string do Neon.")
    neon = Neon(url) if url else None
    if neon and not args.dry_run:
        print("Conectado:", neon.sql("select current_user as u, version() as v")["rows"][0]["u"])

    destino = Destino(neon, args.dry_run)
    fonte = Fonte(args.fonte)
    inicio = time.time()
    if args.so in (None, "leis"):
        importar_leis(fonte, destino)
    if args.so in (None, "precedentes"):
        importar_precedentes(fonte, destino)
    print(f"\nConcluído em {time.time() - inicio:.0f}s:", destino.contagem)


if __name__ == "__main__":
    main()
