# Peças de Processo Civil e Família — Lex Unum (conteúdo autoral).
from base import *

G = "Processo Civil"
F = "Família e Sucessões"

PECAS = [
P("acao-indenizatoria", "Ação de Indenização por Danos Materiais e Morais", G,
  "Quando alguém sofre dano patrimonial e/ou extrapatrimonial causado por ato ilícito (responsabilidade subjetiva) ou por atividade de risco / relação de consumo (responsabilidade objetiva).",
  "Prescrição de 3 anos (CC, art. 206, § 3º, V) ou 5 anos nas relações de consumo por fato do produto/serviço (CDC, art. 27)",
  "CC, arts. 186, 187, 927 e 944; CDC, arts. 12 e 14; CPC, art. 319",
  ["Narrativa do fato, do dano e do nexo causal", "Indicação da modalidade de responsabilidade (subjetiva ou objetiva)", "Pedidos de dano material (danos emergentes e lucros cessantes) e de dano moral, com valores", "Valor da causa = soma dos pedidos (CPC, art. 292, V e VI)"],
  ["No dano moral, o valor deve ser indicado na inicial (CPC, art. 292, V)", "Em relação de consumo, peça a inversão do ônus da prova (CDC, art. 6º, VIII)", "Juros de mora desde o evento danoso na extracontratual (Súmula 54 do STJ)"],
  f"""{JUIZO_CIVEL}

{PF("AUTOR(A)")}, {ADV}, vem, respeitosamente, à presença de Vossa Excelência, propor a presente

AÇÃO DE INDENIZAÇÃO POR DANOS MATERIAIS E MORAIS

em face de {PJ("RÉ")}, pelos fatos e fundamentos a seguir expostos.

I – DOS FATOS
[Narrar cronologicamente o evento danoso, a conduta do réu e as consequências suportadas pelo autor.]

II – DO DIREITO
II.1 – Da responsabilidade civil do réu
[Demonstrar conduta, dano e nexo causal (CC, arts. 186 e 927). Se for objetiva, fundamentar no art. 927, parágrafo único, do CC ou nos arts. 12/14 do CDC.]
II.2 – Dos danos materiais
[Danos emergentes e lucros cessantes (CC, art. 402), com documentos.]
II.3 – Dos danos morais
[Violação a direito da personalidade e critérios de arbitramento.]
II.4 – Da inversão do ônus da prova (se relação de consumo)
[CDC, art. 6º, VIII.]

III – DOS PEDIDOS
Diante do exposto, requer:
a) a citação do réu para, querendo, contestar, sob pena de revelia;
b) a [designação / dispensa] da audiência de conciliação (CPC, art. 319, VII);
c) a inversão do ônus da prova, se cabível;
d) a procedência dos pedidos, condenando o réu ao pagamento de R$ [valor] a título de danos materiais e de R$ [valor] a título de danos morais, acrescidos de correção monetária e juros de mora;
e) a condenação do réu em custas processuais e honorários advocatícios (CPC, art. 85);
f) a produção de todas as provas em direito admitidas.

Dá-se à causa o valor de R$ [soma dos pedidos].

{FECHO}""", ["CC:186","CC:927","CC:944","CDC:6","CPC:292","CPC:319"]),

P("obrigacao-fazer", "Ação de Obrigação de Fazer ou Não Fazer", G,
  "Para compelir o réu a cumprir prestação de fazer ou de abster-se, com tutela específica e meios coercitivos (multa, busca e apreensão etc.).",
  "Conforme a pretensão de direito material",
  "CPC, arts. 497, 499, 536 e 537; CC, arts. 247 a 251",
  ["Indicação precisa da obrigação a ser cumprida", "Pedido de tutela de urgência, se houver risco (CPC, art. 300)", "Pedido de multa diária (astreintes) para o caso de descumprimento", "Pedido subsidiário de conversão em perdas e danos"],
  ["A tutela específica tem preferência sobre as perdas e danos (CPC, art. 499)", "A multa pode ser fixada de ofício e alterada pelo juiz (art. 537, § 1º)", "Para a tutela inibitória, não é preciso provar dano nem culpa (art. 497, parágrafo único)"],
  f"""{JUIZO_CIVEL}

{PF("AUTOR(A)")}, {ADV}, vem propor a presente

AÇÃO DE OBRIGAÇÃO DE [FAZER / NÃO FAZER] COM PEDIDO DE TUTELA DE URGÊNCIA

em face de {PF("RÉU/RÉ")}, pelas razões a seguir.

I – DOS FATOS
[Origem da obrigação e descumprimento pelo réu.]

II – DO DIREITO
[Obrigação de fazer/não fazer (CC, arts. 247 e 251) e tutela específica (CPC, arts. 497 e 536).]

III – DA TUTELA DE URGÊNCIA
[Probabilidade do direito e perigo de dano (CPC, art. 300).]

IV – DOS PEDIDOS
a) concessão de tutela de urgência para determinar que o réu [conduta], no prazo de [__] dias, sob pena de multa diária de R$ [valor];
b) citação do réu;
c) procedência do pedido, confirmando a tutela e condenando o réu a [conduta];
d) subsidiariamente, conversão em perdas e danos (CPC, art. 499);
e) custas e honorários;
f) produção de provas.

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CPC:497","CPC:499","CPC:536","CPC:537","CC:247"]),

P("replica", "Réplica (Manifestação sobre a Contestação)", G,
  "Quando o réu, na contestação, alega fato impeditivo, modificativo ou extintivo do direito do autor, ou qualquer das matérias do art. 337 do CPC.",
  "15 dias úteis (CPC, arts. 350 e 351)",
  "CPC, arts. 350 e 351",
  ["Identificação do processo", "Impugnação das preliminares", "Impugnação dos fatos novos alegados pelo réu", "Reiteração dos pedidos iniciais e especificação de provas"],
  ["A réplica não é peça para inovar pedidos ou causa de pedir", "Rebata cada preliminar na ordem em que aparece na contestação", "Juntada de documentos novos deve observar o art. 435 do CPC"],
  f"""{JUIZO_CIVEL}

{PROC}

[NOME DO(A) AUTOR(A)], já qualificado(a) nos autos da ação que move em face de [NOME DO RÉU], {ADV}, vem apresentar

RÉPLICA

à contestação de fls. [__], nos termos dos arts. 350 e 351 do CPC, pelos fundamentos a seguir.

I – SÍNTESE DA CONTESTAÇÃO
[Resumo das teses do réu.]

II – DAS PRELIMINARES ARGUIDAS
[Rebater cada preliminar.]

III – DO MÉRITO
[Impugnar os fatos impeditivos, modificativos ou extintivos alegados.]

IV – DOS PEDIDOS
a) a rejeição das preliminares;
b) a procedência integral dos pedidos formulados na inicial;
c) a produção das provas [especificar].

{FECHO}""", ["CPC:350","CPC:351","CPC:435"]),

P("reconvencao", "Reconvenção", G,
  "Quando o réu quer formular pedido próprio contra o autor, conexo com a ação principal ou com o fundamento da defesa.",
  "Na própria contestação, em 15 dias úteis (CPC, art. 343)",
  "CPC, art. 343",
  ["Apresentada na mesma peça da contestação, em tópico próprio", "Conexão com a ação principal ou com a defesa", "Pedido e valor da causa próprios", "Requisitos do art. 319 do CPC"],
  ["A desistência da ação principal não impede o prosseguimento da reconvenção (art. 343, § 2º)", "Pode ser proposta contra o autor e terceiro (§ 3º)", "O autor é intimado para responder em 15 dias (§ 1º)"],
  f"""{JUIZO_CIVEL}

{PROC}

[NOME DO(A) RÉU/RÉ], já qualificado(a), {ADV}, nos autos da ação que lhe move [NOME DO AUTOR], vem apresentar

CONTESTAÇÃO COM RECONVENÇÃO

pelos fundamentos a seguir.

PARTE I – DA CONTESTAÇÃO
I – Preliminares (CPC, art. 337)
II – Mérito
[Defesa com impugnação especificada.]

PARTE II – DA RECONVENÇÃO (CPC, art. 343)
I – Dos fatos
II – Da conexão com a ação principal / com a defesa
III – Do direito
IV – Dos pedidos reconvencionais
a) a intimação do autor-reconvindo, na pessoa de seu advogado, para responder em 15 dias (art. 343, § 1º);
b) a procedência da reconvenção para [pedido];
c) custas e honorários.

Dá-se à reconvenção o valor de R$ [valor].

PEDIDOS FINAIS
Requer a improcedência da ação principal e a procedência da reconvenção, com a produção de todas as provas admitidas.

{FECHO}""", ["CPC:343","CPC:337"]),

P("embargos-declaracao-civel", "Embargos de Declaração (Cível)", G,
  "Contra qualquer decisão judicial que contenha obscuridade, contradição, omissão ou erro material.",
  "5 dias úteis (CPC, art. 1.023)",
  "CPC, arts. 1.022 a 1.026",
  ["Dirigidos ao próprio juiz ou relator que proferiu a decisão", "Indicação precisa do vício", "Não há preparo", "Pedido de efeito modificativo, se for o caso"],
  ["Interrompem o prazo para outros recursos (art. 1.026)", "Servem para prequestionar (art. 1.025 — prequestionamento ficto)", "Embargos protelatórios: multa de até 2% (art. 1.026, § 2º)"],
  f"""{JUIZO_CIVEL}

{PROC}

[NOME DA PARTE], já qualificada nos autos, {ADV}, vem opor

EMBARGOS DE DECLARAÇÃO

em face da [sentença / decisão] de fls. [__], com fundamento no art. 1.022, [inciso], do CPC, pelas razões a seguir.

I – DA TEMPESTIVIDADE
[Prazo de 5 dias úteis — art. 1.023.]

II – DO VÍCIO
[Apontar a omissão/contradição/obscuridade/erro material, transcrevendo o trecho.]

III – DOS EFEITOS INFRINGENTES (se for o caso)
[Requerer a intimação da parte contrária (art. 1.023, § 2º).]

IV – DO PEDIDO
Requer o conhecimento e o provimento dos embargos para sanar o vício apontado [e, por consequência, modificar a decisão para ...].

{FECHO}""", ["CPC:1022","CPC:1023","CPC:1025","CPC:1026"]),

P("recurso-extraordinario", "Recurso Extraordinário", G,
  "Contra decisão de única ou última instância que contrariar a Constituição, declarar a inconstitucionalidade de tratado ou lei federal, julgar válida lei ou ato local contestado em face da CF ou julgar válida lei local contestada em face de lei federal.",
  "15 dias úteis (CPC, art. 1.003, § 5º)",
  "CF, art. 102, III; CPC, arts. 1.029 a 1.035",
  ["Peça de interposição ao Presidente/Vice do tribunal recorrido e razões ao STF", "Cabimento (alínea do art. 102, III)", "Prequestionamento da matéria constitucional", "Preliminar formal e fundamentada de repercussão geral (CPC, art. 1.035, § 2º)", "Preparo"],
  ["Sem preliminar de repercussão geral, o RE não é conhecido", "Não cabe para reexame de provas (Súmula 279 do STF)", "Pode ser interposto simultaneamente com o recurso especial (art. 1.031)"],
  f"""EXCELENTÍSSIMO(A) SENHOR(A) DESEMBARGADOR(A) PRESIDENTE DO TRIBUNAL DE JUSTIÇA DO ESTADO DE [UF]

{PROC}

[NOME DO RECORRENTE], já qualificado nos autos, {ADV}, inconformado com o v. acórdão de fls. [__], vem interpor

RECURSO EXTRAORDINÁRIO

com fundamento no art. 102, III, [alínea], da Constituição Federal, requerendo seu recebimento e remessa ao Supremo Tribunal Federal, juntando o comprovante de preparo.

{FECHO}

---

RAZÕES DE RECURSO EXTRAORDINÁRIO
Recorrente: [nome] — Recorrido: [nome]

Colendo Supremo Tribunal Federal,

I – DA TEMPESTIVIDADE E DO PREPARO
II – DO CABIMENTO (art. 102, III, [alínea], CF)
III – DO PREQUESTIONAMENTO
IV – DA REPERCUSSÃO GERAL (CPC, art. 1.035)
[Questão relevante do ponto de vista econômico, político, social ou jurídico que ultrapassa o interesse das partes.]
V – DOS FATOS E DO ACÓRDÃO RECORRIDO
VI – DAS RAZÕES DO RECURSO
[Demonstrar a violação ao dispositivo constitucional.]
VII – DO PEDIDO
Requer o conhecimento e o provimento do recurso para reformar o acórdão recorrido, [pedido específico].

{FECHO}""", ["CF:102","CPC:1029","CPC:1035"]),

P("agravo-interno", "Agravo Interno", G,
  "Contra decisão proferida pelo relator (decisão monocrática) em tribunal.",
  "15 dias úteis (CPC, art. 1.021)",
  "CPC, art. 1.021",
  ["Dirigido ao relator, para julgamento pelo órgão colegiado", "Impugnação específica dos fundamentos da decisão agravada (art. 1.021, § 1º)", "Pedido de retratação ou de inclusão em pauta"],
  ["É vedado ao relator apenas reproduzir a decisão agravada para negar provimento (§ 3º)", "Agravo manifestamente inadmissível ou improcedente em votação unânime gera multa de 1% a 5% (§ 4º)"],
  f"""EXCELENTÍSSIMO(A) SENHOR(A) DESEMBARGADOR(A) RELATOR(A) DO [RECURSO Nº ___] — [ÓRGÃO JULGADOR] DO TRIBUNAL DE [__]

{PROC}

[NOME DO AGRAVANTE], já qualificado, {ADV}, vem interpor

AGRAVO INTERNO

contra a decisão monocrática de fls. [__], com fundamento no art. 1.021 do CPC, requerendo a retratação ou, não sendo o caso, o julgamento pelo órgão colegiado.

I – DA TEMPESTIVIDADE
II – DA DECISÃO AGRAVADA
III – DAS RAZÕES DE REFORMA
[Impugnar especificamente cada fundamento da decisão (art. 1.021, § 1º).]
IV – DO PEDIDO
Requer a reconsideração da decisão ou o provimento do agravo pelo colegiado, para [pedido].

{FECHO}""", ["CPC:1021"]),

P("agravo-resp-re", "Agravo em Recurso Especial / Extraordinário", G,
  "Contra a decisão do presidente ou vice-presidente do tribunal de origem que inadmitir recurso especial ou extraordinário (salvo quando fundada em precedente qualificado, caso em que cabe agravo interno).",
  "15 dias úteis (CPC, art. 1.042)",
  "CPC, art. 1.042",
  ["Dirigido ao presidente/vice do tribunal de origem", "Impugnação de todos os fundamentos da decisão de inadmissão", "Sem preparo (art. 1.042, § 2º)"],
  ["Se a inadmissão se baseia em tema repetitivo/repercussão geral, cabe agravo interno (art. 1.030, § 2º), não o art. 1.042", "Não impugnar todos os fundamentos leva ao não conhecimento (Súmula 182 do STJ)"],
  f"""EXCELENTÍSSIMO(A) SENHOR(A) DESEMBARGADOR(A) [PRESIDENTE / VICE-PRESIDENTE] DO TRIBUNAL DE [__]

{PROC}

[NOME DO AGRAVANTE], {ADV}, vem interpor

AGRAVO EM RECURSO [ESPECIAL / EXTRAORDINÁRIO]

contra a decisão que inadmitiu o recurso, com fundamento no art. 1.042 do CPC, requerendo, caso não haja retratação, a remessa ao [STJ / STF].

I – DA DECISÃO AGRAVADA
II – DO DESACERTO DA INADMISSÃO
[Rebater, um a um, todos os fundamentos.]
III – DO PEDIDO
Requer o provimento do agravo para admitir o recurso [especial / extraordinário] e, desde logo, julgá-lo (art. 1.042, § 5º).

{FECHO}""", ["CPC:1030","CPC:1042"]),

P("contrarrazoes-apelacao", "Contrarrazões de Apelação", G,
  "Resposta do apelado ao recurso de apelação interposto pela parte contrária.",
  "15 dias úteis (CPC, art. 1.010, § 1º)",
  "CPC, arts. 1.009, § 1º, e 1.010",
  ["Peça de juntada ao juízo de primeiro grau e razões ao tribunal", "Preliminares de inadmissibilidade do recurso", "Defesa da sentença", "Impugnação de interlocutórias não agraváveis, se houver (art. 1.009, § 1º)"],
  ["Nas contrarrazões, o apelado pode suscitar questões decididas em interlocutórias não agraváveis", "Aponte a falta de preparo, intempestividade ou ausência de dialeticidade, se houver"],
  f"""{JUIZO_CIVEL}

{PROC}

[NOME DO APELADO], já qualificado, {ADV}, vem apresentar

CONTRARRAZÕES DE APELAÇÃO

ao recurso interposto por [NOME DO APELANTE], requerendo a remessa ao Tribunal de Justiça.

{FECHO}

---

CONTRARRAZÕES DE APELAÇÃO
Apelante: [nome] — Apelado: [nome]

Egrégio Tribunal, Colenda Câmara,

I – DA SÍNTESE DO RECURSO
II – PRELIMINARMENTE: DO NÃO CONHECIMENTO DO RECURSO [se houver]
III – DO MÉRITO: DO ACERTO DA SENTENÇA
IV – [DAS QUESTÕES DECIDIDAS EM INTERLOCUTÓRIAS NÃO AGRAVÁVEIS — art. 1.009, § 1º]
V – DO PEDIDO
Requer o não conhecimento ou o desprovimento da apelação, mantendo-se a sentença, com majoração dos honorários (CPC, art. 85, § 11).

{FECHO}""", ["CPC:1009","CPC:1010","CPC:85"]),

P("recurso-ordinario-constitucional", "Recurso Ordinário Constitucional (Cível)", G,
  "Contra acórdão denegatório de mandado de segurança decidido em única instância pelos tribunais (ao STJ) ou pelos tribunais superiores (ao STF), e nas causas entre Estado estrangeiro e Município ou pessoa residente no Brasil.",
  "15 dias úteis (CPC, art. 1.003, § 5º)",
  "CF, arts. 102, II, e 105, II; CPC, arts. 1.027 e 1.028",
  ["Interposição perante o tribunal de origem", "Razões dirigidas ao STJ ou ao STF", "Preparo", "Devolve toda a matéria, como uma apelação"],
  ["Cabe apenas contra decisão DENEGATÓRIA do MS em única instância", "Não exige prequestionamento nem repercussão geral", "Aplica-se a teoria da causa madura (art. 1.027, § 2º)"],
  f"""EXCELENTÍSSIMO(A) SENHOR(A) DESEMBARGADOR(A) PRESIDENTE DO TRIBUNAL DE JUSTIÇA DO ESTADO DE [UF]

Mandado de Segurança nº [número]

[NOME DO RECORRENTE], {ADV}, vem interpor

RECURSO ORDINÁRIO CONSTITUCIONAL

contra o acórdão que denegou a segurança, com fundamento no art. 105, II, b, da CF e no art. 1.027, II, a, do CPC, requerendo a intimação do recorrido e a remessa ao Superior Tribunal de Justiça.

{FECHO}

---

RAZÕES DE RECURSO ORDINÁRIO
I – DA TEMPESTIVIDADE E DO CABIMENTO
II – DOS FATOS E DO ACÓRDÃO RECORRIDO
III – DO DIREITO LÍQUIDO E CERTO VIOLADO
IV – DO PEDIDO
Requer o provimento do recurso para conceder a segurança, [pedido].

{FECHO}""", ["CF:105","CPC:1027"]),

P("acao-rescisoria", "Ação Rescisória", G,
  "Para desconstituir decisão de mérito transitada em julgado nas hipóteses taxativas do art. 966 do CPC (prevaricação, incompetência absoluta, dolo, ofensa à coisa julgada, violação manifesta de norma jurídica, prova falsa, prova nova, erro de fato).",
  "2 anos do trânsito em julgado da última decisão do processo (CPC, art. 975)",
  "CPC, arts. 966 a 975",
  ["Competência originária do tribunal", "Cumulação do pedido de rescisão (iudicium rescindens) com o de novo julgamento (iudicium rescissorium), quando for o caso", "Depósito de 5% do valor da causa (art. 968, II)", "Indicação da hipótese do art. 966"],
  ["Não cabe rescisória nos Juizados Especiais (Lei 9.099/1995, art. 59)", "Prova nova: prazo conta da descoberta, limitado a 5 anos do trânsito (art. 975, § 2º)", "A propositura não impede o cumprimento da decisão, salvo tutela provisória (art. 969)"],
  f"""EXCELENTÍSSIMO(A) SENHOR(A) DESEMBARGADOR(A) PRESIDENTE DO TRIBUNAL DE JUSTIÇA DO ESTADO DE [UF]

{PF("AUTOR(A)")}, {ADV}, vem propor

AÇÃO RESCISÓRIA

em face de {PF("RÉU/RÉ")}, visando à rescisão da [sentença/acórdão] proferido nos autos nº [número], transitado em julgado em [data], com fundamento no art. 966, [inciso], do CPC.

I – DA TEMPESTIVIDADE (art. 975)
II – DA DECISÃO RESCINDENDA
III – DO CABIMENTO: [HIPÓTESE DO ART. 966]
IV – DO NOVO JULGAMENTO DA CAUSA
V – DA TUTELA PROVISÓRIA (art. 969), se for o caso
VI – DOS PEDIDOS
a) a citação do réu para responder no prazo fixado pelo relator (art. 970);
b) a procedência do pedido para rescindir a decisão e, em novo julgamento, [pedido];
c) a restituição do depósito do art. 968, II;
d) custas e honorários.

Junta comprovante do depósito de 5% do valor da causa.
Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CPC:966","CPC:968","CPC:969","CPC:975"]),

P("acao-monitoria", "Ação Monitória", G,
  "Para quem tem prova escrita sem eficácia de título executivo (cheque prescrito, contrato sem testemunhas, e-mails) que comprove direito a pagamento de quantia, entrega de coisa ou obrigação de fazer ou não fazer.",
  "Prescrição da pretensão de direito material (ex.: 5 anos para cheque prescrito — Súmula 503 do STJ)",
  "CPC, arts. 700 a 702",
  ["Prova escrita sem eficácia de título executivo", "Memória de cálculo da quantia devida (art. 700, § 2º)", "Pedido de expedição de mandado de pagamento/entrega/cumprimento em 15 dias"],
  ["Pagando no prazo, o réu fica isento de custas e paga honorários de 5% (art. 701, § 1º)", "A defesa é por embargos monitórios, em 15 dias, sem garantia do juízo (art. 702)", "Cabe contra a Fazenda Pública (Súmula 339 do STJ)"],
  f"""{JUIZO_CIVEL}

{PF("AUTOR(A)")}, {ADV}, vem propor

AÇÃO MONITÓRIA

em face de {PF("RÉU/RÉ")}, com fundamento nos arts. 700 e seguintes do CPC, pelos motivos a seguir.

I – DOS FATOS
[Origem da dívida e prova escrita (ex.: cheque nº __, prescrito).]

II – DO DIREITO
[Cabimento da monitória (art. 700) — prova escrita sem eficácia executiva.]

III – DO VALOR DEVIDO
[Memória de cálculo atualizada (art. 700, § 2º).]

IV – DOS PEDIDOS
a) a expedição de mandado de pagamento para que o réu pague R$ [valor], no prazo de 15 dias, acrescido de honorários de 5% (art. 701);
b) não havendo pagamento nem embargos, a constituição de pleno direito do título executivo judicial (art. 701, § 2º);
c) custas e honorários.

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CPC:700","CPC:701","CPC:702"]),

P("execucao-titulo-extrajudicial", "Execução de Título Extrajudicial", G,
  "Quando o credor tem título executivo extrajudicial (CPC, art. 784) líquido, certo e exigível — cheque, nota promissória, duplicata, contrato assinado por duas testemunhas etc.",
  "Prescrição do título (ex.: 6 meses para cheque após o prazo de apresentação)",
  "CPC, arts. 778, 783, 784, 798 e 829",
  ["Título executivo original (ou cópia, no processo eletrônico)", "Demonstrativo atualizado do débito (art. 798, I, b)", "Indicação de bens à penhora, se possível", "Pedido de citação para pagar em 3 dias"],
  ["Se pagar em 3 dias, os honorários caem pela metade (art. 827, § 1º)", "Peça a averbação premonitória da execução (art. 828)", "O executado se defende por embargos, sem garantia do juízo (art. 914)"],
  f"""{JUIZO_CIVEL}

{PF("EXEQUENTE")}, {ADV}, vem propor

AÇÃO DE EXECUÇÃO DE TÍTULO EXTRAJUDICIAL

em face de {PF("EXECUTADO(A)")}, com fundamento nos arts. 784, [inciso], e 829 do CPC.

I – DO TÍTULO EXECUTIVO
[Descrever o título e demonstrar liquidez, certeza e exigibilidade (art. 783).]

II – DO DÉBITO
[Demonstrativo atualizado (art. 798, I, b).]

III – DOS PEDIDOS
a) a citação do executado para pagar R$ [valor] em 3 dias (art. 829), com honorários de 10% (art. 827);
b) não havendo pagamento, a penhora e avaliação de bens, indicando desde já [bens];
c) a expedição de certidão para averbação premonitória (art. 828);
d) custas e honorários.

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CPC:783","CPC:784","CPC:798","CPC:827","CPC:828","CPC:829"]),

P("cumprimento-sentenca", "Requerimento de Cumprimento de Sentença", G,
  "Para executar sentença condenatória ao pagamento de quantia certa, na mesma relação processual.",
  "Prescrição da pretensão executiva (mesmo prazo da pretensão original — Súmula 150 do STF)",
  "CPC, arts. 513, 523 e 524",
  ["Petição nos próprios autos", "Demonstrativo discriminado e atualizado do crédito (art. 524)", "Pedido de intimação do devedor para pagar em 15 dias"],
  ["Sem pagamento voluntário, incidem multa de 10% e honorários de 10% (art. 523, § 1º)", "O devedor pode impugnar em 15 dias após o prazo de pagamento (art. 525)", "Cabe protesto da decisão e inclusão em cadastros (arts. 517 e 782, § 3º)"],
  f"""{JUIZO_CIVEL}

{PROC}

[NOME DO CREDOR], já qualificado nos autos, {ADV}, vem requerer o

CUMPRIMENTO DE SENTENÇA

em face de [NOME DO DEVEDOR], com fundamento nos arts. 523 e seguintes do CPC.

I – DO TÍTULO
[Sentença/acórdão transitado em julgado em [data].]

II – DO DEMONSTRATIVO DO CRÉDITO (art. 524)
[Valor principal, índice de correção, juros, termo inicial e final.]

III – DOS PEDIDOS
a) a intimação do executado para pagar R$ [valor] em 15 dias, sob pena de multa de 10% e honorários de 10% (art. 523, § 1º);
b) decorrido o prazo, a penhora de bens, inclusive por meio do SISBAJUD;
c) o protesto da decisão judicial (art. 517).

{FECHO}""", ["CPC:513","CPC:517","CPC:523","CPC:524","CPC:525"]),

P("embargos-execucao", "Embargos à Execução", G,
  "Defesa do executado na execução de título extrajudicial.",
  "15 dias úteis da juntada do mandado de citação (CPC, art. 915)",
  "CPC, arts. 914 a 920",
  ["Distribuídos por dependência à execução, em autos apartados", "Matérias do art. 917 (inexequibilidade, excesso de execução, penhora incorreta etc.)", "No excesso de execução, indicar o valor correto com demonstrativo (art. 917, § 3º)", "Pedido de efeito suspensivo, se houver garantia e requisitos (art. 919, § 1º)"],
  ["Não exigem garantia do juízo (art. 914)", "Efeito suspensivo exige garantia + requisitos da tutela provisória", "Embargos manifestamente protelatórios geram multa (art. 918, parágrafo único)"],
  f"""{JUIZO_CIVEL}

Distribuição por dependência aos autos nº [número]

{PF("EMBARGANTE")}, {ADV}, vem opor

EMBARGOS À EXECUÇÃO

em face de [NOME DO EMBARGADO], com fundamento nos arts. 914 e 917 do CPC.

I – DA TEMPESTIVIDADE (art. 915)
II – DOS FATOS
III – DO DIREITO
[Matéria do art. 917: inexequibilidade do título / excesso de execução / etc.]
IV – DO EXCESSO DE EXECUÇÃO (se for o caso)
[Valor que entende correto: R$ [valor], com demonstrativo — art. 917, § 3º.]
V – DO EFEITO SUSPENSIVO (art. 919, § 1º)
VI – DOS PEDIDOS
a) a concessão de efeito suspensivo;
b) a intimação do embargado para impugnar em 15 dias (art. 920);
c) a procedência dos embargos para [extinguir a execução / reduzir o valor];
d) custas e honorários.

Dá-se à causa o valor de R$ [valor controvertido].

{FECHO}""", ["CPC:914","CPC:915","CPC:917","CPC:919","CPC:920"]),

P("impugnacao-cumprimento", "Impugnação ao Cumprimento de Sentença", G,
  "Defesa do executado no cumprimento de sentença que reconhece obrigação de pagar quantia.",
  "15 dias úteis após o fim do prazo para pagamento voluntário (CPC, art. 525)",
  "CPC, art. 525",
  ["Petição nos próprios autos", "Matérias do art. 525, § 1º", "No excesso, declarar o valor correto com demonstrativo (§ 4º)", "Pedido de efeito suspensivo, com garantia (§ 6º)"],
  ["Independe de penhora (art. 525, caput)", "Matérias anteriores à sentença estão cobertas pela coisa julgada", "Inexigibilidade por decisão do STF em controle de constitucionalidade (§ 12)"],
  f"""{JUIZO_CIVEL}

{PROC}

[NOME DO EXECUTADO], já qualificado, {ADV}, vem apresentar

IMPUGNAÇÃO AO CUMPRIMENTO DE SENTENÇA

com fundamento no art. 525, § 1º, [inciso], do CPC.

I – DA TEMPESTIVIDADE
II – DAS MATÉRIAS IMPUGNADAS
[Excesso de execução / inexigibilidade / falta de citação / causa extintiva superveniente etc.]
III – DO VALOR CORRETO (art. 525, § 4º)
IV – DO EFEITO SUSPENSIVO (art. 525, § 6º)
V – DOS PEDIDOS
Requer o acolhimento da impugnação para [extinguir / reduzir] a execução, com condenação do exequente em honorários.

{FECHO}""", ["CPC:525"]),

P("embargos-terceiro", "Embargos de Terceiro", G,
  "Para quem, não sendo parte no processo, sofre constrição ou ameaça de constrição sobre bens que possua ou sobre os quais tenha direito incompatível com o ato (ex.: penhora de imóvel já vendido ao terceiro).",
  "No conhecimento, até o trânsito em julgado; na execução, até 5 dias após a adjudicação, alienação ou arrematação, antes da assinatura da carta (CPC, art. 675)",
  "CPC, arts. 674 a 681",
  ["Distribuição por dependência ao juízo que ordenou a constrição", "Prova sumária da posse ou do domínio e da qualidade de terceiro", "Rol de testemunhas (art. 677)", "Pedido liminar de suspensão da constrição"],
  ["O promitente comprador com contrato não registrado pode opor embargos (Súmula 84 do STJ)", "O cônjuge pode defender sua meação (art. 674, § 2º, I)", "Honorários são pagos por quem deu causa à constrição (Súmula 303 do STJ)"],
  f"""{JUIZO_CIVEL}

Distribuição por dependência aos autos nº [número]

{PF("EMBARGANTE")}, {ADV}, vem opor

EMBARGOS DE TERCEIRO COM PEDIDO LIMINAR

em face de [NOME DO EMBARGADO — exequente/autor do processo principal], pelos fatos a seguir.

I – DOS FATOS
[Constrição sobre bem do embargante, que não é parte no processo.]
II – DA QUALIDADE DE TERCEIRO E DA POSSE/PROPRIEDADE
[Prova documental — ex.: contrato de compra e venda anterior.]
III – DA LIMINAR (art. 678)
IV – DOS PEDIDOS
a) a suspensão liminar das medidas constritivas sobre o bem [descrição];
b) a citação do embargado para contestar em 15 dias (art. 679);
c) a procedência dos embargos para desconstituir a constrição;
d) custas e honorários.

Rol de testemunhas: [__].
Dá-se à causa o valor de R$ [valor do bem].

{FECHO}""", ["CPC:674","CPC:675","CPC:677","CPC:678","CPC:679"]),

P("tutela-antecipada-antecedente", "Tutela Antecipada Requerida em Caráter Antecedente", G,
  "Quando a urgência é contemporânea à propositura da ação: a parte pede apenas a tutela antecipada, com indicação do pedido final.",
  "Aditamento da inicial em 15 dias após a concessão (CPC, art. 303, § 1º, I)",
  "CPC, arts. 300, 303 e 304",
  ["Indicação de que se vale do benefício do art. 303 (§ 5º)", "Exposição sumária da lide e do direito", "Perigo de dano ou risco ao resultado útil", "Indicação do pedido de tutela final e do valor da causa"],
  ["Se o réu não recorrer, a tutela se estabiliza (art. 304)", "Não aditando a inicial, o processo é extinto (art. 303, § 2º)", "O valor da causa considera o pedido final (§ 4º)"],
  f"""{JUIZO_CIVEL}

{PF("REQUERENTE")}, {ADV}, vem, com fundamento no art. 303 do CPC, requerer

TUTELA ANTECIPADA EM CARÁTER ANTECEDENTE

em face de {PJ("REQUERIDA")}, declarando que se vale do benefício do art. 303, § 5º, do CPC.

I – EXPOSIÇÃO SUMÁRIA DA LIDE
II – DO DIREITO QUE SE BUSCA REALIZAR
III – DA PROBABILIDADE DO DIREITO E DO PERIGO DE DANO (art. 300)
IV – DO PEDIDO DE TUTELA FINAL
[Indicar o pedido principal que será objeto do aditamento.]
V – DOS PEDIDOS
a) a concessão da tutela antecipada para [medida];
b) a intimação do requerente para aditar a inicial em 15 dias (art. 303, § 1º, I);
c) a citação e intimação do requerido.

Dá-se à causa o valor de R$ [valor do pedido final].

{FECHO}""", ["CPC:300","CPC:303","CPC:304"]),

P("tutela-cautelar-antecedente", "Tutela Cautelar Requerida em Caráter Antecedente", G,
  "Para assegurar o resultado útil de um processo (arresto, sequestro, arrolamento, protesto contra alienação etc.) antes da propositura do pedido principal.",
  "Pedido principal em 30 dias da efetivação da medida (CPC, art. 308)",
  "CPC, arts. 301 e 305 a 310",
  ["Indicação da lide e seu fundamento", "Exposição sumária do direito que se visa assegurar", "Perigo de dano ou risco ao resultado útil"],
  ["Se o juiz entender que o pedido é de tutela antecipada, aplica o art. 303 (fungibilidade — art. 305, parágrafo único)", "A eficácia cessa se o pedido principal não for deduzido no prazo (art. 309)", "O réu tem 5 dias para contestar (art. 306)"],
  f"""{JUIZO_CIVEL}

{PF("REQUERENTE")}, {ADV}, vem requerer

TUTELA CAUTELAR EM CARÁTER ANTECEDENTE

em face de {PF("REQUERIDO(A)")}, com fundamento nos arts. 301 e 305 do CPC.

I – DA LIDE E SEU FUNDAMENTO (art. 305)
II – DO DIREITO A SER ASSEGURADO
III – DO PERIGO DE DANO / RISCO AO RESULTADO ÚTIL
IV – DOS PEDIDOS
a) a concessão liminar da medida de [arresto / sequestro / etc.] sobre [bens];
b) a citação do requerido para contestar em 5 dias (art. 306);
c) a ciência de que o pedido principal será formulado em 30 dias (art. 308).

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CPC:301","CPC:305","CPC:306","CPC:308","CPC:309"]),

P("reclamacao-cpc", "Reclamação (CPC)", G,
  "Para preservar a competência do tribunal, garantir a autoridade de suas decisões e a observância de súmula vinculante, de decisão do STF em controle concentrado e de acórdão em IRDR ou IAC.",
  "Antes do trânsito em julgado da decisão reclamada (CPC, art. 988, § 5º, I)",
  "CPC, arts. 988 a 993; CF, arts. 102, I, l, e 103-A, § 3º",
  ["Dirigida ao presidente do tribunal cuja autoridade se busca garantir", "Prova documental da decisão reclamada e do paradigma", "Pedido de suspensão do ato reclamado"],
  ["Para garantir a observância de RE com repercussão geral ou de recurso repetitivo, é preciso esgotar as instâncias ordinárias (art. 988, § 5º, II)", "Não cabe após o trânsito em julgado da decisão reclamada"],
  f"""EXCELENTÍSSIMO(A) SENHOR(A) MINISTRO(A) PRESIDENTE DO [SUPREMO TRIBUNAL FEDERAL / SUPERIOR TRIBUNAL DE JUSTIÇA]

{PF("RECLAMANTE")}, {ADV}, vem apresentar

RECLAMAÇÃO COM PEDIDO LIMINAR

contra ato do [Juízo/Tribunal reclamado], proferido nos autos nº [número], com fundamento no art. 988, [inciso], do CPC.

I – DO CABIMENTO
II – DO ATO RECLAMADO E DO PARADIGMA DESRESPEITADO
III – DA LIMINAR (art. 989, II)
IV – DOS PEDIDOS
a) a suspensão liminar do ato reclamado;
b) a requisição de informações à autoridade reclamada;
c) a citação do beneficiário do ato (art. 989, III);
d) a procedência da reclamação para cassar a decisão (art. 992).

{FECHO}""", ["CPC:988","CPC:989","CPC:992","CF:103-A"]),

P("arguicao-impedimento-suspeicao", "Arguição de Impedimento ou Suspeição", G,
  "Quando o juiz está em alguma das hipóteses de impedimento (art. 144) ou suspeição (art. 145) do CPC.",
  "15 dias do conhecimento do fato (CPC, art. 146)",
  "CPC, arts. 144 a 148",
  ["Petição específica dirigida ao juiz da causa", "Indicação do fundamento e prova documental/rol de testemunhas", "Pedido de remessa ao tribunal se o juiz não reconhecer"],
  ["Impedimento é objetivo (presunção absoluta); suspeição é subjetiva", "Impedimento autoriza ação rescisória (art. 966, II); suspeição não", "Também se aplica ao MP, auxiliares da justiça e peritos (art. 148)"],
  f"""{JUIZO_CIVEL}

{PROC}

[NOME DA PARTE], já qualificada, {ADV}, vem, com fundamento no art. 146 do CPC, arguir o

[IMPEDIMENTO / A SUSPEIÇÃO]

do(a) MM. Juiz(a) [nome], pelos fatos a seguir.

I – DA TEMPESTIVIDADE (15 dias do conhecimento do fato)
II – DOS FATOS
III – DO FUNDAMENTO (art. [144/145], inciso [__], do CPC)
IV – DOS PEDIDOS
a) que Vossa Excelência reconheça [o impedimento / a suspeição] e remeta os autos ao substituto legal;
b) caso contrário, a autuação em apartado e a remessa ao tribunal (art. 146, § 1º).

{FECHO}""", ["CPC:144","CPC:145","CPC:146"]),

P("acao-consignacao", "Ação de Consignação em Pagamento", G,
  "Quando o credor se recusa a receber, não pode receber, é desconhecido ou há dúvida sobre quem deva receber (CC, art. 335), para que o devedor se libere da obrigação.",
  "Enquanto a dívida for exigível",
  "CPC, arts. 539 a 549; CC, arts. 334 a 345",
  ["Indicação da hipótese do art. 335 do CC", "Pedido de depósito da quantia ou da coisa em 5 dias (art. 542, I)", "Pedido de declaração de extinção da obrigação"],
  ["Para dinheiro, é possível o depósito extrajudicial em banco oficial (art. 539, § 1º)", "Na defesa, o réu só pode alegar as matérias do art. 544", "Nas prestações sucessivas, pode-se consignar as que vencerem no curso do processo (art. 541)"],
  f"""{JUIZO_CIVEL}

{PF("AUTOR(A)")}, {ADV}, vem propor

AÇÃO DE CONSIGNAÇÃO EM PAGAMENTO

em face de {PF("RÉU/RÉ")}, com fundamento nos arts. 539 e seguintes do CPC e 335, [inciso], do CC.

I – DOS FATOS
[Obrigação, tentativa de pagamento e recusa/impossibilidade.]
II – DO DIREITO
III – DOS PEDIDOS
a) a autorização para depósito de R$ [valor] em 5 dias (art. 542, I);
b) a citação do réu para levantar o depósito ou contestar (art. 542, II);
c) a procedência do pedido, declarando extinta a obrigação;
d) custas e honorários.

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CPC:539","CPC:542","CPC:544","CC:335"]),

P("reintegracao-posse", "Ação de Reintegração de Posse", G,
  "Quando o possuidor é privado da posse por esbulho. Se houver apenas turbação, cabe manutenção; se houver ameaça, interdito proibitório (fungibilidade — CPC, art. 554).",
  "Ação de força nova (liminar) se proposta em até ano e dia do esbulho (CPC, art. 558)",
  "CPC, arts. 554 a 566; CC, arts. 1.196 e 1.210",
  ["Prova da posse anterior", "Prova do esbulho e de sua data", "Prova da perda da posse (art. 561)", "Pedido liminar sem ouvir o réu (art. 562)"],
  ["As ações possessórias têm natureza dúplice: o réu pode pedir proteção possessória na contestação (art. 556)", "Não se discute domínio na possessória (art. 557)", "Litígio coletivo exige audiência de mediação antes da liminar quando o esbulho tiver mais de ano e dia (art. 565)"],
  f"""{JUIZO_CIVEL}

{PF("AUTOR(A)")}, {ADV}, vem propor

AÇÃO DE REINTEGRAÇÃO DE POSSE COM PEDIDO LIMINAR

em face de {PF("RÉU/RÉ")}, com fundamento nos arts. 560 e seguintes do CPC e 1.210 do CC.

I – DOS FATOS
[Posse exercida pelo autor, esbulho praticado em [data] e perda da posse.]
II – DO DIREITO
[Requisitos do art. 561 do CPC.]
III – DA LIMINAR (art. 562)
[Ação de força nova — esbulho há menos de ano e dia.]
IV – DOS PEDIDOS
a) a expedição liminar de mandado de reintegração de posse;
b) a citação do réu;
c) a procedência do pedido, confirmando a liminar, com cominação de multa para nova turbação ou esbulho (art. 555, parágrafo único, I);
d) a condenação em perdas e danos (art. 555, I);
e) custas e honorários.

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CPC:554","CPC:555","CPC:556","CPC:558","CPC:561","CPC:562","CC:1210"]),

P("acao-usucapiao", "Ação de Usucapião", G,
  "Para obter a declaração de domínio de quem exerceu posse com ânimo de dono pelo prazo legal, conforme a modalidade de usucapião.",
  "Imprescritível enquanto durar a posse; os prazos aquisitivos variam de 2 a 15 anos",
  "CC, arts. 1.238 a 1.244; CF, arts. 183 e 191; CPC, arts. 246, § 3º, e 259, I",
  ["Indicação da modalidade e preenchimento dos requisitos", "Planta e memorial descritivo do imóvel", "Certidões do registro de imóveis", "Citação dos confinantes e de interessados por edital", "Intimação das Fazendas Públicas"],
  ["A usucapião também pode ser extrajudicial, em cartório (Lei 6.015/1973, art. 216-A)", "Bens públicos não são usucapíveis", "Pode ser alegada como matéria de defesa (Súmula 237 do STF)"],
  f"""{JUIZO_CIVEL}

{PF("AUTOR(A)")}, {ADV}, vem propor

AÇÃO DE USUCAPIÃO [EXTRAORDINÁRIA / ORDINÁRIA / ESPECIAL URBANA]

em relação ao imóvel situado na [endereço], matrícula nº [__] do [__] Registro de Imóveis, em face de [proprietário registral / réus incertos], com fundamento no art. [1.238 / 1.240] do CC.

I – DOS FATOS
[Início da posse, sua natureza mansa, pacífica e ininterrupta, com animus domini, e benfeitorias.]
II – DOS REQUISITOS DA USUCAPIÃO
III – DOS PEDIDOS
a) a citação do proprietário registral e dos confinantes (art. 246, § 3º);
b) a citação por edital de réus incertos e eventuais interessados (art. 259, I);
c) a intimação da União, do Estado e do Município;
d) a intimação do Ministério Público, se houver interesse;
e) a procedência do pedido para declarar o domínio do autor e determinar o registro da sentença.

Dá-se à causa o valor de R$ [valor venal do imóvel].

{FECHO}""", ["CC:1238","CC:1240","CC:1242","CPC:246","CPC:259","CF:183"]),

P("acao-despejo", "Ação de Despejo", G,
  "Para retomar imóvel urbano locado nas hipóteses da Lei do Inquilinato (falta de pagamento, denúncia vazia, infração contratual, uso próprio etc.).",
  "Enquanto durar a locação",
  "Lei 8.245/1991, arts. 5º, 9º, 59 a 66",
  ["Prova da locação (contrato)", "Indicação do fundamento do despejo", "Na falta de pagamento: cálculo discriminado do débito (art. 62, I)", "Pedido de liminar quando cabível (art. 59, § 1º)"],
  ["Na falta de pagamento, o locatário pode purgar a mora em 15 dias (art. 62, II)", "Liminar para desocupação em 15 dias exige caução de 3 aluguéis (art. 59, § 1º)", "O rito é o comum (art. 59)"],
  f"""{JUIZO_CIVEL}

{PF("LOCADOR(A)")}, {ADV}, vem propor

AÇÃO DE DESPEJO POR [FALTA DE PAGAMENTO / DENÚNCIA VAZIA / ...] [CUMULADA COM COBRANÇA DE ALUGUÉIS]

em face de {PF("LOCATÁRIO(A)")}, com fundamento nos arts. 5º, 9º, [inciso], e 59 da Lei 8.245/1991.

I – DA LOCAÇÃO
II – DO FUNDAMENTO DO DESPEJO
III – DO DÉBITO (art. 62, I) — se por falta de pagamento
IV – DA LIMINAR (art. 59, § 1º, [inciso])
V – DOS PEDIDOS
a) a concessão de liminar para desocupação em 15 dias, mediante caução;
b) a citação do réu para contestar ou purgar a mora em 15 dias (art. 62, II);
c) a procedência do pedido para decretar o despejo [e condenar ao pagamento dos aluguéis e encargos];
d) custas e honorários.

Dá-se à causa o valor de R$ [12 aluguéis — art. 58, III].

{FECHO}""", ["L8245:5","L8245:9","L8245:58","L8245:59","L8245:62"]),

P("acao-alimentos", "Ação de Alimentos", F,
  "Para que o alimentando (filho, ex-cônjuge, parente) obtenha prestação alimentar de quem tem o dever legal, com base no binômio necessidade–possibilidade.",
  "O direito a alimentos é imprescritível; prestações vencidas prescrevem em 2 anos (CC, art. 206, § 2º)",
  "Lei 5.478/1968; CC, arts. 1.694 a 1.710; CPC, art. 693, parágrafo único",
  ["Prova do parentesco ou da obrigação alimentar", "Demonstração das necessidades do alimentando e das possibilidades do alimentante", "Pedido de alimentos provisórios (Lei 5.478/1968, art. 4º)", "Intervenção do MP se houver incapaz"],
  ["Alimentos provisórios são fixados desde o despacho inicial", "Prisão civil só pelas três últimas prestações anteriores ao ajuizamento e as vincendas (Súmula 309 do STJ)", "Alimentos gravídicos têm lei própria (Lei 11.804/2008)"],
  f"""{JUIZO_FAMILIA}

[NOME DO ALIMENTANDO], menor impúbere, neste ato representado(a) por sua genitora {PF("REPRESENTANTE")}, {ADV}, vem propor

AÇÃO DE ALIMENTOS

em face de {PF("ALIMENTANTE")}, com fundamento na Lei 5.478/1968 e nos arts. 1.694 e seguintes do CC.

I – DOS FATOS
[Vínculo de parentesco e ausência de contribuição do réu.]
II – DAS NECESSIDADES DO ALIMENTANDO
III – DAS POSSIBILIDADES DO ALIMENTANTE
IV – DOS ALIMENTOS PROVISÓRIOS (Lei 5.478/1968, art. 4º)
V – DOS PEDIDOS
a) a fixação de alimentos provisórios em [__% dos rendimentos / R$ valor];
b) a citação do réu e a designação de audiência;
c) a intimação do Ministério Público;
d) a procedência do pedido para fixar alimentos definitivos em [valor], com desconto em folha;
e) a gratuidade da justiça;
f) custas e honorários.

Dá-se à causa o valor de R$ [12 prestações — CPC, art. 292, III].

{FECHO}""", ["CC:1694","CC:1695","CC:1696","CPC:292","CPC:693","L5478:4"]),

P("acao-divorcio", "Ação de Divórcio (Litigioso)", F,
  "Para dissolver o casamento quando não há consenso entre os cônjuges. Havendo consenso e sem filhos incapazes, o divórcio pode ser feito em cartório.",
  "Não há prazo (EC 66/2010)",
  "CF, art. 226, § 6º; CPC, arts. 693 a 699 e 731; CC, arts. 1.571 e seguintes",
  ["Certidão de casamento", "Pedidos de partilha, guarda, convivência e alimentos, quando cabíveis", "Indicação do regime de bens e dos bens a partilhar", "Retorno ao nome de solteiro(a), se desejado"],
  ["O divórcio é direito potestativo: não depende de culpa nem de prazo", "Pode-se pedir a decretação liminar do divórcio, deixando a partilha para depois", "Ações de família priorizam a mediação (CPC, art. 694)"],
  f"""{JUIZO_FAMILIA}

{PF("REQUERENTE")}, {ADV}, vem propor

AÇÃO DE DIVÓRCIO LITIGIOSO [CUMULADA COM PARTILHA, GUARDA E ALIMENTOS]

em face de {PF("REQUERIDO(A)")}, com fundamento no art. 226, § 6º, da CF e nos arts. 693 e seguintes do CPC.

I – DO CASAMENTO E DO REGIME DE BENS
II – DO DIVÓRCIO (direito potestativo — EC 66/2010)
III – DOS FILHOS: GUARDA E CONVIVÊNCIA (CC, arts. 1.583 e 1.584)
IV – DOS ALIMENTOS
V – DA PARTILHA DOS BENS
VI – DO NOME
VII – DOS PEDIDOS
a) a decretação do divórcio, inclusive em tutela de evidência;
b) a fixação da guarda [compartilhada] e do regime de convivência;
c) a fixação de alimentos em favor dos filhos;
d) a partilha dos bens conforme o regime;
e) a citação do requerido e a designação de audiência de mediação (art. 695);
f) a intimação do MP (art. 698).

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CF:226","CPC:693","CPC:694","CPC:695","CPC:698","CC:1583","CC:1584"]),

P("investigacao-paternidade", "Ação de Investigação de Paternidade", F,
  "Para que o filho obtenha o reconhecimento judicial da paternidade não declarada voluntariamente.",
  "Imprescritível (ECA, art. 27)",
  "CC, arts. 1.596, 1.606 e 1.607; ECA, art. 27; Lei 8.560/1992",
  ["Legitimidade do filho (representado, se incapaz)", "Indícios da relação entre a mãe e o suposto pai", "Pedido de exame de DNA", "Cumulação com alimentos e retificação do registro"],
  ["A recusa ao exame de DNA gera presunção relativa de paternidade (Súmula 301 do STJ; Lei 8.560/1992, art. 2º-A)", "Os alimentos fixados retroagem à citação (Súmula 277 do STJ)", "Pode ser proposta contra os herdeiros se o suposto pai faleceu"],
  f"""{JUIZO_FAMILIA}

[NOME DO AUTOR], menor, representado(a) por {PF("REPRESENTANTE LEGAL")}, {ADV}, vem propor

AÇÃO DE INVESTIGAÇÃO DE PATERNIDADE CUMULADA COM ALIMENTOS

em face de {PF("INVESTIGADO")}, pelos fatos a seguir.

I – DOS FATOS
II – DO DIREITO AO RECONHECIMENTO DO ESTADO DE FILIAÇÃO (ECA, art. 27)
III – DA PROVA PERICIAL (DNA) E DA PRESUNÇÃO EM CASO DE RECUSA (Súmula 301 do STJ)
IV – DOS ALIMENTOS
V – DOS PEDIDOS
a) a fixação de alimentos provisórios;
b) a citação do réu e a realização de exame de DNA;
c) a intimação do Ministério Público;
d) a procedência para declarar a paternidade, determinar a averbação no registro civil e fixar alimentos definitivos;
e) a gratuidade da justiça.

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CC:1596","CC:1606","ECA:27","L8560:2-A"]),

P("inventario", "Abertura de Inventário Judicial", F,
  "Para apurar, liquidar e partilhar os bens deixados pelo falecido quando houver testamento, herdeiro incapaz ou falta de consenso (do contrário, pode ser extrajudicial).",
  "Instauração em 2 meses da abertura da sucessão, com conclusão em 12 meses (CPC, art. 611)",
  "CPC, arts. 610 a 673; CC, arts. 1.784 e 1.991",
  ["Certidão de óbito", "Indicação de quem deve ser nomeado inventariante (art. 617)", "Relação dos herdeiros e dos bens conhecidos", "Foro do último domicílio do falecido (art. 48)"],
  ["Inventário extrajudicial exige herdeiros capazes e concordes, por escritura pública (art. 610, § 1º)", "O arrolamento sumário serve quando todos os herdeiros são capazes e concordam com a partilha (art. 659)", "O inventariante presta as primeiras declarações em 20 dias (art. 620)"],
  f"""{JUIZO_FAMILIA}

{PF("REQUERENTE")}, na qualidade de [cônjuge/herdeiro(a)] de [NOME DO FALECIDO], falecido em [data], {ADV}, vem requerer a

ABERTURA DE INVENTÁRIO

dos bens deixados pelo de cujus, com fundamento nos arts. 610 e seguintes do CPC.

I – DO FALECIMENTO E DA LEGITIMIDADE (art. 616)
II – DOS HERDEIROS
III – DOS BENS CONHECIDOS
IV – DOS PEDIDOS
a) a nomeação do(a) requerente como inventariante (art. 617, [inciso]);
b) a intimação para prestar compromisso e as primeiras declarações em 20 dias (art. 620);
c) a citação dos herdeiros e a intimação da Fazenda Pública (art. 626).

Dá-se à causa o valor de R$ [valor estimado dos bens].

{FECHO}""", ["CPC:48","CPC:610","CPC:611","CPC:616","CPC:617","CPC:620","CPC:659","CC:1784"]),
]
