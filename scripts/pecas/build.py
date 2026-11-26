# Gera os dados das peças e embute no index.html (#pecasData).
import json, os, re, sys
aqui = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, aqui)
import civil, penal, outras

# Complementos para as 11 peças originais do index.html (cabimento, prazo, fundamento, grupo)
COMPLEMENTOS = {
 "peticao-inicial": dict(grupo="Processo Civil", cabimento="Ato que inaugura o processo de conhecimento, delimitando partes, causa de pedir e pedido.", prazo="Conforme a prescrição/decadência da pretensão", fundamento="CPC, arts. 319 e 320", artigos=["CPC:319","CPC:320","CPC:321","CPC:330"]),
 "contestacao": dict(grupo="Processo Civil", cabimento="Principal defesa do réu no procedimento comum, concentrando preliminares, mérito e eventual reconvenção.", prazo="15 dias úteis (CPC, art. 335)", fundamento="CPC, arts. 335 a 342", artigos=["CPC:335","CPC:336","CPC:337","CPC:341","CPC:343"]),
 "apelacao": dict(grupo="Processo Civil", cabimento="Contra sentença (e para impugnar interlocutórias não agraváveis — CPC, art. 1.009, § 1º).", prazo="15 dias úteis (CPC, art. 1.003, § 5º)", fundamento="CPC, arts. 1.009 a 1.014", artigos=["CPC:1009","CPC:1010","CPC:1012","CPC:1013"]),
 "agravo-instrumento": dict(grupo="Processo Civil", cabimento="Contra decisões interlocutórias do rol do art. 1.015 do CPC (taxatividade mitigada — STJ, Tema 988).", prazo="15 dias úteis (CPC, art. 1.003, § 5º)", fundamento="CPC, arts. 1.015 a 1.020", artigos=["CPC:1015","CPC:1016","CPC:1017","CPC:1019"]),
 "recurso-especial": dict(grupo="Processo Civil", cabimento="Contra acórdão de TJ ou TRF que contrariar lei federal, julgar válido ato local contestado em face de lei federal ou divergir de outro tribunal na interpretação da lei federal.", prazo="15 dias úteis (CPC, art. 1.003, § 5º)", fundamento="CF, art. 105, III; CPC, arts. 1.029 a 1.041", artigos=["CF:105","CPC:1029"]),
 "habeas-corpus": dict(grupo="Processo Penal", cabimento="Sempre que alguém sofrer ou se achar ameaçado de sofrer violência ou coação em sua liberdade de locomoção, por ilegalidade ou abuso de poder.", prazo="A qualquer tempo, enquanto houver constrangimento", fundamento="CF, art. 5º, LXVIII; CPP, arts. 647 a 667", artigos=["CF:5","CPP:647","CPP:648","CPP:654"]),
 "mandado-seguranca": dict(grupo="Constitucional", cabimento="Para proteger direito líquido e certo, não amparado por HC ou HD, contra ato ilegal ou abusivo de autoridade pública ou agente no exercício de atribuições do Poder Público.", prazo="120 dias da ciência do ato (Lei 12.016/2009, art. 23)", fundamento="CF, art. 5º, LXIX; Lei 12.016/2009", artigos=["CF:5","LMS:1","LMS:6","LMS:7","LMS:23"]),
 "habeas-data": dict(grupo="Constitucional", cabimento="Para assegurar o conhecimento ou a retificação de informações relativas à pessoa do impetrante em bancos de dados governamentais ou de caráter público.", prazo="Não há prazo; exige prévia recusa administrativa", fundamento="CF, art. 5º, LXXII; Lei 9.507/1997", artigos=["CF:5","L9507:7","L9507:8"]),
 "mandado-injuncao": dict(grupo="Constitucional", cabimento="Quando a falta de norma regulamentadora tornar inviável o exercício de direitos e liberdades constitucionais e prerrogativas de nacionalidade, soberania e cidadania.", prazo="Não há prazo", fundamento="CF, art. 5º, LXXI; Lei 13.300/2016", artigos=["CF:5","L13300:2","L13300:8"]),
 "acao-popular": dict(grupo="Constitucional", cabimento="Para anular ato lesivo ao patrimônio público, à moralidade administrativa, ao meio ambiente e ao patrimônio histórico e cultural.", prazo="5 anos (Lei 4.717/1965, art. 21)", fundamento="CF, art. 5º, LXXIII; Lei 4.717/1965", artigos=["CF:5","L4717:1","L4717:21"]),
 "reclamacao-trabalhista": dict(grupo="Processo do Trabalho", cabimento="Ação do empregado (ou empregador) para cobrar direitos decorrentes da relação de trabalho.", prazo="2 anos após a extinção do contrato, limitada aos últimos 5 anos (CF, art. 7º, XXIX)", fundamento="CLT, art. 840", artigos=["CLT:840","CF:7"]),
}
novas = civil.PECAS + penal.PECAS + outras.PECAS
ids = [p["id"] for p in novas]
assert len(ids) == len(set(ids)), "ids duplicados"
dados = {"novas": novas, "complementos": COMPLEMENTOS}
idx = os.path.join(aqui, "..", "..", "index.html")
html = open(idx, encoding="utf-8").read()
bloco = json.dumps(dados, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
novo, n = re.subn(r'(<script type="application/json" id="pecasData">).*?(</script>)', lambda m: m.group(1) + bloco + m.group(2), html, count=1, flags=re.S)
assert n == 1, "marcador pecasData não encontrado"
open(idx, "w", encoding="utf-8").write(novo)
from collections import Counter
print(len(novas), "peças novas;", Counter(p["area"] for p in novas))
