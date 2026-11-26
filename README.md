# Lex Unum — Plataforma de Estudos Jurídicos

Da faculdade à aprovação na OAB, sem trocar de plataforma.

Lex Unum reúne em um só lugar:

- **Vade Mecum** — 277 leis e códigos em texto integral (23 mil artigos), com busca por artigo ou palavra-chave e notas de estudo nos artigos mais cobrados.
- **Doutrinas por matéria** — resumos das principais disciplinas do Direito e da prova da OAB.
- **Jurisprudência** — 33 mil precedentes do STF e do STJ (súmulas, temas, teses, informativos e acórdãos uniformizadores), com busca e link para a fonte oficial.
- **Peças processuais** — modelos comentados (petição inicial, contestação, apelação, HC, MS, remédios constitucionais etc.) e assistente de IA.
- **Banco de questões** — questões autorais de 1ª fase (com comentário em cada alternativa) e de 2ª fase (discursivas com gabarito), além de importação por PDF ou JSON.
- **Simulado OAB** — simulados cronometrados por nível (fácil, médio, difícil) com sugestão adaptativa.
- **Provas oficiais** — links para os canais oficiais da OAB/FGV.
- **Notícias do Direito** — manchetes recentes de Migalhas, Conjur, JOTA, STF e STJ.

## Tecnologias

- HTML, CSS e JavaScript puro (arquivo único `index.html`)
- [Neon](https://neon.com) — acervo de leis e precedentes (Data API)
- [Supabase](https://supabase.com) — autenticação, progresso do usuário, questões importadas e histórico de simulados
- Supabase Edge Function `peca-assistant` — assistente de IA para peças
- [PDF.js](https://mozilla.github.io/pdf.js/) — leitura de PDFs para importar questões

## Como rodar

Abra o `index.html` em um navegador (Chrome, Safari, Firefox ou Edge). Não é preciso build.

Para publicar, qualquer hospedagem estática serve (GitHub Pages, Vercel, Netlify).

## Acervo jurídico (Neon)

O Vade Mecum e a Jurisprudência consultam um banco Postgres no [Neon](https://neon.com) (projeto `lex-unum`, região São Paulo) pela **Data API**, com token anônimo e só leitura:

| Tabela | Conteúdo |
|---|---|
| `leis` | 277 diplomas: CF, ADCT, códigos, estatutos, leis complementares, leis e decretos |
| `dispositivos` | 23.095 artigos em texto integral (compilado do Planalto), com título/capítulo/seção |
| `precedentes` | 33.704 itens: súmulas vinculantes, súmulas STF e STJ, temas de repercussão geral (STF), temas repetitivos (STJ), Jurisprudência em Teses (STJ), Informativo STF e acórdãos uniformizadores do STJ |

Busca em texto integral em português (ignora acentos e plural) pelas funções `buscar_dispositivos` e `buscar_precedentes`. RLS ativo: o papel `anonymous` só tem `SELECT`.

Se o acervo estiver fora do ar, o app volta para a seleção curada embutida no `index.html`.

### Importar ou atualizar o acervo

Os dados vêm da base aberta [advocacia-aberta](https://github.com/emidio-trancoso/advocacia-aberta) (código MIT; textos legais e decisões são de fontes oficiais e não têm proteção autoral, Lei 9.610/98, art. 8º, IV). O script usa só Python 3 e a API HTTPS do Neon:

```bash
export NEON_DATABASE_URL='postgresql://USUARIO:SENHA@ep-....sa-east-1.aws.neon.tech/neondb?sslmode=require'
python3 scripts/importar_acervo.py            # tudo (leva poucos minutos)
python3 scripts/importar_acervo.py --so leis  # só legislação
```

A importação é idempotente (atualiza o que já existe). Para trazer uma versão mais nova da base, troque `COMMIT` no topo do script. Não commite a connection string.

## Supabase

O app espera as tabelas `questoes_importadas`, `resultados_simulado` e `respostas_usuario`, todas com a coluna `user_id`, e a Edge Function `peca-assistant` publicada no projeto. A chave usada no front-end é a chave **publicável** do Supabase; a proteção dos dados depende das políticas de RLS das tabelas.

---

Desenvolvido por [Feito em Código](https://github.com/Luiz204).
