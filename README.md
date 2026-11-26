# Lex Unum — Plataforma de Estudos Jurídicos

Da faculdade à aprovação na OAB, sem trocar de plataforma.

Lex Unum reúne em um só lugar:

- **Vade Mecum** — artigos selecionados da CF, CC, CP, CPC, CPP, CLT, CDC, ECA, CTN e Estatuto da Advocacia, com busca e link para o texto oficial no Planalto.
- **Doutrinas por matéria** — resumos das principais disciplinas do Direito e da prova da OAB.
- **Jurisprudência** — súmulas comentadas do STF, STJ e TST.
- **Peças processuais** — modelos comentados (petição inicial, contestação, apelação, HC, MS, remédios constitucionais etc.) e assistente de IA.
- **Banco de questões** — questões autorais de 1ª fase (com comentário em cada alternativa) e de 2ª fase (discursivas com gabarito), além de importação por PDF ou JSON.
- **Simulado OAB** — simulados cronometrados por nível (fácil, médio, difícil) com sugestão adaptativa.
- **Provas oficiais** — links para os canais oficiais da OAB/FGV.
- **Notícias do Direito** — manchetes recentes de Migalhas, Conjur, JOTA, STF e STJ.

## Tecnologias

- HTML, CSS e JavaScript puro (arquivo único `index.html`)
- [Supabase](https://supabase.com) — autenticação, progresso do usuário, questões importadas e histórico de simulados
- Supabase Edge Function `peca-assistant` — assistente de IA para peças
- [PDF.js](https://mozilla.github.io/pdf.js/) — leitura de PDFs para importar questões

## Como rodar

Abra o `index.html` em um navegador (Chrome, Safari, Firefox ou Edge). Não é preciso build.

Para publicar, qualquer hospedagem estática serve (GitHub Pages, Vercel, Netlify).

## Supabase

O app espera as tabelas `questoes_importadas`, `resultados_simulado` e `respostas_usuario`, todas com a coluna `user_id`, e a Edge Function `peca-assistant` publicada no projeto. A chave usada no front-end é a chave **publicável** do Supabase; a proteção dos dados depende das políticas de RLS das tabelas.

---

Desenvolvido por [Feito em Código](https://github.com/Luiz204).
