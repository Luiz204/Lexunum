# Peças de Processo Penal — Lex Unum (conteúdo autoral).
from base import *

G = "Processo Penal"
TJ = "EXCELENTÍSSIMO(A) SENHOR(A) DESEMBARGADOR(A) PRESIDENTE DO TRIBUNAL DE JUSTIÇA DO ESTADO DE [UF]"

PECAS = [
P("resposta-acusacao", "Resposta à Acusação", G,
  "Primeira defesa do acusado no procedimento comum (ordinário e sumário), após o recebimento da denúncia ou queixa e a citação.",
  "10 dias da citação (CPP, art. 396)",
  "CPP, arts. 396, 396-A e 397",
  ["Arguição de preliminares e nulidades", "Teses de absolvição sumária (art. 397)", "Juntada de documentos e justificações", "Rol de testemunhas, com pedido de intimação (até 8 no ordinário e 5 no sumário)"],
  ["É peça obrigatória: se não apresentada, o juiz nomeia defensor (art. 396-A, § 2º)", "É o momento de arrolar testemunhas, sob pena de preclusão", "Absolvição sumária: excludente de ilicitude, excludente de culpabilidade (salvo inimputabilidade), fato atípico ou extinção da punibilidade"],
  f"""{JUIZO_CRIMINAL}

{PROC}

[NOME DO ACUSADO], já qualificado nos autos, {ADV}, vem apresentar

RESPOSTA À ACUSAÇÃO

com fundamento nos arts. 396 e 396-A do CPP, pelas razões a seguir.

I – SÍNTESE DA DENÚNCIA
II – PRELIMINARMENTE
[Nulidades, inépcia da denúncia (art. 41), falta de justa causa (art. 395, III).]
III – DA ABSOLVIÇÃO SUMÁRIA (art. 397)
[Inciso aplicável: I – excludente de ilicitude; II – excludente de culpabilidade; III – fato não constitui crime; IV – extinta a punibilidade.]
IV – DOS PEDIDOS
a) o acolhimento das preliminares, com a rejeição da denúncia;
b) subsidiariamente, a absolvição sumária do acusado, com fundamento no art. 397, [inciso], do CPP;
c) não sendo o caso, a produção de todas as provas admitidas e a intimação das testemunhas abaixo arroladas.

ROL DE TESTEMUNHAS
1. [nome, qualificação e endereço]

{FECHO}""", ["CPP:395","CPP:396","CPP:396-A","CPP:397","CPP:41"]),

P("memoriais-penal", "Memoriais (Alegações Finais por Escrito)", G,
  "Ao final da instrução criminal, quando o juiz concede prazo para alegações escritas em razão da complexidade do caso ou do número de acusados.",
  "5 dias, sucessivamente para acusação e defesa (CPP, art. 403, § 3º)",
  "CPP, arts. 403, § 3º, e 404",
  ["Preliminares e nulidades ocorridas na instrução", "Análise da prova produzida", "Teses de mérito (absolvição — art. 386)", "Teses subsidiárias de dosimetria, regime e substituição da pena"],
  ["Na OAB, sempre organize: preliminares, mérito (absolvição) e pedidos subsidiários", "Indique o inciso do art. 386 adequado a cada tese", "Peça a desclassificação, o afastamento de qualificadoras e as atenuantes"],
  f"""{JUIZO_CRIMINAL}

{PROC}

[NOME DO ACUSADO], já qualificado, {ADV}, vem apresentar

MEMORIAIS

com fundamento no art. 403, § 3º, do CPP.

I – SÍNTESE DO PROCESSO
II – PRELIMINARMENTE: DAS NULIDADES
III – DO MÉRITO
III.1 – Da absolvição [art. 386, inciso __]
III.2 – Subsidiariamente: da desclassificação / do afastamento da qualificadora
IV – DA DOSIMETRIA (subsidiariamente)
[Pena-base no mínimo; atenuantes (art. 65); causas de diminuição; regime inicial mais brando (art. 33); substituição (art. 44); sursis (art. 77).]
V – DOS PEDIDOS
a) o reconhecimento das nulidades;
b) a absolvição do acusado com fundamento no art. 386, [inciso], do CPP;
c) subsidiariamente, [desclassificação / pena mínima / regime aberto / substituição por restritivas de direitos];
d) o direito de recorrer em liberdade.

{FECHO}""", ["CPP:386","CPP:403","CPP:404","CP:33","CP:44","CP:59","CP:65"]),

P("queixa-crime", "Queixa-Crime", G,
  "Peça inicial da ação penal privada, proposta pelo ofendido ou seu representante legal (ex.: crimes contra a honra, salvo exceções).",
  "6 meses do conhecimento da autoria, sob pena de decadência (CPP, art. 38; CP, art. 103)",
  "CPP, arts. 30, 41, 44 e 45",
  ["Requisitos do art. 41 do CPP (fato, circunstâncias, qualificação, classificação e rol de testemunhas)", "Procuração com poderes especiais, com menção ao fato criminoso (art. 44)", "Inclusão de todos os autores (indivisibilidade — art. 48)", "Pedido de condenação"],
  ["A omissão de um dos autores pode configurar renúncia tácita a todos (art. 49)", "Nos crimes de menor potencial ofensivo, o endereçamento é ao JECRIM", "Prazo decadencial não se suspende nem se interrompe"],
  f"""AO JUÍZO DO [JUIZADO ESPECIAL CRIMINAL / ___ VARA CRIMINAL] DA COMARCA DE [CIDADE/UF]

{PF("QUERELANTE")}, {ADV} (procuração com poderes especiais — art. 44 do CPP), vem oferecer

QUEIXA-CRIME

em face de {PF("QUERELADO(A)")}, pela prática do crime previsto no art. [__] do Código Penal, pelos fatos a seguir.

I – DOS FATOS
[Data, local, conduta e circunstâncias — art. 41 do CPP.]
II – DO DIREITO
[Tipicidade da conduta e classificação.]
III – DOS PEDIDOS
a) o recebimento da queixa-crime e a citação do querelado;
b) [a designação de audiência de conciliação — art. 520 do CPP, nos crimes contra a honra];
c) a intimação do Ministério Público (art. 45);
d) a condenação do querelado nas penas do art. [__] do CP;
e) a fixação de valor mínimo de reparação (art. 387, IV).

ROL DE TESTEMUNHAS
1. [nome e endereço]

{FECHO}""", ["CPP:30","CPP:38","CPP:41","CPP:44","CPP:45","CPP:48","CPP:49","CPP:387","CPP:520","CP:103"]),

P("relaxamento-prisao", "Pedido de Relaxamento de Prisão", G,
  "Quando a prisão é ilegal — flagrante sem situação de flagrância, sem formalidades, excesso de prazo, ausência de audiência de custódia sem justificativa etc.",
  "A qualquer tempo, enquanto durar a prisão ilegal",
  "CF, art. 5º, LXV; CPP, art. 310, I",
  ["Demonstração da ilegalidade da prisão", "Pedido de relaxamento e expedição de alvará de soltura"],
  ["Relaxamento = prisão ILEGAL; liberdade provisória = prisão legal, mas desnecessária; revogação = preventiva sem requisitos atuais", "Na OAB, se a prisão em flagrante é ilegal, o pedido é de relaxamento", "Se o juiz não relaxar, cabe habeas corpus"],
  f"""{JUIZO_CRIMINAL}

Auto de Prisão em Flagrante nº [número]

[NOME DO PRESO], já qualificado, {ADV}, vem requerer o

RELAXAMENTO DA PRISÃO

com fundamento no art. 5º, LXV, da CF e no art. 310, I, do CPP, pelos fatos a seguir.

I – DOS FATOS
II – DA ILEGALIDADE DA PRISÃO
[Ausência de situação de flagrância (art. 302) / vício formal no auto / excesso de prazo.]
III – DO PEDIDO
Requer o relaxamento da prisão ilegal, com a imediata expedição de alvará de soltura.

{FECHO}""", ["CF:5","CPP:302","CPP:310"]),

P("liberdade-provisoria", "Pedido de Liberdade Provisória", G,
  "Quando a prisão em flagrante é legal, mas não estão presentes os requisitos da prisão preventiva (CPP, art. 312).",
  "A qualquer tempo após a prisão em flagrante",
  "CF, art. 5º, LXVI; CPP, arts. 310, III, 321 e 350",
  ["Demonstração da ausência dos requisitos da preventiva", "Condições pessoais favoráveis (primariedade, residência, trabalho)", "Pedido com ou sem fiança, cumulado ou não com cautelares do art. 319"],
  ["A gravidade abstrata do crime não impede a liberdade provisória", "Crimes hediondos não admitem fiança, mas admitem liberdade provisória sem fiança", "Ao preso pobre, o juiz pode dispensar a fiança (art. 350)"],
  f"""{JUIZO_CRIMINAL}

Auto de Prisão em Flagrante nº [número]

[NOME DO PRESO], {ADV}, vem requerer

LIBERDADE PROVISÓRIA [SEM / COM] FIANÇA

com fundamento no art. 5º, LXVI, da CF e nos arts. 310, III, e 321 do CPP.

I – DOS FATOS
II – DA AUSÊNCIA DOS REQUISITOS DA PRISÃO PREVENTIVA (arts. 312 e 313)
III – DAS CONDIÇÕES PESSOAIS FAVORÁVEIS
IV – DA SUFICIÊNCIA DAS MEDIDAS CAUTELARES DIVERSAS (art. 319)
V – DO PEDIDO
Requer a concessão de liberdade provisória [sem fiança / com dispensa da fiança — art. 350], [com as cautelares que Vossa Excelência entender adequadas], expedindo-se alvará de soltura.

{FECHO}""", ["CF:5","CPP:310","CPP:312","CPP:319","CPP:321","CPP:350"]),

P("revogacao-preventiva", "Pedido de Revogação da Prisão Preventiva", G,
  "Quando a prisão preventiva foi decretada, mas os motivos que a justificaram deixaram de existir ou nunca estiveram presentes.",
  "A qualquer tempo",
  "CPP, arts. 312, 315 e 316",
  ["Indicação da decisão que decretou a preventiva", "Demonstração de que os fundamentos desapareceram ou são inidôneos", "Pedido subsidiário de substituição por cautelares diversas (art. 282, § 6º)"],
  ["A preventiva deve ser revisada a cada 90 dias (art. 316, parágrafo único)", "Fundamentação genérica é nula (art. 315, § 2º)", "Gestante, mãe de criança até 12 anos ou responsável por pessoa com deficiência pode ter prisão domiciliar (art. 318-A)"],
  f"""{JUIZO_CRIMINAL}

{PROC}

[NOME DO ACUSADO], {ADV}, vem requerer a

REVOGAÇÃO DA PRISÃO PREVENTIVA

com fundamento no art. 316 do CPP.

I – DA DECISÃO QUE DECRETOU A PREVENTIVA
II – DA AUSÊNCIA SUPERVENIENTE DOS REQUISITOS / DA FUNDAMENTAÇÃO INIDÔNEA (arts. 312 e 315)
III – DA SUFICIÊNCIA DAS CAUTELARES DIVERSAS (art. 319)
IV – DO PEDIDO
Requer a revogação da prisão preventiva ou, subsidiariamente, sua substituição por medidas cautelares diversas, com a expedição de alvará de soltura.

{FECHO}""", ["CPP:282","CPP:312","CPP:315","CPP:316","CPP:318-A","CPP:319"]),

P("rese", "Recurso em Sentido Estrito", G,
  "Contra as decisões listadas no art. 581 do CPP, como as que rejeitam a denúncia, pronunciam o réu, concedem ou negam fiança e julgam extinta a punibilidade.",
  "5 dias para interpor (CPP, art. 586); 2 dias para as razões (art. 588)",
  "CPP, arts. 581 a 592",
  ["Petição de interposição ao juiz, com pedido de retratação (art. 589)", "Razões dirigidas ao tribunal", "Indicação do inciso do art. 581"],
  ["O RESE admite juízo de retratação", "Contra a pronúncia cabe RESE (art. 581, IV); contra impronúncia e absolvição sumária, apelação (art. 416)", "Decisão que rejeita a denúncia no JECRIM desafia apelação (Lei 9.099/1995, art. 82)"],
  f"""{JUIZO_CRIMINAL}

{PROC}

[NOME DO RECORRENTE], {ADV}, inconformado com a decisão de fls. [__], vem interpor

RECURSO EM SENTIDO ESTRITO

com fundamento no art. 581, [inciso], do CPP, requerendo, caso não haja retratação (art. 589), a remessa ao Tribunal de Justiça.

{FECHO}

---

RAZÕES DE RECURSO EM SENTIDO ESTRITO
Recorrente: [nome] — Recorrido: [Ministério Público / nome]

Egrégio Tribunal,
I – DA TEMPESTIVIDADE E DO CABIMENTO
II – DOS FATOS E DA DECISÃO RECORRIDA
III – DAS RAZÕES DE REFORMA
IV – DO PEDIDO
Requer o provimento do recurso para [reformar a decisão de pronúncia, impronunciando o réu / etc.].

{FECHO}""", ["CPP:581","CPP:586","CPP:588","CPP:589","CPP:416"]),

P("apelacao-criminal", "Apelação Criminal", G,
  "Contra sentenças definitivas de condenação ou absolvição, decisões definitivas ou com força de definitivas não impugnáveis por RESE e decisões do Júri (art. 593).",
  "5 dias para interpor (CPP, art. 593); 8 dias para as razões (art. 600)",
  "CPP, arts. 593 a 603",
  ["Petição de interposição ao juiz e razões ao tribunal", "No Júri, indicação da alínea do art. 593, III", "Teses de absolvição e subsidiárias de dosimetria"],
  ["É possível arrazoar diretamente no tribunal (art. 600, § 4º)", "No Júri, a apelação é vinculada às alíneas do art. 593, III (Súmula 713 do STF)", "Vedação da reformatio in pejus em recurso exclusivo da defesa (art. 617)"],
  f"""{JUIZO_CRIMINAL}

{PROC}

[NOME DO APELANTE], {ADV}, inconformado com a sentença de fls. [__], vem interpor

APELAÇÃO

com fundamento no art. 593, [inciso/alínea], do CPP, requerendo o recebimento e a remessa ao Tribunal de Justiça [com as razões anexas / protestando por arrazoar na instância superior — art. 600, § 4º].

{FECHO}

---

RAZÕES DE APELAÇÃO
Apelante: [nome] — Apelado: Ministério Público

Egrégio Tribunal, Colenda Câmara Criminal,
I – DA TEMPESTIVIDADE
II – DOS FATOS
III – PRELIMINARMENTE: DAS NULIDADES
IV – DO MÉRITO: DA ABSOLVIÇÃO (art. 386, [inciso])
V – SUBSIDIARIAMENTE: DA DOSIMETRIA, DO REGIME E DA SUBSTITUIÇÃO
VI – DO PEDIDO
Requer o provimento do recurso para [anular o processo / absolver o apelante / reduzir a pena / fixar regime aberto / substituir a pena].

{FECHO}""", ["CPP:593","CPP:600","CPP:617","CPP:386"]),

P("embargos-infringentes-penal", "Embargos Infringentes e de Nulidade", G,
  "Exclusivos da defesa, contra acórdão não unânime de segundo grau desfavorável ao réu, em apelação, RESE ou agravo em execução.",
  "10 dias da publicação do acórdão (CPP, art. 609, parágrafo único)",
  "CPP, art. 609, parágrafo único",
  ["Limitados à matéria objeto da divergência", "Fundamentação no voto vencido", "Dirigidos ao relator do acórdão embargado"],
  ["Não cabem para a acusação", "Infringentes: divergência de mérito; de nulidade: divergência sobre nulidade processual", "Não cabem contra acórdão em revisão criminal ou habeas corpus originário"],
  f"""EXCELENTÍSSIMO(A) SENHOR(A) DESEMBARGADOR(A) RELATOR(A) DA APELAÇÃO CRIMINAL Nº [__]

[NOME DO EMBARGANTE], {ADV}, vem opor

EMBARGOS INFRINGENTES [E DE NULIDADE]

contra o acórdão não unânime de fls. [__], com fundamento no art. 609, parágrafo único, do CPP, requerendo o processamento e o julgamento pelo órgão competente.

I – DA TEMPESTIVIDADE E DO CABIMENTO
II – DO ACÓRDÃO E DO VOTO VENCIDO
III – DAS RAZÕES PARA PREVALÊNCIA DO VOTO VENCIDO
IV – DO PEDIDO
Requer o provimento dos embargos para que prevaleça o voto vencido, [absolvendo o embargante / reconhecendo a nulidade].

{FECHO}""", ["CPP:609"]),

P("revisao-criminal", "Revisão Criminal", G,
  "Ação autônoma de impugnação contra sentença condenatória transitada em julgado, nas hipóteses do art. 621 do CPP (decisão contrária à lei ou à evidência dos autos, prova falsa, provas novas de inocência ou de circunstância que diminua a pena).",
  "A qualquer tempo, antes ou depois de extinta a pena (CPP, art. 622)",
  "CPP, arts. 621 a 631",
  ["Competência originária do tribunal", "Certidão de trânsito em julgado", "Indicação da hipótese do art. 621", "Provas pré-constituídas (justificação criminal, se necessário)"],
  ["Só cabe em favor do réu (pro reo)", "Pode ser proposta pelo próprio réu, sem advogado, ou por cônjuge, ascendente, descendente ou irmão se ele tiver falecido (art. 623)", "Pode-se pedir indenização pelo erro judiciário (art. 630)"],
  f"""{TJ}

{PF("REQUERENTE")}, {ADV}, vem propor

REVISÃO CRIMINAL

da sentença condenatória proferida nos autos nº [número], transitada em julgado em [data], com fundamento no art. 621, [inciso], do CPP.

I – DA DECISÃO REVISANDA
II – DO CABIMENTO (art. 621, [inciso])
III – DAS RAZÕES DA REVISÃO
IV – DA INDENIZAÇÃO (art. 630), se for o caso
V – DOS PEDIDOS
Requer a procedência da revisão para [absolver o requerente / anular o processo / reduzir a pena], com o restabelecimento de todos os direitos perdidos (art. 627) [e o reconhecimento do direito à indenização].

{FECHO}""", ["CPP:621","CPP:622","CPP:623","CPP:626","CPP:627","CPP:630"]),

P("agravo-execucao", "Agravo em Execução", G,
  "Contra as decisões proferidas pelo juiz da execução penal (progressão, remição, livramento, falta grave, unificação de penas etc.).",
  "5 dias (Súmula 700 do STF), seguindo o rito do RESE",
  "LEP, art. 197",
  ["Interposição ao juiz da execução, com pedido de retratação", "Razões ao tribunal", "Cópias da decisão agravada e dos cálculos de pena"],
  ["Não tem efeito suspensivo", "Segue, por analogia, o procedimento do RESE", "Na OAB, é a peça típica contra decisões sobre progressão e falta grave"],
  f"""AO JUÍZO DA VARA DE EXECUÇÕES PENAIS DA COMARCA DE [CIDADE/UF]

Execução Penal nº [número]

[NOME DO SENTENCIADO], {ADV}, inconformado com a decisão de fls. [__], vem interpor

AGRAVO EM EXECUÇÃO

com fundamento no art. 197 da Lei 7.210/1984, requerendo a retratação ou a remessa ao Tribunal de Justiça.

{FECHO}

---

RAZÕES DE AGRAVO EM EXECUÇÃO
I – DA TEMPESTIVIDADE (Súmula 700 do STF)
II – DA DECISÃO AGRAVADA
III – DAS RAZÕES DE REFORMA
[Ex.: preenchimento dos requisitos de progressão (LEP, art. 112).]
IV – DO PEDIDO
Requer o provimento do agravo para [conceder a progressão / reconhecer a remição / afastar a falta grave].

{FECHO}""", ["LEP:66","LEP:112","LEP:118","LEP:126","LEP:197"]),

P("rohc", "Recurso Ordinário em Habeas Corpus", G,
  "Contra acórdão que denega habeas corpus decidido em única ou última instância pelos tribunais (ao STJ) ou em única instância pelos tribunais superiores (ao STF).",
  "5 dias (Lei 8.038/1990, art. 30; STJ) ",
  "CF, arts. 102, II, a, e 105, II, a",
  ["Interposição perante o tribunal que denegou a ordem", "Razões ao STJ ou ao STF", "Cópia do acórdão denegatório"],
  ["Cabe apenas contra decisão DENEGATÓRIA", "Não exige prequestionamento", "Na prática, é comum a impetração de HC substitutivo, mas a peça tecnicamente correta é o recurso ordinário"],
  f"""{TJ}

Habeas Corpus nº [número]

[NOME DO PACIENTE], {ADV}, vem interpor

RECURSO ORDINÁRIO EM HABEAS CORPUS

contra o acórdão que denegou a ordem, com fundamento no art. 105, II, a, da CF, requerendo a remessa ao Superior Tribunal de Justiça.

{FECHO}

---

RAZÕES DO RECURSO ORDINÁRIO
I – DA TEMPESTIVIDADE E DO CABIMENTO
II – DOS FATOS E DO ACÓRDÃO RECORRIDO
III – DO CONSTRANGIMENTO ILEGAL
IV – DO PEDIDO LIMINAR
V – DO PEDIDO
Requer o provimento do recurso para conceder a ordem de habeas corpus, [expedindo-se alvará de soltura / trancando-se a ação penal].

{FECHO}""", ["CF:102","CF:105","L8038:30"]),

P("contrarrazoes-apelacao-criminal", "Contrarrazões de Apelação Criminal", G,
  "Resposta da defesa à apelação interposta pelo Ministério Público ou pelo assistente de acusação.",
  "8 dias (CPP, art. 600)",
  "CPP, art. 600",
  ["Defesa da sentença absolutória ou da pena aplicada", "Preliminares de não conhecimento do recurso, se houver"],
  ["Aponte a intempestividade do recurso da acusação, se houver", "Reforce a fragilidade probatória (in dubio pro reo)"],
  f"""{JUIZO_CRIMINAL}

{PROC}

[NOME DO APELADO], {ADV}, vem apresentar

CONTRARRAZÕES DE APELAÇÃO

ao recurso interposto pelo Ministério Público, requerendo a remessa ao Tribunal de Justiça.

{FECHO}

---

CONTRARRAZÕES
I – DA SÍNTESE DO RECURSO
II – PRELIMINARMENTE: DO NÃO CONHECIMENTO [se houver]
III – DO MÉRITO: DO ACERTO DA SENTENÇA
IV – DO PEDIDO
Requer o não provimento do recurso, mantendo-se integralmente a sentença.

{FECHO}""", ["CPP:600","CPP:386"]),

P("embargos-declaracao-penal", "Embargos de Declaração (Penal)", G,
  "Contra sentença ou acórdão criminal com ambiguidade, obscuridade, contradição ou omissão.",
  "2 dias (CPP, arts. 382 e 619)",
  "CPP, arts. 382, 619 e 620",
  ["Indicação precisa do vício", "Dirigidos ao próprio juiz ou relator"],
  ["No JECRIM, o prazo é de 5 dias (Lei 9.099/1995, art. 83)", "Interrompem o prazo para outros recursos"],
  f"""{JUIZO_CRIMINAL}

{PROC}

[NOME DO EMBARGANTE], {ADV}, vem opor

EMBARGOS DE DECLARAÇÃO

em face da sentença de fls. [__], com fundamento no art. 382 do CPP.

I – DA TEMPESTIVIDADE (2 dias)
II – DO VÍCIO [ambiguidade / obscuridade / contradição / omissão]
III – DO PEDIDO
Requer o acolhimento dos embargos para sanar o vício apontado.

{FECHO}""", ["CPP:382","CPP:619","CPP:620"]),

P("restituicao-coisa-apreendida", "Pedido de Restituição de Coisa Apreendida", G,
  "Para reaver bens apreendidos que não interessam mais ao processo e não são instrumento ou produto do crime de posse ilícita.",
  "Enquanto o bem estiver apreendido, antes do trânsito em julgado",
  "CPP, arts. 118 a 124",
  ["Prova da propriedade", "Demonstração de que o bem não interessa ao processo", "Demonstração de que não é bem de confisco obrigatório (CP, art. 91, II)"],
  ["Havendo dúvida sobre o direito do reclamante, o pedido é autuado em apartado (art. 120, § 1º)", "Terceiro de boa-fé pode pedir a restituição", "Da decisão cabe apelação (art. 593, II)"],
  f"""{JUIZO_CRIMINAL}

Inquérito / Processo nº [número]

{PF("REQUERENTE")}, {ADV}, vem requerer a

RESTITUIÇÃO DE COISA APREENDIDA

com fundamento nos arts. 118 e 120 do CPP.

I – DOS FATOS
II – DA PROPRIEDADE DO BEM
III – DA DESNECESSIDADE DA APREENSÃO PARA O PROCESSO
IV – DO PEDIDO
Requer a restituição do bem [descrição], ouvido o Ministério Público (art. 120, § 3º).

{FECHO}""", ["CPP:118","CPP:120","CP:91"]),

P("defesa-previa-drogas", "Defesa Prévia (Lei de Drogas)", G,
  "No procedimento especial da Lei 11.343/2006, antes do recebimento da denúncia, após a notificação do acusado.",
  "10 dias da notificação (Lei 11.343/2006, art. 55)",
  "Lei 11.343/2006, arts. 55 e 56",
  ["Preliminares e exceções", "Teses de rejeição da denúncia", "Rol de até 5 testemunhas", "Especificação das provas"],
  ["Diferente da resposta à acusação, é apresentada ANTES do recebimento da denúncia", "Tese frequente: desclassificação para uso próprio (art. 28)", "Tráfico privilegiado reduz a pena de 1/6 a 2/3 e não é hediondo (art. 33, § 4º)"],
  f"""{JUIZO_CRIMINAL}

{PROC}

[NOME DO ACUSADO], {ADV}, vem apresentar

DEFESA PRÉVIA

com fundamento no art. 55 da Lei 11.343/2006.

I – SÍNTESE DA DENÚNCIA
II – PRELIMINARMENTE
[Nulidade do flagrante, ilicitude de provas, inépcia.]
III – DA REJEIÇÃO DA DENÚNCIA (CPP, art. 395)
IV – SUBSIDIARIAMENTE: DA DESCLASSIFICAÇÃO PARA O ART. 28 / DO TRÁFICO PRIVILEGIADO (art. 33, § 4º)
V – DOS PEDIDOS
a) a rejeição da denúncia;
b) subsidiariamente, a produção das provas e a oitiva das testemunhas arroladas.

ROL DE TESTEMUNHAS (até 5)
1. [nome e endereço]

{FECHO}""", ["LD:28","LD:33","LD:55","LD:56","CPP:395"]),
]
