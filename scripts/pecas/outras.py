# Peças de Trabalho, Tributário, Constitucional, Administrativo e Empresarial — Lex Unum (conteúdo autoral).
from base import *

T = "Processo do Trabalho"
TR = "Tributário"
C = "Constitucional"
A = "Administrativo"
E = "Empresarial"
TRT = "EXCELENTÍSSIMO(A) SENHOR(A) DESEMBARGADOR(A) PRESIDENTE DO TRIBUNAL REGIONAL DO TRABALHO DA ___ REGIÃO"
STF = "EXCELENTÍSSIMO(A) SENHOR(A) MINISTRO(A) PRESIDENTE DO SUPREMO TRIBUNAL FEDERAL"
JUIZO_FALENCIA = "AO JUÍZO DE DIREITO DA ___ VARA DE FALÊNCIAS E RECUPERAÇÕES JUDICIAIS DA COMARCA DE [CIDADE/UF]"

PECAS = [
# ------------------------------------------------------------------ TRABALHO
P("contestacao-trabalhista", "Contestação Trabalhista", T,
  "Defesa do reclamado na reclamação trabalhista.",
  "Até a audiência; no PJe, pode ser juntada até a audiência (CLT, art. 847, parágrafo único)",
  "CLT, arts. 847 e 769; CPC, arts. 336 e 337 (aplicação subsidiária)",
  ["Preliminares (incompetência, inépcia, ilegitimidade, litispendência)", "Prejudiciais de mérito: prescrição bienal e quinquenal (CF, art. 7º, XXIX)", "Impugnação específica de cada pedido", "Pedido de compensação/dedução de valores pagos"],
  ["A prescrição deve ser arguida na instância ordinária (Súmula 153 do TST)", "Compensação só pode ser arguida na contestação (Súmula 48 do TST)", "Na OAB, organize: preliminares, prejudiciais, mérito pedido a pedido e pedidos finais"],
  f"""{JUIZO_TRABALHO}

{PROC}

{PJ("RECLAMADA")}, {ADV}, nos autos da reclamação trabalhista ajuizada por [NOME DO RECLAMANTE], vem apresentar

CONTESTAÇÃO

com fundamento no art. 847 da CLT, pelas razões a seguir.

I – SÍNTESE DA INICIAL
II – PRELIMINARMENTE
[Inépcia, incompetência, ilegitimidade etc.]
III – DAS PREJUDICIAIS DE MÉRITO: PRESCRIÇÃO (CF, art. 7º, XXIX)
IV – DO MÉRITO
[Impugnar cada pedido: horas extras, verbas rescisórias, adicionais, dano moral...]
V – DA COMPENSAÇÃO / DEDUÇÃO (Súmula 48 do TST)
VI – DOS PEDIDOS
a) o acolhimento das preliminares;
b) a pronúncia da prescrição;
c) a improcedência dos pedidos;
d) a condenação do reclamante em honorários de sucumbência (CLT, art. 791-A);
e) a produção de todas as provas admitidas.

{FECHO}""", ["CLT:769","CLT:791-A","CLT:847","CF:7"]),

P("recurso-ordinario-trabalhista", "Recurso Ordinário Trabalhista", T,
  "Contra as decisões definitivas ou terminativas das Varas do Trabalho e contra decisões dos TRTs em processos de sua competência originária.",
  "8 dias (CLT, art. 895)",
  "CLT, arts. 895 e 899",
  ["Interposição ao juiz da Vara e razões ao TRT", "Preparo: custas e depósito recursal (pelo empregador)", "Impugnação dos fundamentos da sentença"],
  ["O depósito recursal é reduzido pela metade para entidades sem fins lucrativos, empregador doméstico, ME e EPP (art. 899, § 9º)", "Beneficiários da justiça gratuita, entidades filantrópicas e empresas em recuperação judicial são isentos do depósito (§ 10)", "No rito sumaríssimo, o RO tem regras próprias (art. 895, § 1º)"],
  f"""{JUIZO_TRABALHO}

{PROC}

[NOME DO RECORRENTE], {ADV}, inconformado com a sentença de fls. [__], vem interpor

RECURSO ORDINÁRIO

com fundamento no art. 895, I, da CLT, juntando os comprovantes de custas e depósito recursal, e requerendo a remessa ao Tribunal Regional do Trabalho.

{FECHO}

---

RAZÕES DE RECURSO ORDINÁRIO
Recorrente: [nome] — Recorrido: [nome]

Egrégio Tribunal Regional do Trabalho,
I – DOS PRESSUPOSTOS DE ADMISSIBILIDADE (tempestividade, preparo, representação)
II – PRELIMINARMENTE: DA NULIDADE [cerceamento de defesa, negativa de prestação jurisdicional]
III – DO MÉRITO
[Atacar cada capítulo da sentença.]
IV – DO PEDIDO
Requer o conhecimento e o provimento do recurso para reformar a sentença, [pedido].

{FECHO}""", ["CLT:895","CLT:899"]),

P("recurso-revista", "Recurso de Revista", T,
  "Contra acórdãos dos TRTs em recurso ordinário, nas hipóteses do art. 896 da CLT (divergência jurisprudencial, violação de lei federal ou da Constituição).",
  "8 dias (CLT, art. 896)",
  "CLT, arts. 896 e 896-A",
  ["Interposição ao Presidente do TRT e razões ao TST", "Demonstração da transcendência (econômica, política, social ou jurídica — art. 896-A)", "Prequestionamento com transcrição do trecho do acórdão (art. 896, § 1º-A)", "Preparo"],
  ["Não cabe para reexame de fatos e provas (Súmula 126 do TST)", "No sumaríssimo, só cabe por contrariedade a súmula do TST, súmula vinculante ou violação direta da CF (art. 896, § 9º)", "A indicação de divergência exige acórdão de TRT diverso ou da SDI"],
  f"""{TRT}

{PROC}

[NOME DO RECORRENTE], {ADV}, vem interpor

RECURSO DE REVISTA

com fundamento no art. 896, [alínea], da CLT, requerendo a remessa ao Tribunal Superior do Trabalho.

{FECHO}

---

RAZÕES DE RECURSO DE REVISTA
I – DOS PRESSUPOSTOS EXTRÍNSECOS
II – DA TRANSCENDÊNCIA (art. 896-A)
III – DO PREQUESTIONAMENTO (art. 896, § 1º-A — transcrição do trecho do acórdão)
IV – DA VIOLAÇÃO / DIVERGÊNCIA
V – DO PEDIDO
Requer o conhecimento e o provimento do recurso de revista para [pedido].

{FECHO}""", ["CLT:896","CLT:896-A"]),

P("agravo-peticao", "Agravo de Petição", T,
  "Contra as decisões do juiz na execução trabalhista (ex.: sentença de embargos à execução ou de impugnação).",
  "8 dias (CLT, art. 897, a)",
  "CLT, art. 897, a e § 1º",
  ["Delimitação justificada das matérias e dos valores impugnados (art. 897, § 1º)", "Interposição ao juiz da execução e razões ao TRT"],
  ["Sem a delimitação de matérias e valores, o agravo não é conhecido", "A parte incontroversa pode ser executada imediatamente", "Não exige depósito recursal se o juízo já estiver garantido"],
  f"""{JUIZO_TRABALHO}

{PROC}

[NOME DO AGRAVANTE], {ADV}, vem interpor

AGRAVO DE PETIÇÃO

contra a decisão de fls. [__], com fundamento no art. 897, a, da CLT.

I – DA DELIMITAÇÃO DAS MATÉRIAS E DOS VALORES (art. 897, § 1º)
[Matérias impugnadas: ___ ; valor incontroverso: R$ ___ ; valor impugnado: R$ ___.]

{FECHO}

---

RAZÕES DE AGRAVO DE PETIÇÃO
I – DA TEMPESTIVIDADE E DO CABIMENTO
II – DAS RAZÕES DE REFORMA
III – DO PEDIDO
Requer o provimento do agravo para [pedido].

{FECHO}""", ["CLT:897"]),

P("agravo-instrumento-trabalhista", "Agravo de Instrumento Trabalhista", T,
  "Exclusivamente contra despachos que denegarem a interposição de recursos (CLT, art. 897, b).",
  "8 dias (CLT, art. 897, b)",
  "CLT, arts. 897, b, e 899, § 7º",
  ["Interposição perante o juízo que denegou o recurso", "Depósito recursal de 50% do valor do depósito do recurso trancado (art. 899, § 7º)", "Impugnação dos fundamentos do despacho denegatório"],
  ["No processo do trabalho, o agravo de instrumento NÃO serve para atacar interlocutórias (que são irrecorríveis de imediato — art. 893, § 1º)", "Não exige depósito quando o recurso denegado era contra decisão contrária a súmula ou OJ do TST (art. 899, § 8º)"],
  f"""[JUÍZO QUE DENEGOU O RECURSO]

{PROC}

[NOME DO AGRAVANTE], {ADV}, vem interpor

AGRAVO DE INSTRUMENTO

contra o despacho que negou seguimento ao [recurso ordinário / recurso de revista], com fundamento no art. 897, b, da CLT, juntando o comprovante do depósito recursal (art. 899, § 7º).

{FECHO}

---

RAZÕES DE AGRAVO DE INSTRUMENTO
I – DO DESPACHO AGRAVADO
II – DO PREENCHIMENTO DOS PRESSUPOSTOS DO RECURSO TRANCADO
III – DO PEDIDO
Requer o provimento do agravo para destrancar o recurso e, desde logo, julgá-lo.

{FECHO}""", ["CLT:893","CLT:897","CLT:899"]),

P("embargos-declaracao-trabalhista", "Embargos de Declaração Trabalhistas", T,
  "Contra sentença ou acórdão com omissão, contradição ou manifesto equívoco no exame dos pressupostos extrínsecos do recurso.",
  "5 dias (CLT, art. 897-A)",
  "CLT, art. 897-A; CPC, art. 1.022 (subsidiário)",
  ["Indicação precisa do vício", "Pedido de efeito modificativo, com intimação da parte contrária"],
  ["Interrompem o prazo recursal, salvo se intempestivos, irregulares ou sem assinatura (art. 897-A, § 3º)", "Erros materiais podem ser corrigidos de ofício"],
  f"""{JUIZO_TRABALHO}

{PROC}

[NOME DO EMBARGANTE], {ADV}, vem opor

EMBARGOS DE DECLARAÇÃO

em face da sentença de fls. [__], com fundamento no art. 897-A da CLT.

I – DA TEMPESTIVIDADE (5 dias)
II – DA OMISSÃO / CONTRADIÇÃO
III – DO PEDIDO
Requer o acolhimento dos embargos para sanar o vício [com efeito modificativo].

{FECHO}""", ["CLT:897-A"]),

P("embargos-execucao-trabalhista", "Embargos à Execução Trabalhista", T,
  "Defesa do executado na execução trabalhista, após a garantia do juízo.",
  "5 dias da garantia da execução ou da penhora (CLT, art. 884)",
  "CLT, art. 884",
  ["Garantia do juízo (depósito, penhora ou seguro-garantia)", "Matérias: cumprimento da decisão, quitação, prescrição da dívida (art. 884, § 1º) e impugnação da sentença de liquidação (§ 3º)"],
  ["Entidades filantrópicas e seus diretores não precisam garantir o juízo (art. 884, § 6º)", "Da decisão dos embargos cabe agravo de petição", "A Fazenda Pública tem 30 dias para embargar"],
  f"""{JUIZO_TRABALHO}

{PROC}

[NOME DO EXECUTADO], {ADV}, garantido o juízo, vem opor

EMBARGOS À EXECUÇÃO

com fundamento no art. 884 da CLT.

I – DA TEMPESTIVIDADE E DA GARANTIA DO JUÍZO
II – DAS MATÉRIAS DE DEFESA (art. 884, § 1º)
III – DA IMPUGNAÇÃO AOS CÁLCULOS DE LIQUIDAÇÃO (art. 884, § 3º)
IV – DO PEDIDO
Requer a procedência dos embargos para [reduzir o valor / extinguir a execução].

{FECHO}""", ["CLT:884"]),

P("consignacao-trabalhista", "Ação de Consignação em Pagamento Trabalhista", T,
  "Quando o empregador quer pagar as verbas rescisórias e o empregado se recusa a receber, está desaparecido ou faleceu sem dependentes habilitados.",
  "Antes de vencido o prazo de pagamento das verbas (CLT, art. 477, § 6º) para afastar a multa",
  "CLT, art. 769; CPC, arts. 539 a 549; CC, art. 335",
  ["Indicação da recusa ou impossibilidade de pagamento", "Discriminação das verbas", "Pedido de depósito e quitação"],
  ["Afasta a multa do art. 477, § 8º, da CLT se o depósito for tempestivo", "É a peça adequada quando o empregado abandona o emprego e não recebe as verbas"],
  f"""{JUIZO_TRABALHO}

{PJ("CONSIGNANTE")}, {ADV}, vem propor

AÇÃO DE CONSIGNAÇÃO EM PAGAMENTO

em face de {PF("CONSIGNATÁRIO(A)")}, com fundamento no art. 769 da CLT e nos arts. 539 e seguintes do CPC.

I – DO CONTRATO DE TRABALHO E DE SUA EXTINÇÃO
II – DA RECUSA / IMPOSSIBILIDADE DE PAGAMENTO
III – DAS VERBAS DEVIDAS
[Saldo de salário, férias + 1/3, 13º proporcional etc.]
IV – DOS PEDIDOS
a) o depósito de R$ [valor];
b) a citação do consignatário para receber ou contestar;
c) a procedência para declarar a extinção da obrigação e afastar a multa do art. 477, § 8º, da CLT.

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CLT:477","CLT:769","CPC:539","CC:335"]),

P("inquerito-falta-grave", "Inquérito para Apuração de Falta Grave", T,
  "Para que o empregador obtenha autorização judicial para dispensar empregado estável que exige o inquérito (ex.: dirigente sindical — Súmula 379 do TST).",
  "30 dias da suspensão do empregado (CLT, art. 853; Súmula 403 do STF)",
  "CLT, arts. 494, 853 a 855",
  ["Petição escrita", "Descrição da falta grave (art. 482)", "Até 6 testemunhas (art. 821)", "Suspensão prévia do empregado, se for o caso"],
  ["O prazo de 30 dias é decadencial (Súmula 403 do STF)", "Julgado improcedente, o empregado é reintegrado com salários do período (art. 495)", "O dirigente sindical só pode ser dispensado por falta grave apurada em inquérito (Súmula 379 do TST)"],
  f"""{JUIZO_TRABALHO}

{PJ("REQUERENTE")}, {ADV}, vem ajuizar

INQUÉRITO PARA APURAÇÃO DE FALTA GRAVE

em face de {PF("REQUERIDO(A)")}, com fundamento nos arts. 494 e 853 da CLT.

I – DO CONTRATO E DA ESTABILIDADE DO EMPREGADO
II – DA FALTA GRAVE PRATICADA (art. 482, [alínea])
III – DA SUSPENSÃO E DA TEMPESTIVIDADE (art. 853)
IV – DOS PEDIDOS
a) a notificação do requerido;
b) a procedência do inquérito para reconhecer a falta grave e declarar resolvido o contrato de trabalho.

ROL DE TESTEMUNHAS (até 6)

{FECHO}""", ["CLT:482","CLT:494","CLT:495","CLT:821","CLT:853"]),

# ------------------------------------------------------------------ TRIBUTÁRIO
P("acao-anulatoria-tributaria", "Ação Anulatória de Débito Fiscal", TR,
  "Para anular o lançamento tributário já realizado (crédito constituído), com ou sem execução fiscal ajuizada.",
  "5 anos (Decreto 20.910/1932); 2 anos para anular decisão administrativa que denegar restituição (CTN, art. 169)",
  "Lei 6.830/1980, art. 38; CTN, arts. 151 e 169; CPC, art. 319",
  ["Identificação do lançamento/auto de infração", "Demonstração do vício (material ou formal)", "Pedido de tutela de urgência ou depósito para suspender a exigibilidade"],
  ["O depósito integral em dinheiro suspende a exigibilidade (CTN, art. 151, II; Súmula 112 do STJ)", "Não é necessário esgotar a via administrativa", "Se já houver execução fiscal, cabe também embargos (com garantia)"],
  f"""{JUIZO_FAZENDA}

{PJ("AUTORA")}, {ADV}, vem propor

AÇÃO ANULATÓRIA DE DÉBITO FISCAL COM PEDIDO DE TUTELA DE URGÊNCIA

em face do [ESTADO / MUNICÍPIO DE ___ / UNIÃO], pessoa jurídica de direito público, pelos fatos a seguir.

I – DOS FATOS
[Lançamento / auto de infração nº ___.]
II – DO DIREITO
[Inexistência do fato gerador, ilegalidade da base de cálculo, decadência (CTN, art. 173) etc.]
III – DA SUSPENSÃO DA EXIGIBILIDADE (CTN, art. 151, II ou V)
IV – DOS PEDIDOS
a) a tutela de urgência para suspender a exigibilidade do crédito [ou a autorização do depósito integral];
b) a citação do réu;
c) a procedência para anular o lançamento e o crédito tributário dele decorrente;
d) custas e honorários (CPC, art. 85, § 3º).

Dá-se à causa o valor de R$ [valor do débito].

{FECHO}""", ["CTN:151","CTN:169","CTN:173","LEF:38"]),

P("declaratoria-tributaria", "Ação Declaratória de Inexistência de Relação Jurídico-Tributária", TR,
  "Antes do lançamento, para obter a declaração de que o contribuinte não está obrigado a recolher determinado tributo (ex.: por imunidade ou inconstitucionalidade da lei).",
  "Enquanto não houver lançamento (depois dele, a via é a anulatória)",
  "CPC, arts. 19 e 20; CTN, art. 151",
  ["Demonstração da não incidência, imunidade ou ilegalidade", "Pedido de tutela para suspender a exigibilidade", "Pode cumular com repetição de indébito ou compensação"],
  ["É ação preventiva, típica para tributos sujeitos a lançamento por homologação", "Cumule com pedido de compensação após o trânsito (CTN, art. 170-A)"],
  f"""{JUIZO_FEDERAL}

{PJ("AUTORA")}, {ADV}, vem propor

AÇÃO DECLARATÓRIA DE INEXISTÊNCIA DE RELAÇÃO JURÍDICO-TRIBUTÁRIA COM PEDIDO DE TUTELA DE URGÊNCIA

em face da UNIÃO (FAZENDA NACIONAL), pelos fatos a seguir.

I – DOS FATOS
II – DO DIREITO
[Imunidade (CF, art. 150, VI) / inconstitucionalidade / não incidência.]
III – DA TUTELA DE URGÊNCIA (CTN, art. 151, V)
IV – DOS PEDIDOS
a) a suspensão da exigibilidade do tributo;
b) a citação da ré;
c) a procedência para declarar a inexistência de relação jurídico-tributária que obrigue a autora ao recolhimento de [tributo];
d) [a restituição/compensação dos valores pagos nos últimos 5 anos];
e) custas e honorários.

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CPC:19","CTN:151","CTN:170-A","CF:150"]),

P("repeticao-indebito", "Ação de Repetição de Indébito Tributário", TR,
  "Para obter a restituição de tributo pago indevidamente ou a maior.",
  "5 anos da extinção do crédito (CTN, art. 168; LC 118/2005)",
  "CTN, arts. 165 a 169",
  ["Prova do pagamento indevido", "Demonstração da ilegitimidade da cobrança", "Nos tributos indiretos, prova de que assumiu o encargo ou autorização de quem o suportou (CTN, art. 166)"],
  ["Juros de mora só a partir do trânsito em julgado (Súmula 188 do STJ) — na esfera federal, aplica-se a SELIC", "O contribuinte pode optar pela compensação (Súmula 461 do STJ)", "Atenção ao art. 166 do CTN nos tributos indiretos (ICMS, IPI)"],
  f"""{JUIZO_FAZENDA}

{PJ("AUTORA")}, {ADV}, vem propor

AÇÃO DE REPETIÇÃO DE INDÉBITO TRIBUTÁRIO

em face do [ESTADO / MUNICÍPIO / UNIÃO], com fundamento nos arts. 165 e seguintes do CTN.

I – DOS FATOS
[Pagamentos realizados e motivo de serem indevidos.]
II – DO DIREITO
III – DA LEGITIMIDADE (CTN, art. 166), se tributo indireto
IV – DOS PEDIDOS
a) a citação do réu;
b) a procedência para condenar o réu a restituir R$ [valor], corrigidos e acrescidos de juros;
c) alternativamente, o reconhecimento do direito à compensação;
d) custas e honorários.

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CTN:165","CTN:166","CTN:167","CTN:168","CTN:170-A"]),

P("embargos-execucao-fiscal", "Embargos à Execução Fiscal", TR,
  "Defesa do executado na execução fiscal, após a garantia do juízo.",
  "30 dias da garantia (depósito, fiança/seguro ou intimação da penhora) (LEF, art. 16)",
  "Lei 6.830/1980, art. 16",
  ["Garantia do juízo", "Toda a matéria de defesa (art. 16, § 2º)", "Rol de até 3 testemunhas", "Distribuição por dependência"],
  ["Não se admite reconvenção nem compensação nos embargos (art. 16, § 3º)", "Para matérias de ordem pública sem dilação probatória, cabe exceção de pré-executividade, sem garantia", "Efeito suspensivo depende de garantia e dos requisitos do art. 919 do CPC"],
  f"""AO JUÍZO DA VARA DE EXECUÇÕES FISCAIS DA COMARCA DE [CIDADE/UF]

Distribuição por dependência à Execução Fiscal nº [número]

{PJ("EMBARGANTE")}, {ADV}, garantido o juízo, vem opor

EMBARGOS À EXECUÇÃO FISCAL

em face do [ENTE EXEQUENTE], com fundamento no art. 16 da Lei 6.830/1980.

I – DA TEMPESTIVIDADE E DA GARANTIA DO JUÍZO
II – PRELIMINARMENTE [nulidade da CDA — CTN, art. 202; LEF, art. 2º, § 5º]
III – DO MÉRITO [prescrição (CTN, art. 174), decadência, ilegitimidade, inexistência do débito]
IV – DO EFEITO SUSPENSIVO
V – DOS PEDIDOS
a) a intimação da embargada para impugnar em 30 dias (art. 17);
b) a procedência dos embargos para extinguir a execução;
c) custas e honorários.

Rol de testemunhas (até 3).
Dá-se à causa o valor de R$ [valor da execução].

{FECHO}""", ["LEF:2","LEF:16","LEF:17","CTN:174","CTN:202"]),

P("excecao-pre-executividade", "Exceção de Pré-Executividade", TR,
  "Defesa na execução (especialmente a fiscal), sem garantia do juízo, para matérias de ordem pública que dispensam dilação probatória: prescrição, decadência, ilegitimidade, nulidade da CDA, pagamento comprovado documentalmente.",
  "A qualquer tempo, enquanto pendente a execução",
  "Construção jurisprudencial; Súmula 393 do STJ",
  ["Petição simples nos autos da execução", "Prova documental pré-constituída", "Matéria cognoscível de ofício"],
  ["Não cabe se a matéria exigir produção de provas", "Ilegitimidade do sócio cujo nome consta da CDA exige prova e, em regra, não cabe por exceção", "Acolhida, gera condenação da Fazenda em honorários"],
  f"""AO JUÍZO DA VARA DE EXECUÇÕES FISCAIS DA COMARCA DE [CIDADE/UF]

Execução Fiscal nº [número]

[NOME DO EXECUTADO], {ADV}, vem apresentar

EXCEÇÃO DE PRÉ-EXECUTIVIDADE

com fundamento na Súmula 393 do STJ, pelas razões a seguir.

I – DO CABIMENTO (matéria de ordem pública, sem dilação probatória)
II – DA [PRESCRIÇÃO / DECADÊNCIA / NULIDADE DA CDA / ILEGITIMIDADE]
III – DOS PEDIDOS
a) a suspensão dos atos executivos;
b) o acolhimento da exceção para extinguir a execução;
c) a condenação do exequente em honorários.

{FECHO}""", ["CTN:173","CTN:174","LEF:2"]),

P("mandado-seguranca-tributario", "Mandado de Segurança em Matéria Tributária", TR,
  "Contra ato ilegal de autoridade fiscal que viole direito líquido e certo do contribuinte, com prova pré-constituída. Pode ser repressivo ou preventivo.",
  "120 dias da ciência do ato (Lei 12.016/2009, art. 23); o preventivo não tem prazo",
  "CF, art. 5º, LXIX; Lei 12.016/2009",
  ["Indicação da autoridade coatora e da pessoa jurídica a que pertence (art. 6º)", "Prova pré-constituída do direito", "Pedido liminar (art. 7º, III)"],
  ["Não cabe condenação em honorários (art. 25)", "Liminar não pode determinar compensação de créditos tributários (art. 7º, § 2º)", "MS é via adequada para declarar o direito à compensação (Súmula 213 do STJ)"],
  f"""{JUIZO_FEDERAL}

{PJ("IMPETRANTE")}, {ADV}, vem impetrar

MANDADO DE SEGURANÇA [PREVENTIVO] COM PEDIDO LIMINAR

contra ato do [DELEGADO DA RECEITA FEDERAL DO BRASIL EM ___], autoridade vinculada à União (Fazenda Nacional), com fundamento no art. 5º, LXIX, da CF e na Lei 12.016/2009.

I – DA TEMPESTIVIDADE (art. 23)
II – DOS FATOS
III – DO DIREITO LÍQUIDO E CERTO
IV – DA LIMINAR (art. 7º, III)
V – DOS PEDIDOS
a) a concessão de liminar para suspender a exigibilidade do crédito (CTN, art. 151, IV);
b) a notificação da autoridade coatora para prestar informações em 10 dias;
c) a ciência do órgão de representação judicial da pessoa jurídica interessada;
d) a oitiva do Ministério Público;
e) a concessão da segurança para [pedido].

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["LMS:1","LMS:6","LMS:7","LMS:23","LMS:25","CTN:151"]),

P("consignacao-tributaria", "Ação de Consignação em Pagamento Tributária", TR,
  "Quando o contribuinte quer pagar, mas há recusa do recebimento, subordinação do pagamento a outro tributo ou exigência de dois entes sobre o mesmo fato gerador.",
  "Enquanto o crédito for exigível",
  "CTN, art. 164",
  ["Indicação da hipótese do art. 164", "Depósito do valor que o contribuinte entende devido", "Nos casos de bitributação, citação de ambos os entes"],
  ["Só pode versar sobre o crédito que o consignante se propõe a pagar (art. 164, § 1º)", "Julgada procedente, o pagamento se reputa efetuado e o valor é convertido em renda (§ 2º)"],
  f"""{JUIZO_FAZENDA}

{PJ("CONSIGNANTE")}, {ADV}, vem propor

AÇÃO DE CONSIGNAÇÃO EM PAGAMENTO

em face do [ENTE / ENTES TRIBUTANTES], com fundamento no art. 164, [inciso], do CTN.

I – DOS FATOS
II – DO DIREITO
III – DOS PEDIDOS
a) a autorização para depósito de R$ [valor];
b) a citação do(s) réu(s);
c) a procedência para declarar extinto o crédito tributário (CTN, art. 156, VIII), convertendo-se o depósito em renda do ente competente.

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CTN:156","CTN:164"]),

# ------------------------------------------------------------------ CONSTITUCIONAL
P("adi", "Ação Direta de Inconstitucionalidade (ADI)", C,
  "Para declarar a inconstitucionalidade de lei ou ato normativo federal ou estadual em face da Constituição Federal.",
  "Não há prazo",
  "CF, arts. 102, I, a, e 103; Lei 9.868/1999",
  ["Legitimidade ativa (art. 103), com pertinência temática quando exigida", "Indicação do dispositivo impugnado e dos fundamentos (Lei 9.868/1999, art. 3º)", "Cópia da lei ou ato impugnado", "Procuração com poderes específicos, quando houver advogado"],
  ["Partidos, confederações sindicais e entidades de classe precisam de advogado; os demais legitimados não", "Lei municipal não é objeto de ADI no STF (cabe ADPF)", "Não admite desistência (art. 5º) nem intervenção de terceiros, salvo amicus curiae"],
  f"""{STF}

[LEGITIMADO — art. 103 da CF], {ADV} (procuração com poderes específicos), vem propor

AÇÃO DIRETA DE INCONSTITUCIONALIDADE COM PEDIDO DE MEDIDA CAUTELAR

em face do [ato normativo — Lei nº ___], editada pelo [órgão/autoridade responsável], com fundamento no art. 102, I, a, da CF e na Lei 9.868/1999.

I – DA LEGITIMIDADE ATIVA [E DA PERTINÊNCIA TEMÁTICA]
II – DO ATO NORMATIVO IMPUGNADO
III – DA INCONSTITUCIONALIDADE [formal / material]
IV – DA MEDIDA CAUTELAR (Lei 9.868/1999, art. 10)
V – DOS PEDIDOS
a) a concessão de medida cautelar para suspender a eficácia do dispositivo;
b) a solicitação de informações ao órgão responsável (art. 6º);
c) a oitiva do Advogado-Geral da União e do Procurador-Geral da República (art. 8º);
d) a procedência do pedido para declarar a inconstitucionalidade do [dispositivo].

{FECHO}""", ["CF:102","CF:103","L9868:2","L9868:3","L9868:10"]),

P("adc", "Ação Declaratória de Constitucionalidade (ADC)", C,
  "Para afirmar a constitucionalidade de lei ou ato normativo federal objeto de controvérsia judicial relevante.",
  "Não há prazo",
  "CF, art. 102, I, a; Lei 9.868/1999, arts. 13 a 21",
  ["Legitimidade (art. 103 da CF)", "Demonstração de controvérsia judicial relevante (art. 14, III)", "Somente lei ou ato normativo federal"],
  ["Sem controvérsia judicial relevante, a ADC não é conhecida", "A medida cautelar pode suspender os processos que envolvam a aplicação da lei (art. 21)", "ADI e ADC têm natureza dúplice (art. 24)"],
  f"""{STF}

[LEGITIMADO], {ADV}, vem propor

AÇÃO DECLARATÓRIA DE CONSTITUCIONALIDADE COM PEDIDO DE MEDIDA CAUTELAR

da [Lei federal nº ___], com fundamento no art. 102, I, a, da CF e nos arts. 13 e seguintes da Lei 9.868/1999.

I – DA LEGITIMIDADE
II – DA CONTROVÉRSIA JUDICIAL RELEVANTE (art. 14, III)
III – DA CONSTITUCIONALIDADE DA NORMA
IV – DA MEDIDA CAUTELAR (art. 21)
V – DOS PEDIDOS
Requer a cautelar para suspender o julgamento dos processos que envolvam a aplicação da lei e, no mérito, a declaração de sua constitucionalidade.

{FECHO}""", ["CF:102","L9868:13","L9868:14","L9868:21","L9868:24"]),

P("adpf", "Arguição de Descumprimento de Preceito Fundamental (ADPF)", C,
  "Para evitar ou reparar lesão a preceito fundamental resultante de ato do Poder Público, inclusive lei municipal e direito pré-constitucional, quando não houver outro meio eficaz.",
  "Não há prazo",
  "CF, art. 102, § 1º; Lei 9.882/1999",
  ["Legitimados da ADI (Lei 9.882/1999, art. 2º, I)", "Indicação do preceito fundamental violado e do ato questionado (art. 3º)", "Demonstração da subsidiariedade (art. 4º, § 1º)"],
  ["Subsidiariedade: se couber ADI, ADC ou ADO, a ADPF não é conhecida", "O STF admite fungibilidade entre ADPF e ADI", "A liminar pode ser concedida por maioria absoluta (art. 5º)"],
  f"""{STF}

[LEGITIMADO], {ADV}, vem propor

ARGUIÇÃO DE DESCUMPRIMENTO DE PRECEITO FUNDAMENTAL COM PEDIDO LIMINAR

em face do [ato do Poder Público], com fundamento no art. 102, § 1º, da CF e na Lei 9.882/1999.

I – DA LEGITIMIDADE
II – DO ATO DO PODER PÚBLICO QUESTIONADO
III – DO PRECEITO FUNDAMENTAL VIOLADO
IV – DA SUBSIDIARIEDADE (art. 4º, § 1º)
V – DA LIMINAR (art. 5º)
VI – DOS PEDIDOS
Requer a liminar e, no mérito, a procedência para [declarar a incompatibilidade / não recepção do ato / fixar a interpretação conforme].

{FECHO}""", ["CF:102","L9882:1","L9882:2","L9882:3","L9882:4","L9882:5"]),

P("ado", "Ação Direta de Inconstitucionalidade por Omissão (ADO)", C,
  "Quando a falta de medida para tornar efetiva norma constitucional (omissão legislativa ou administrativa) inviabiliza sua aplicação.",
  "Não há prazo",
  "CF, art. 103, § 2º; Lei 9.868/1999, arts. 12-A a 12-H",
  ["Legitimados da ADI", "Indicação da omissão e da norma constitucional não regulamentada (art. 12-B)"],
  ["Declarada a omissão, dá-se ciência ao Poder competente; se for órgão administrativo, a providência deve ocorrer em 30 dias (CF, art. 103, § 2º)", "Diferente do mandado de injunção, a ADO é controle abstrato e não exige caso concreto"],
  f"""{STF}

[LEGITIMADO], {ADV}, vem propor

AÇÃO DIRETA DE INCONSTITUCIONALIDADE POR OMISSÃO

com fundamento no art. 103, § 2º, da CF e nos arts. 12-A e seguintes da Lei 9.868/1999.

I – DA LEGITIMIDADE
II – DA NORMA CONSTITUCIONAL CARENTE DE REGULAMENTAÇÃO
III – DA OMISSÃO INCONSTITUCIONAL (art. 12-B)
IV – DOS PEDIDOS
Requer a declaração da omissão inconstitucional, com ciência ao Poder competente para a adoção das providências necessárias [no prazo de 30 dias, se órgão administrativo].

{FECHO}""", ["CF:103","L9868:12-A","L9868:12-B","L9868:12-H"]),

P("reclamacao-constitucional", "Reclamação Constitucional (Súmula Vinculante)", C,
  "Contra ato administrativo ou decisão judicial que contrariar súmula vinculante ou a aplicar indevidamente, ou que desrespeitar decisão do STF.",
  "Antes do trânsito em julgado da decisão reclamada",
  "CF, arts. 102, I, l, e 103-A, § 3º; Lei 11.417/2006, art. 7º; CPC, art. 988",
  ["Indicação da súmula vinculante ou decisão desrespeitada", "Prova documental do ato reclamado", "Contra omissão ou ato da Administração, esgotamento da via administrativa (Lei 11.417/2006, art. 7º, § 1º)"],
  ["Contra ato administrativo, é preciso esgotar as vias administrativas antes", "Julgada procedente, o STF anula o ato ou cassa a decisão (CF, art. 103-A, § 3º)"],
  f"""{STF}

{PF("RECLAMANTE")}, {ADV}, vem apresentar

RECLAMAÇÃO CONSTITUCIONAL COM PEDIDO LIMINAR

contra [ato/decisão], por violação à Súmula Vinculante nº [__], com fundamento no art. 103-A, § 3º, da CF e no art. 7º da Lei 11.417/2006.

I – DO CABIMENTO
II – DO ATO RECLAMADO
III – DA VIOLAÇÃO À SÚMULA VINCULANTE
IV – DA LIMINAR
V – DOS PEDIDOS
Requer a suspensão liminar do ato e, ao final, a procedência para [anular o ato administrativo / cassar a decisão judicial], determinando que outra seja proferida com observância da súmula.

{FECHO}""", ["CF:102","CF:103-A","L11417:7","CPC:988"]),

P("mandado-seguranca-coletivo", "Mandado de Segurança Coletivo", C,
  "Para proteger direito líquido e certo coletivo ou individual homogêneo dos membros ou associados de partido político, organização sindical, entidade de classe ou associação.",
  "120 dias da ciência do ato (Lei 12.016/2009, art. 23)",
  "CF, art. 5º, LXX; Lei 12.016/2009, arts. 21 e 22",
  ["Legitimidade: partido com representação no Congresso; sindicato, entidade de classe ou associação em funcionamento há pelo menos 1 ano", "Pertinência com as finalidades da entidade", "Prova pré-constituída"],
  ["Dispensa autorização especial dos associados (Súmula 629 do STF)", "Basta que o direito interesse a parte da categoria (Súmula 630 do STF)", "A liminar contra o Poder Público exige audiência prévia do representante judicial em 72 horas (art. 22, § 2º)"],
  f"""{JUIZO_FAZENDA}

[NOME DA ENTIDADE IMPETRANTE], [qualificação], {ADV}, vem impetrar

MANDADO DE SEGURANÇA COLETIVO COM PEDIDO LIMINAR

contra ato do [AUTORIDADE COATORA], vinculada ao [ente], com fundamento no art. 5º, LXX, da CF e nos arts. 21 e 22 da Lei 12.016/2009.

I – DA LEGITIMIDADE ATIVA E DA PERTINÊNCIA TEMÁTICA
II – DOS FATOS
III – DO DIREITO LÍQUIDO E CERTO DOS SUBSTITUÍDOS
IV – DA LIMINAR (art. 22, § 2º)
V – DOS PEDIDOS
Requer a liminar, a notificação da autoridade, a ciência do órgão de representação judicial, a oitiva do MP e a concessão da segurança em favor de todos os [membros/associados].

{FECHO}""", ["CF:5","LMS:21","LMS:22","LMS:23"]),

# ------------------------------------------------------------------ ADMINISTRATIVO
P("acao-civil-publica", "Ação Civil Pública", A,
  "Para responsabilizar por danos ao meio ambiente, ao consumidor, à ordem urbanística, ao patrimônio público e social e a outros interesses difusos e coletivos.",
  "Em regra, 5 anos; a reparação de dano ambiental é imprescritível (STF, Tema 999)",
  "Lei 7.347/1985; CF, art. 129, III; CDC, arts. 81 e 82",
  ["Legitimidade (Lei 7.347/1985, art. 5º): MP, Defensoria, entes públicos e associações constituídas há pelo menos 1 ano", "Indicação do interesse difuso, coletivo ou individual homogêneo", "Pedido de tutela de urgência e de condenação ao fundo (art. 13)"],
  ["Não há adiantamento de custas nem condenação da associação autora em honorários, salvo má-fé (art. 18)", "Competência do foro do local do dano (art. 2º)", "O MP atua como fiscal da ordem jurídica quando não for autor (art. 5º, § 1º)"],
  f"""{JUIZO_FAZENDA}

[ASSOCIAÇÃO AUTORA], [qualificação, constituída há mais de 1 ano], {ADV}, vem propor

AÇÃO CIVIL PÚBLICA COM PEDIDO DE TUTELA DE URGÊNCIA

em face de [RÉU], com fundamento na Lei 7.347/1985.

I – DA LEGITIMIDADE ATIVA (art. 5º, V)
II – DA COMPETÊNCIA (art. 2º — local do dano)
III – DOS FATOS
IV – DO DIREITO [interesse difuso/coletivo lesado]
V – DA TUTELA DE URGÊNCIA (art. 12)
VI – DOS PEDIDOS
a) a tutela de urgência para [cessar a atividade lesiva];
b) a citação do réu e a intimação do MP;
c) a procedência para condenar o réu a [obrigação de fazer/não fazer] e ao pagamento de indenização revertida ao fundo do art. 13;
d) a dispensa de custas (art. 18).

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["LACP:1","LACP:2","LACP:5","LACP:12","LACP:13","LACP:18"]),

P("indenizacao-estado", "Ação de Indenização contra o Estado", A,
  "Para reparação de danos causados por agentes de pessoa jurídica de direito público ou de direito privado prestadora de serviço público.",
  "5 anos (Decreto 20.910/1932)",
  "CF, art. 37, § 6º; CC, art. 43",
  ["Ação proposta contra o ente (não contra o agente — Tema 940 do STF)", "Demonstração de conduta, dano e nexo causal (responsabilidade objetiva)", "Pedidos de danos materiais, morais e estéticos"],
  ["Responsabilidade objetiva pelo risco administrativo, com excludentes", "Por omissão, demonstre o dever específico de agir", "Danos morais e estéticos são cumuláveis (Súmula 387 do STJ)"],
  f"""{JUIZO_FAZENDA}

{PF("AUTOR(A)")}, {ADV}, vem propor

AÇÃO DE INDENIZAÇÃO POR DANOS MATERIAIS E MORAIS

em face do [ESTADO / MUNICÍPIO DE ___], pessoa jurídica de direito público interno, com fundamento no art. 37, § 6º, da CF.

I – DOS FATOS
II – DA RESPONSABILIDADE OBJETIVA DO ESTADO (art. 37, § 6º)
III – DOS DANOS
IV – DOS PEDIDOS
a) a citação do réu;
b) a procedência para condenar o réu ao pagamento de R$ [valor] por danos materiais, R$ [valor] por danos morais [e estéticos], com correção e juros;
c) custas e honorários (CPC, art. 85, § 3º).

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CF:37","CC:43"]),

P("anulatoria-ato-administrativo", "Ação Anulatória de Ato Administrativo", A,
  "Para anular ato administrativo ilegal (ex.: demissão de servidor sem devido processo, penalidade desproporcional, exclusão de concurso), com pedido de reintegração ou recomposição.",
  "5 anos (Decreto 20.910/1932)",
  "CF, arts. 5º, XXXV, LIV e LV, e 37; Lei 9.784/1999; Lei 8.112/1990",
  ["Identificação do ato e do vício (competência, finalidade, forma, motivo ou objeto)", "Pedido de tutela de urgência", "Pedidos consequentes (reintegração, pagamento de vencimentos)"],
  ["O Judiciário controla a legalidade, não o mérito administrativo", "A teoria dos motivos determinantes vincula o ato aos motivos declarados", "Reintegração do servidor demitido ilegalmente: CF, art. 41, § 2º, e Lei 8.112/1990, art. 28"],
  f"""{JUIZO_FAZENDA}

{PF("AUTOR(A)")}, {ADV}, vem propor

AÇÃO ANULATÓRIA DE ATO ADMINISTRATIVO COM PEDIDO DE TUTELA DE URGÊNCIA

em face do [ENTE PÚBLICO], pelos fatos a seguir.

I – DOS FATOS
II – DA ILEGALIDADE DO ATO
[Vício de competência / desvio de finalidade / motivo inexistente / ofensa ao contraditório (CF, art. 5º, LV).]
III – DA TUTELA DE URGÊNCIA
IV – DOS PEDIDOS
a) a suspensão dos efeitos do ato;
b) a citação do réu;
c) a procedência para anular o ato [e determinar a reintegração do autor, com o pagamento das vantagens do período];
d) custas e honorários.

Dá-se à causa o valor de R$ [valor].

{FECHO}""", ["CF:5","CF:37","CF:41","L9784:2","L9784:50","L8112:28"]),

P("contestacao-improbidade", "Contestação em Ação de Improbidade Administrativa", A,
  "Defesa do réu na ação de improbidade administrativa, após a Lei 14.230/2021.",
  "30 dias (Lei 8.429/1992, art. 17, § 7º)",
  "Lei 8.429/1992, arts. 1º, 9º a 11, 17 e 23",
  ["Preliminares (prescrição, ilegitimidade, inépcia)", "Ausência de dolo específico", "Atipicidade da conduta (rol taxativo do art. 11)", "Impugnação das sanções e do ressarcimento"],
  ["Desde a Lei 14.230/2021, só há improbidade dolosa (art. 1º, § 1º)", "Prescrição de 8 anos e prescrição intercorrente de 4 anos (art. 23)", "O rol do art. 11 passou a ser taxativo"],
  f"""{JUIZO_FAZENDA}

{PROC}

{PF("RÉU/RÉ")}, {ADV}, nos autos da ação de improbidade administrativa proposta pelo [MINISTÉRIO PÚBLICO / ENTE], vem apresentar

CONTESTAÇÃO

com fundamento no art. 17, § 7º, da Lei 8.429/1992.

I – SÍNTESE DA INICIAL
II – PRELIMINARMENTE: DA PRESCRIÇÃO (art. 23) / DA INÉPCIA
III – DO MÉRITO
III.1 – Da ausência de dolo (art. 1º, §§ 1º a 3º)
III.2 – Da atipicidade da conduta
III.3 – Da desproporcionalidade das sanções (art. 12)
IV – DOS PEDIDOS
Requer o acolhimento das preliminares ou a improcedência dos pedidos.

{FECHO}""", ["LIA:1","LIA:9","LIA:10","LIA:11","LIA:12","LIA:17","LIA:23"]),

P("recurso-administrativo", "Recurso Administrativo", A,
  "Contra decisão administrativa no âmbito federal (e, por analogia ou lei própria, nos demais entes), por razões de legalidade e de mérito.",
  "10 dias da ciência ou divulgação da decisão (Lei 9.784/1999, art. 59)",
  "Lei 9.784/1999, arts. 56 a 65",
  ["Dirigido à autoridade que proferiu a decisão, que pode reconsiderar em 5 dias (art. 56, § 1º)", "Exposição dos fundamentos do pedido de reexame", "Em regra, independe de caução (art. 56, § 2º)"],
  ["Tramita por no máximo três instâncias administrativas (art. 57)", "Não tem efeito suspensivo, salvo disposição legal ou risco de prejuízo (art. 61)", "Pode haver reformatio in pejus, com ciência prévia do recorrente (art. 64, parágrafo único)"],
  f"""ILUSTRÍSSIMO(A) SENHOR(A) [AUTORIDADE QUE PROFERIU A DECISÃO]

Processo Administrativo nº [número]

{PF("RECORRENTE")}, {ADV}, vem interpor

RECURSO ADMINISTRATIVO

contra a decisão de fls. [__], com fundamento nos arts. 56 e seguintes da Lei 9.784/1999, requerendo a reconsideração ou o encaminhamento à autoridade superior.

I – DA TEMPESTIVIDADE (art. 59)
II – DOS FATOS
III – DAS RAZÕES DO RECURSO
IV – DO EFEITO SUSPENSIVO (art. 61, parágrafo único)
V – DO PEDIDO
Requer o provimento do recurso para [anular / reformar] a decisão.

{FECHO}""", ["L9784:56","L9784:57","L9784:59","L9784:61","L9784:64"]),

# ------------------------------------------------------------------ EMPRESARIAL
P("pedido-recuperacao-judicial", "Pedido de Recuperação Judicial", E,
  "Para o empresário ou sociedade empresária em crise econômico-financeira que pretende superá-la com um plano aprovado pelos credores.",
  "Não há prazo; exige mais de 2 anos de atividade regular",
  "Lei 11.101/2005, arts. 47, 48 e 51",
  ["Requisitos do art. 48 (atividade há mais de 2 anos, não ser falido, não ter obtido recuperação há menos de 5 anos etc.)", "Documentos do art. 51 (demonstrações contábeis, relação de credores e de empregados, certidões etc.)", "Foro do principal estabelecimento (art. 3º)"],
  ["O plano deve ser apresentado em 60 dias do deferimento do processamento (art. 53)", "O stay period é de 180 dias (art. 6º, § 4º)", "ME e EPP podem apresentar plano especial (arts. 70 a 72)"],
  f"""{JUIZO_FALENCIA}

{PJ("REQUERENTE")}, {ADV}, vem requerer

RECUPERAÇÃO JUDICIAL

com fundamento nos arts. 47, 48 e 51 da Lei 11.101/2005.

I – DA COMPETÊNCIA (art. 3º — principal estabelecimento)
II – DAS CAUSAS DA CRISE ECONÔMICO-FINANCEIRA (art. 51, I)
III – DO PREENCHIMENTO DOS REQUISITOS (art. 48)
IV – DOS DOCUMENTOS (art. 51, II a XI)
V – DOS PEDIDOS
a) o deferimento do processamento da recuperação judicial (art. 52);
b) a nomeação de administrador judicial;
c) a suspensão das ações e execuções pelo prazo de 180 dias (art. 6º);
d) a dispensa de certidões negativas para o exercício das atividades;
e) a intimação do MP e a comunicação às Fazendas Públicas;
f) a concessão de prazo de 60 dias para o plano (art. 53).

Dá-se à causa o valor de R$ [total dos créditos sujeitos].

{FECHO}""", ["LREF:3","LREF:6","LREF:47","LREF:48","LREF:51","LREF:52","LREF:53"]),

P("pedido-falencia", "Pedido de Falência (pelo Credor)", E,
  "Quando o devedor empresário, sem relevante razão de direito, não paga obrigação líquida acima de 40 salários mínimos materializada em título protestado, sofre execução frustrada ou pratica atos de falência.",
  "Não há prazo específico (observa a exigibilidade do título)",
  "Lei 11.101/2005, arts. 94 e 97",
  ["Indicação da hipótese do art. 94 (impontualidade, execução frustrada ou atos de falência)", "Títulos executivos e instrumentos de protesto para fim falimentar (art. 94, § 3º)", "Credor empresário: prova da regularidade (art. 97, § 1º)"],
  ["Credores podem se reunir para atingir o piso de 40 salários mínimos (art. 94, § 1º)", "O devedor pode elidir a falência com depósito do valor, correção, juros e honorários (art. 98, parágrafo único)", "Não se decreta falência de quem está fora do regime (art. 2º)"],
  f"""{JUIZO_FALENCIA}

{PJ("REQUERENTE")}, {ADV}, vem requerer a

DECRETAÇÃO DE FALÊNCIA

de {PJ("REQUERIDA")}, com fundamento no art. 94, [inciso], da Lei 11.101/2005.

I – DA LEGITIMIDADE (art. 97, IV)
II – DO CRÉDITO E DA IMPONTUALIDADE INJUSTIFICADA
[Título(s) protestado(s) para fim falimentar, superior a 40 salários mínimos.]
III – DOS PEDIDOS
a) a citação da requerida para contestar em 10 dias (art. 98);
b) a decretação da falência, com as determinações do art. 99.

Dá-se à causa o valor de R$ [valor do crédito].

{FECHO}""", ["LREF:2","LREF:94","LREF:97","LREF:98","LREF:99"]),

P("contestacao-falencia", "Contestação ao Pedido de Falência", E,
  "Defesa do devedor contra o pedido de falência formulado por credor.",
  "10 dias da citação (Lei 11.101/2005, art. 98)",
  "Lei 11.101/2005, arts. 95, 96 e 98",
  ["Matérias do art. 96 (falsidade do título, prescrição, nulidade, pagamento etc.)", "Depósito elisivo, se for o caso (art. 98, parágrafo único)", "Pedido de recuperação judicial no prazo da contestação, se desejar (art. 95)"],
  ["O depósito elisivo impede a decretação da falência, ainda que a defesa seja rejeitada", "Na contestação o devedor pode pleitear recuperação judicial (art. 95)"],
  f"""{JUIZO_FALENCIA}

{PROC}

{PJ("REQUERIDA")}, {ADV}, vem apresentar

CONTESTAÇÃO AO PEDIDO DE FALÊNCIA

com fundamento nos arts. 96 e 98 da Lei 11.101/2005.

I – DA TEMPESTIVIDADE (10 dias)
II – DAS MATÉRIAS DE DEFESA (art. 96)
III – DO DEPÓSITO ELISIVO (art. 98, parágrafo único)
IV – DOS PEDIDOS
Requer a improcedência do pedido de falência [com o levantamento do depósito] e a condenação do requerente em custas e honorários [e em indenização por pedido doloso — art. 101].

{FECHO}""", ["LREF:95","LREF:96","LREF:98","LREF:101"]),

P("habilitacao-credito", "Habilitação / Divergência de Crédito", E,
  "Para que o credor inclua seu crédito na falência ou recuperação judicial, ou corrija valor ou classificação na relação publicada.",
  "15 dias da publicação do edital (Lei 11.101/2005, art. 7º, § 1º); depois, habilitação retardatária (art. 10)",
  "Lei 11.101/2005, arts. 7º, 9º e 10",
  ["Dirigida ao administrador judicial na fase administrativa", "Requisitos do art. 9º (nome, valor atualizado, origem, classificação, documentos)", "Indicação da garantia, se houver"],
  ["Habilitações retardatárias não dão direito a voto na assembleia (salvo trabalhistas) e perdem rateios já realizados (art. 10)", "A impugnação judicial da relação do administrador é feita em 10 dias (art. 8º)"],
  f"""ILUSTRÍSSIMO(A) SENHOR(A) ADMINISTRADOR(A) JUDICIAL DA [FALÊNCIA / RECUPERAÇÃO JUDICIAL] DE [EMPRESA]

Processo nº [número]

{PJ("CREDOR(A)")}, {ADV}, vem apresentar

HABILITAÇÃO DE CRÉDITO

com fundamento nos arts. 7º, § 1º, e 9º da Lei 11.101/2005.

I – DA ORIGEM DO CRÉDITO
II – DO VALOR ATUALIZADO ATÉ A DATA DA DECRETAÇÃO / DO PEDIDO
III – DA CLASSIFICAÇÃO (art. 83)
IV – DO PEDIDO
Requer a inclusão do crédito de R$ [valor], na classe [__], na relação de credores.

{FECHO}""", ["LREF:7","LREF:8","LREF:9","LREF:10","LREF:83"]),

P("dissolucao-parcial", "Ação de Dissolução Parcial de Sociedade", E,
  "Para resolver a sociedade em relação a um sócio (morte, exclusão, exercício do direito de retirada ou recesso) e apurar seus haveres.",
  "Conforme a causa; a apuração de haveres segue o contrato social ou o art. 606 do CPC",
  "CPC, arts. 599 a 609; CC, arts. 1.028 a 1.032",
  ["Petição instruída com o contrato social consolidado (art. 599, § 1º)", "Indicação da causa da dissolução", "Pedido de apuração de haveres"],
  ["A data da resolução varia conforme a causa (art. 605)", "Na omissão do contrato, os haveres são apurados pelo balanço de determinação (art. 606)", "Se todos os sócios concordarem com a dissolução, não há condenação em honorários (art. 603, § 1º)"],
  f"""{JUIZO_CIVEL}

{PF("AUTOR(A)")}, {ADV}, vem propor

AÇÃO DE DISSOLUÇÃO PARCIAL DE SOCIEDADE COM APURAÇÃO DE HAVERES

em face de {PJ("SOCIEDADE")} e de [demais sócios], com fundamento nos arts. 599 e seguintes do CPC.

I – DA SOCIEDADE E DA PARTICIPAÇÃO DO AUTOR
II – DA CAUSA DA DISSOLUÇÃO [retirada / exclusão / falecimento]
III – DA DATA DA RESOLUÇÃO (art. 605)
IV – DA APURAÇÃO DE HAVERES (art. 606)
V – DOS PEDIDOS
a) a citação da sociedade e dos sócios para concordar ou contestar em 15 dias (art. 601);
b) a decretação da dissolução parcial;
c) a apuração e o pagamento dos haveres do autor;
d) custas e honorários.

Dá-se à causa o valor de R$ [valor estimado dos haveres].

{FECHO}""", ["CPC:599","CPC:601","CPC:603","CPC:605","CPC:606","CC:1029","CC:1031"]),
]
