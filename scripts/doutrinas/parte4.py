# Conteúdo autoral de estudo — Lex Unum. Ética, Direitos Humanos, Previdenciário, Criança e Adolescente.
from parte1 import T

DADOS = {
"etica": [
T("Estatuto da Advocacia", """
O Estatuto da Advocacia e da OAB (Lei 8.906/1994) disciplina a atividade privativa de advocacia, os direitos e deveres do advogado e a organização da Ordem. O advogado é indispensável à administração da justiça (CF, art. 133) e, no seu ministério privado, presta serviço público e exerce função social (EAOAB, art. 2º).

São atividades privativas da advocacia a postulação a órgão do Poder Judiciário e aos juizados especiais e as atividades de consultoria, assessoria e direção jurídicas (art. 1º). A postulação não é privativa no habeas corpus, e o STF admitiu que a parte atue sem advogado nos juizados especiais cíveis até 20 salários mínimos e na Justiça do Trabalho (jus postulandi). Atos privativos praticados por não inscrito são nulos.

Para a inscrição como advogado, exigem-se capacidade civil, diploma de graduação em Direito, título de eleitor e quitação militar (se brasileiro), aprovação no Exame de Ordem, não exercer atividade incompatível, idoneidade moral e compromisso perante o Conselho (art. 8º). Atenção à distinção entre incompatibilidade (proibição total de advogar, art. 28) e impedimento (proibição parcial, art. 30).
""", [
 "Advogado indispensável à administração da justiça (CF, art. 133; EAOAB, art. 2º).",
 "Atividades privativas: art. 1º; nulidade dos atos de não inscrito (art. 4º).",
 "Requisitos de inscrição: art. 8º.",
 "Incompatibilidades: art. 28; impedimentos: art. 30.",
 "Direitos do advogado, incluindo inviolabilidade do escritório: art. 7º.",
], [
 "Servidores da administração pública são impedidos de advogar contra a Fazenda que os remunera (art. 30, I) — impedimento, não incompatibilidade.",
 "Docentes de cursos jurídicos não são impedidos de advogar (art. 30, parágrafo único).",
 "Estagiário pode praticar atos em conjunto com advogado e sob sua responsabilidade (art. 3º, § 2º).",
], ["EOAB:1","EOAB:2","EOAB:3","EOAB:4","EOAB:7","EOAB:8","EOAB:28","EOAB:30","CF:133"]),

T("Código de Ética e Disciplina", """
O Código de Ética e Disciplina da OAB (aprovado pelo Conselho Federal em 2015) orienta a conduta do advogado nas relações com clientes, colegas, autoridades e a sociedade. Entre seus deveres estão atuar com honestidade, lealdade e boa-fé, estimular a conciliação, aconselhar o cliente a não ingressar em aventura judicial e preservar a independência profissional.

O advogado deve recusar o patrocínio de causa quando houver conflito de interesses e não pode representar, em juízo, clientes com interesses opostos. A renúncia ao mandato deve ser comunicada ao cliente, e o advogado continua responsável pelos atos necessários nos 10 dias seguintes, salvo se substituído antes (EAOAB, art. 5º, § 3º). O advogado tem liberdade para recusar causa que contrarie sua consciência, mas, aceito o patrocínio, deve exercê-lo com zelo.

A publicidade profissional é permitida com caráter meramente informativo, primando pela discrição e pela sobriedade, sem configurar captação de clientela ou mercantilização da profissão. O Provimento 205/2021 do Conselho Federal disciplina o marketing jurídico, inclusive nas redes sociais, admitindo conteúdo informativo e vedando a ostentação e a promessa de resultados.
""", [
 "Deveres de lealdade, boa-fé e estímulo à conciliação.",
 "Vedação de patrocinar interesses conflitantes.",
 "Renúncia ao mandato: responsabilidade pelos 10 dias seguintes (EAOAB, art. 5º, § 3º).",
 "Publicidade informativa, discreta e sóbria; vedada a mercantilização.",
 "Marketing jurídico: Provimento 205/2021.",
], [
 "É vedado divulgar a advocacia em conjunto com outra atividade (Código de Ética, art. 40, IV).",
 "Promessa de resultados e menção a valores de honorários em publicidade são vedadas.",
 "O advogado pode recusar a causa por razões de consciência, mas não pode abandoná-la sem renúncia formal.",
], ["EOAB:5","EOAB:31","EOAB:33","EOAB:34"]),

T("Sigilo Profissional", """
O sigilo profissional é ao mesmo tempo direito e dever do advogado, inerente à profissão e de ordem pública. O advogado deve guardar sigilo sobre os fatos de que tome conhecimento no exercício da profissão, ainda que não tenha sido contratado ou que o mandato tenha terminado. O sigilo protege a relação de confiança com o cliente e o direito de defesa.

O Estatuto assegura ao advogado o direito de recusar-se a depor como testemunha em processo no qual funcionou ou deva funcionar, ou sobre fato relacionado com pessoa de quem seja ou foi advogado, mesmo quando autorizado ou solicitado pelo constituinte (art. 7º, XIX). A inviolabilidade do escritório e dos instrumentos de trabalho é garantida, e a quebra só é possível por decisão judicial fundamentada, havendo indícios de crime cometido pelo próprio advogado, com a presença de representante da OAB (art. 7º, II e § 6º).

O sigilo admite exceções restritas, como grave ameaça ao direito à vida ou à honra, ou quando o advogado se veja afrontado pelo próprio cliente e precise revelar fatos em sua defesa, sempre nos limites da necessidade. Violar o sigilo sem justa causa é infração disciplinar (art. 34, VII).
""", [
 "Sigilo como direito e dever do advogado.",
 "Direito de recusar-se a depor (EAOAB, art. 7º, XIX).",
 "Inviolabilidade do escritório e quebra só com ordem judicial e presença da OAB (art. 7º, II e § 6º).",
 "Violação do sigilo sem justa causa é infração (art. 34, VII).",
 "Exceções: ameaça à vida ou à honra e defesa própria do advogado.",
], [
 "A autorização do cliente não obriga o advogado a depor sobre fatos sigilosos.",
 "Documentos de clientes investigados não podem ser apreendidos no escritório, salvo se forem corpo de delito (art. 7º, § 7º).",
 "O sigilo persiste após o fim do mandato.",
], ["EOAB:7","EOAB:34"]),

T("Honorários", """
Honorários são a contraprestação pelos serviços do advogado e têm natureza alimentar (CF, art. 100, § 1º; Súmula Vinculante 47). O Estatuto prevê três espécies: convencionais (contratados com o cliente), fixados por arbitramento judicial (na falta de estipulação) e de sucumbência (pagos pela parte vencida).

Os honorários de sucumbência pertencem ao advogado (EAOAB, art. 23), que pode executá-los autonomamente, inclusive nos próprios autos. O CPC fixa os parâmetros: entre 10% e 20% do valor da condenação, do proveito econômico ou do valor da causa (art. 85, § 2º), com faixas escalonadas contra a Fazenda Pública (§ 3º) e vedação de compensação em caso de sucumbência parcial (§ 14). Também são devidos honorários recursais, majorando a verba na instância superior (§ 11).

A cobrança de honorários prescreve em 5 anos (EAOAB, art. 25). No contrato de honorários, admite-se a cláusula quota litis, em que o advogado recebe percentual do proveito, desde que não supere as vantagens do cliente. O advogado que deixa a causa recebe honorários proporcionais ao trabalho realizado.
""", [
 "Espécies: convencionais, por arbitramento e de sucumbência (EAOAB, art. 22).",
 "Sucumbência pertence ao advogado (EAOAB, art. 23).",
 "Parâmetros do CPC: 10% a 20% (art. 85, § 2º); honorários recursais (§ 11).",
 "Vedada a compensação de honorários na sucumbência recíproca (CPC, art. 85, § 14).",
 "Prescrição da cobrança: 5 anos (EAOAB, art. 25).",
], [
 "Honorários têm natureza alimentar (Súmula Vinculante 47).",
 "A Súmula 306 do STJ, que admitia compensação, ficou superada pelo CPC/2015.",
 "Honorários contratuais não se confundem com os sucumbenciais e podem ser cumulados.",
], ["EOAB:22","EOAB:23","EOAB:24","EOAB:25","CPC:85","CF:100"], ["SV-47"]),

T("Infrações Disciplinares", """
As infrações disciplinares estão listadas no art. 34 do Estatuto, e as sanções são censura, suspensão, exclusão e multa (art. 35). A censura cabe nas infrações menos graves (incisos I a XVI e XXIX) e pode ser convertida em advertência, em ofício reservado, quando houver circunstância atenuante. A suspensão alcança infrações como a recusa injustificada de prestar contas, a retenção abusiva de autos e o inadimplemento de anuidades, e impede o exercício da profissão em todo o território nacional pelo prazo de 30 dias a 12 meses.

A exclusão aplica-se em casos graves, como a aplicação de suspensão por três vezes, a perda de idoneidade moral e a prática de crime infamante, e exige manifestação favorável de 2/3 dos membros do Conselho Seccional competente (art. 38). A multa varia de uma a dez anuidades e é cumulável com censura ou suspensão quando houver agravantes.

O processo disciplinar é sigiloso até o término e garante o contraditório e a ampla defesa. A pretensão punitiva prescreve em 5 anos, contados da constatação oficial do fato, e há prescrição intercorrente quando o processo fica paralisado por mais de 3 anos (art. 43).
""", [
 "Infrações: art. 34; sanções: art. 35.",
 "Censura (art. 36), suspensão (art. 37) e exclusão (art. 38).",
 "Exclusão exige 2/3 do Conselho Seccional (art. 38, parágrafo único).",
 "Processo disciplinar sigiloso (art. 72, § 2º).",
 "Prescrição: 5 anos da constatação oficial; intercorrente após 3 anos de paralisação (art. 43).",
], [
 "Captação de causas (art. 34, IV) e angariar clientela por meio de agenciador são infrações.",
 "A suspensão por inadimplência perdura até a quitação da dívida (art. 37, § 2º).",
 "A reabilitação pode ser requerida 1 ano após o cumprimento da sanção (art. 41).",
], ["EOAB:34","EOAB:35","EOAB:36","EOAB:37","EOAB:38","EOAB:39","EOAB:41","EOAB:43","EOAB:72"]),
],

"direitos-humanos": [
T("Sistema ONU", """
O sistema global de proteção dos direitos humanos foi construído após a Segunda Guerra Mundial, a partir da Carta da ONU (1945) e da Declaração Universal dos Direitos Humanos (1948). A Declaração, embora formalmente uma resolução da Assembleia Geral sem força vinculante, é considerada expressão do costume internacional e de princípios gerais de direito.

A Carta Internacional de Direitos Humanos (International Bill of Rights) reúne a Declaração Universal e os dois Pactos de 1966: o Pacto Internacional dos Direitos Civis e Políticos e o Pacto Internacional dos Direitos Econômicos, Sociais e Culturais, ambos ratificados pelo Brasil em 1992. A eles somam-se convenções temáticas, como as contra a tortura, a discriminação racial, a discriminação contra a mulher (CEDAW), sobre os direitos da criança e das pessoas com deficiência.

O monitoramento se faz por órgãos convencionais (comitês de cada tratado, que analisam relatórios periódicos e, quando o Estado aceita, petições individuais) e extraconvencionais, como o Conselho de Direitos Humanos e sua Revisão Periódica Universal, a que todos os Estados-membros se submetem.
""", [
 "Declaração Universal de 1948: soft law com força de costume internacional.",
 "Pactos de 1966 (civis e políticos; econômicos, sociais e culturais), ratificados pelo Brasil em 1992.",
 "Órgãos convencionais: comitês dos tratados (relatórios, petições individuais).",
 "Conselho de Direitos Humanos e Revisão Periódica Universal.",
 "Convenção sobre os Direitos das Pessoas com Deficiência tem status de emenda constitucional no Brasil.",
], [
 "O Conselho de Direitos Humanos substituiu a antiga Comissão de Direitos Humanos (2006).",
 "Petição individual a comitê da ONU exige aceitação do Estado, esgotamento dos recursos internos e ausência de litispendência internacional.",
 "Os direitos sociais do PIDESC têm realização progressiva, com vedação de retrocesso.",
], ["CF:4","CF:5"]),

T("Sistema Interamericano", """
O Sistema Interamericano de Direitos Humanos, no âmbito da Organização dos Estados Americanos (OEA), tem como principal instrumento a Convenção Americana sobre Direitos Humanos (Pacto de San José da Costa Rica, 1969), promulgada no Brasil pelo Decreto 678/1992. Seus órgãos são a Comissão Interamericana de Direitos Humanos (sede em Washington) e a Corte Interamericana de Direitos Humanos (sede em San José).

A Comissão recebe petições de qualquer pessoa, grupo ou ONG legalmente reconhecida sobre violações por Estado-parte, desde que esgotados os recursos internos, apresentada a petição em até 6 meses da decisão definitiva e inexistente litispendência internacional. Pode emitir recomendações e, se não cumpridas, submeter o caso à Corte. Indivíduos não têm acesso direto à Corte: só a Comissão e os Estados-partes podem submeter casos.

A Corte exerce competência contenciosa, com sentenças definitivas e inapeláveis, obrigatórias para os Estados que reconheceram sua jurisdição — o Brasil o fez em 1998 —, e competência consultiva. O Brasil já foi condenado em casos emblemáticos, como Damião Ximenes Lopes, Gomes Lund (Guerrilha do Araguaia) e Fazenda Brasil Verde.
""", [
 "Convenção Americana: Decreto 678/1992; status supralegal.",
 "Órgãos: Comissão e Corte Interamericanas.",
 "Requisitos de admissibilidade: esgotamento de recursos internos, 6 meses e ausência de litispendência.",
 "Só Comissão e Estados submetem casos à Corte.",
 "Brasil reconheceu a jurisdição contenciosa da Corte em 1998.",
], [
 "O indivíduo peticiona à Comissão, não diretamente à Corte.",
 "Sentenças da Corte Interamericana não dependem de homologação do STJ.",
 "A Convenção Americana veda a prisão civil por dívida, salvo alimentos (art. 7.7), o que fundamenta a Súmula Vinculante 25.",
], ["CF:5","CF:109","ADCT:7"], ["SV-25"]),

T("Tratados de Direitos Humanos", """
Os tratados de direitos humanos têm características próprias em relação aos tratados comuns: criam obrigações dos Estados perante as pessoas sob sua jurisdição, e não apenas relações recíprocas entre Estados; seguem o princípio pro persona, prevalecendo a norma mais favorável; e são interpretados de forma evolutiva, como instrumentos vivos.

O Brasil é parte dos principais tratados globais e regionais: os Pactos de 1966, a Convenção Americana, a Convenção contra a Tortura, a CEDAW, a Convenção de Belém do Pará (violência contra a mulher), a Convenção sobre os Direitos da Criança, a Convenção sobre os Direitos das Pessoas com Deficiência e a Convenção Interamericana contra o Racismo. Desses, a Convenção sobre os Direitos das Pessoas com Deficiência e a Convenção Interamericana contra o Racismo — além do Tratado de Marraqueche, sobre acesso a obras por pessoas com deficiência visual — foram aprovados pelo rito qualificado do art. 5º, § 3º.

Esses tratados influenciam diretamente a legislação interna: a Convenção de Belém do Pará inspirou a Lei Maria da Penha, e a Convenção sobre os Direitos das Pessoas com Deficiência fundamentou o Estatuto da Pessoa com Deficiência (Lei 13.146/2015) e a reforma do regime de capacidade civil.
""", [
 "Princípio pro persona: prevalece a norma mais favorável.",
 "Tratados aprovados pelo rito do art. 5º, § 3º: Convenção sobre PcD e seu Protocolo, Tratado de Marraqueche e Convenção Interamericana contra o Racismo.",
 "Convenção de Belém do Pará inspirou a Lei Maria da Penha.",
 "Convenção sobre PcD fundamentou o Estatuto da Pessoa com Deficiência.",
], [
 "Nem todo tratado de direitos humanos tem status de emenda: só os aprovados pelo rito qualificado.",
 "A Lei Maria da Penha aplica-se independentemente da orientação sexual (art. 2º).",
 "A Convenção Interamericana contra o Racismo foi aprovada com status de emenda constitucional em 2021.",
], ["CF:5","LMP:1","LMP:2","EPD:1"]),

T("Incorporação ao Direito Interno", """
A incorporação de tratados ao ordenamento brasileiro segue as etapas de assinatura pelo Presidente, aprovação pelo Congresso Nacional por decreto legislativo, ratificação e promulgação por decreto presidencial. Só depois da promulgação o tratado passa a ter vigência e executoriedade internas.

Quanto à hierarquia dos tratados de direitos humanos, o STF, no RE 466.343 (2008), fixou a tese da supralegalidade: os tratados de direitos humanos aprovados sem o rito do art. 5º, § 3º, estão abaixo da Constituição, mas acima das leis ordinárias, paralisando a eficácia da legislação infraconstitucional com eles conflitante. Os aprovados em dois turnos, por 3/5 dos votos em cada Casa, equivalem a emendas constitucionais e integram o bloco de constitucionalidade.

Daí decorre o duplo controle de verticalidade das leis: elas devem ser compatíveis com a Constituição (controle de constitucionalidade) e com os tratados de direitos humanos (controle de convencionalidade). O exemplo clássico é a prisão civil do depositário infiel, prevista na Constituição e no Código Civil, mas tornada inaplicável pelo Pacto de San José (Súmula Vinculante 25).
""", [
 "Etapas: assinatura, decreto legislativo, ratificação e decreto de promulgação.",
 "Tratados de direitos humanos sem rito qualificado: supralegais (RE 466.343).",
 "Com rito do art. 5º, § 3º: equivalentes a emendas constitucionais.",
 "Duplo controle: constitucionalidade e convencionalidade.",
 "Prisão do depositário infiel é ilícita (Súmula Vinculante 25).",
], [
 "Tratado supralegal não revoga a Constituição, mas paralisa a lei infraconstitucional conflitante.",
 "O decreto legislativo não basta: a vigência interna depende do decreto de promulgação.",
 "Status de emenda exige o mesmo quórum das emendas: 3/5, dois turnos, em cada Casa.",
], ["CF:5","CF:49","CF:84","CF:60"], ["SV-25"]),
],

"previdenciario": [
T("Regime Geral de Previdência", """
A seguridade social compreende saúde, previdência e assistência social (CF, art. 194). A previdência social organiza-se sob a forma de Regime Geral de caráter contributivo e de filiação obrigatória, observados critérios que preservem o equilíbrio financeiro e atuarial (art. 201). Ao lado do RGPS, gerido pelo INSS, existem os regimes próprios dos servidores (RPPS) e a previdência complementar, facultativa.

São segurados obrigatórios do RGPS o empregado, o empregado doméstico, o contribuinte individual, o trabalhador avulso e o segurado especial (pequeno produtor rural e pescador artesanal em regime de economia familiar). O segurado facultativo é quem, maior de 16 anos, se filia voluntariamente sem exercer atividade remunerada que o vincule obrigatoriamente, como estudantes e donas de casa.

A qualidade de segurado se mantém por um tempo mesmo sem contribuições (período de graça), em regra de 12 meses após a cessação das contribuições, com prorrogações previstas no art. 15 da Lei 8.213/1991. Os dependentes estão divididos em três classes (art. 16), e a existência de dependente de uma classe exclui os das seguintes.
""", [
 "Seguridade social: saúde, previdência e assistência (CF, art. 194).",
 "RGPS: contributivo e de filiação obrigatória (CF, art. 201).",
 "Segurados obrigatórios: Lei 8.213/1991, art. 11; facultativo: art. 13.",
 "Período de graça: art. 15.",
 "Dependentes em três classes: art. 16.",
], [
 "Dependência econômica de cônjuge, companheiro e filhos é presumida; das demais classes, deve ser provada (art. 16, § 4º).",
 "Segurado especial contribui sobre a comercialização da produção.",
 "Servidor efetivo vinculado a RPPS não pode se filiar ao RGPS como facultativo (CF, art. 201, § 5º).",
], ["CF:194","CF:195","CF:201","LBPS:1","LBPS:11","LBPS:13","LBPS:15","LBPS:16"]),

T("Benefícios Previdenciários", """
O RGPS oferece benefícios aos segurados e aos dependentes. Aos segurados: aposentadorias, auxílio por incapacidade temporária (antigo auxílio-doença), auxílio-acidente, salário-maternidade e salário-família. Aos dependentes: pensão por morte e auxílio-reclusão. O serviço social e a reabilitação profissional atendem a ambos.

Muitos benefícios exigem carência, isto é, um número mínimo de contribuições mensais: 12 para o auxílio por incapacidade temporária e a aposentadoria por incapacidade permanente, salvo acidente e doenças graves listadas; 10 para o salário-maternidade de contribuinte individual, segurado especial e facultativo; e 24 para o auxílio-reclusão. A pensão por morte não exige carência, mas sua duração para o cônjuge varia conforme a idade do beneficiário e o tempo de casamento ou união (art. 77, § 2º).

O auxílio-acidente tem natureza indenizatória, é pago quando sequelas reduzem a capacidade para o trabalho habitual e não é cumulável com aposentadoria. A Reforma da Previdência (EC 103/2019) alterou o cálculo de vários benefícios, inclusive o da pensão por morte, que passou a observar cotas por dependente.
""", [
 "Rol de benefícios: Lei 8.213/1991, art. 18.",
 "Carência: arts. 24 a 26.",
 "Pensão por morte: arts. 74 a 77 (duração variável para o cônjuge).",
 "Auxílio-acidente: art. 86 (indenizatório).",
 "Salário-maternidade: art. 71.",
], [
 "A perda da qualidade de segurado não impede a pensão se o falecido já tinha direito a aposentadoria (art. 102, § 2º).",
 "Auxílio-reclusão só para segurado de baixa renda, em regime fechado (art. 80).",
 "Doenças graves listadas em ato ministerial dispensam carência (art. 26, II, e art. 151).",
], ["LBPS:18","LBPS:24","LBPS:25","LBPS:26","LBPS:42","LBPS:59","LBPS:71","LBPS:74","LBPS:77","LBPS:80","LBPS:86","LBPS:102"]),

T("Custeio", """
A seguridade social é financiada por toda a sociedade, de forma direta e indireta, mediante recursos dos orçamentos públicos e de contribuições sociais (CF, art. 195). As contribuições incidem sobre o empregador e a empresa (folha de salários, receita ou faturamento e lucro), sobre o trabalhador e demais segurados, sobre a receita de concursos de prognósticos e sobre o importador.

A Lei 8.212/1991 disciplina o custeio. A empresa contribui com 20% sobre a remuneração paga aos empregados e contribuintes individuais, mais a contribuição para o financiamento dos benefícios decorrentes de riscos ambientais do trabalho (RAT/SAT). O segurado empregado contribui com alíquotas progressivas, após a EC 103/2019, sobre o salário de contribuição, limitado ao teto do RGPS.

As contribuições sociais sujeitam-se à anterioridade nonagesimal, mas não à anterioridade de exercício (art. 195, § 6º). Nova fonte de custeio exige lei complementar (art. 195, § 4º), e nenhum benefício pode ser criado, majorado ou estendido sem a correspondente fonte de custeio total (art. 195, § 5º, princípio da preexistência do custeio).
""", [
 "Financiamento por toda a sociedade (CF, art. 195).",
 "Anterioridade nonagesimal das contribuições sociais (art. 195, § 6º).",
 "Preexistência do custeio (art. 195, § 5º).",
 "Contribuição da empresa: 20% sobre a folha (Lei 8.212/1991, art. 22).",
 "Alíquotas progressivas do empregado após a EC 103/2019.",
], [
 "Entidades beneficentes de assistência social são imunes às contribuições para a seguridade (art. 195, § 7º).",
 "A contribuição do empregador doméstico tem regras próprias (LC 150/2015).",
 "Incide contribuição previdenciária patronal sobre o terço constitucional de férias (STF, Tema 985).",
], ["CF:195","L8212:12","L8212:20","L8212:21","L8212:22","L8212:28"], ["STF-RG-985"]),

T("Aposentadorias", """
A Reforma da Previdência (EC 103/2019) unificou a lógica das aposentadorias do RGPS em torno da idade mínima. A aposentadoria programada exige 65 anos de idade para homens e 62 para mulheres, com tempo mínimo de contribuição de 20 anos para homens que ingressaram após a reforma e 15 anos para mulheres. Deixou de existir, para os novos segurados, a aposentadoria por tempo de contribuição sem idade mínima.

Para quem já era filiado em 13/11/2019, a EC 103/2019 criou regras de transição: pontos (soma de idade e tempo de contribuição, crescente a cada ano), idade mínima progressiva com tempo de contribuição, pedágio de 50% (para quem estava a menos de 2 anos de se aposentar) e pedágio de 100% com idade mínima. O direito adquirido de quem preencheu os requisitos antes da reforma está preservado.

Há também a aposentadoria por incapacidade permanente (antiga aposentadoria por invalidez), a aposentadoria especial (atividades com exposição a agentes nocivos, com idade mínima após a reforma), a aposentadoria do trabalhador rural (60 anos homem, 55 mulher) e a da pessoa com deficiência (LC 142/2013). O cálculo passou a considerar 100% dos salários de contribuição, com 60% da média mais 2% por ano acima de 20 anos (homem) ou 15 anos (mulher).
""", [
 "Aposentadoria programada: 65 (H) e 62 (M) anos (CF, art. 201, § 7º, I, após a EC 103/2019).",
 "Regras de transição: pontos, idade progressiva, pedágio de 50% e de 100%.",
 "Cálculo: 60% da média + 2% por ano que exceder 20 (H) ou 15 (M) anos.",
 "Aposentadoria rural: 60 (H) e 55 (M) anos.",
 "Aposentadoria da pessoa com deficiência: LC 142/2013.",
], [
 "A desaposentação não tem previsão legal e foi rejeitada pelo STF (Tema 503).",
 "A revisão da vida toda foi afastada pelo STF ao validar as regras de transição da Lei 9.876/1999 (2024).",
 "Professor da educação básica tem redução de 5 anos na idade mínima.",
], ["CF:201","LBPS:42","LBPS:48","LBPS:57","LC142:1","LC142:3"], ["STF-RG-503"]),
],

"infancia": [
T("Princípio da Proteção Integral", """
O Estatuto da Criança e do Adolescente (Lei 8.069/1990) rompeu com a antiga doutrina da situação irregular e adotou a doutrina da proteção integral: crianças e adolescentes são sujeitos de direitos, em condição peculiar de pessoa em desenvolvimento, e gozam de todos os direitos fundamentais inerentes à pessoa humana, além de proteção especial.

A Constituição atribui à família, à sociedade e ao Estado o dever de assegurar, com absoluta prioridade, os direitos da criança e do adolescente (CF, art. 227; ECA, art. 4º). A prioridade absoluta compreende primazia de proteção e socorro, precedência no atendimento nos serviços públicos, preferência na formulação de políticas sociais e destinação privilegiada de recursos.

Para o ECA, criança é a pessoa até 12 anos incompletos e adolescente a de 12 a 18 anos (art. 2º), com aplicação excepcional até os 21 anos. A interpretação do Estatuto deve observar os fins sociais a que se dirige e o princípio do melhor interesse da criança e do adolescente (art. 6º).
""", [
 "Doutrina da proteção integral (ECA, arts. 1º e 3º).",
 "Prioridade absoluta (CF, art. 227; ECA, art. 4º).",
 "Criança: até 12 anos incompletos; adolescente: 12 a 18 anos (art. 2º).",
 "Interpretação pelos fins sociais e condição peculiar de pessoa em desenvolvimento (art. 6º).",
 "Direito à convivência familiar e comunitária (art. 19).",
], [
 "Aplicação do ECA a maiores de 18 e menores de 21 é excepcional (art. 2º, parágrafo único).",
 "Prioridade absoluta inclui preferência na destinação de recursos públicos (art. 4º, parágrafo único, d).",
 "Acolhimento institucional é medida excepcional e provisória (art. 101, § 1º).",
], ["ECA:1","ECA:2","ECA:3","ECA:4","ECA:5","ECA:6","ECA:19","CF:227"]),

T("Medidas Protetivas", """
As medidas de proteção são aplicáveis sempre que os direitos reconhecidos no ECA forem ameaçados ou violados por ação ou omissão da sociedade ou do Estado, por falta, omissão ou abuso dos pais ou responsável, ou em razão da conduta da própria criança ou adolescente (art. 98). Podem ser aplicadas isolada ou cumulativamente e substituídas a qualquer tempo.

O rol do art. 101 inclui encaminhamento aos pais mediante termo de responsabilidade, orientação e acompanhamento temporários, matrícula e frequência escolar obrigatórias, inclusão em programas de auxílio à família, tratamento médico ou psicológico, acolhimento institucional, inclusão em programa de acolhimento familiar e colocação em família substituta. A aplicação deve priorizar o fortalecimento dos vínculos familiares.

O Conselho Tutelar, órgão permanente e autônomo, não jurisdicional, aplica as medidas de proteção dos incisos I a VII do art. 101, salvo o acolhimento e a família substituta, que dependem de autoridade judiciária. Seus membros são escolhidos pela comunidade local, para mandato de 4 anos. À criança que pratica ato infracional aplicam-se somente medidas de proteção (art. 105).
""", [
 "Hipóteses de aplicação: art. 98.",
 "Rol de medidas de proteção: art. 101.",
 "Criança autora de ato infracional recebe apenas medidas de proteção (art. 105).",
 "Conselho Tutelar: art. 131 e seguintes.",
 "Colocação em família substituta: guarda, tutela ou adoção (art. 28).",
], [
 "Afastamento da criança do convívio familiar é de competência judicial (art. 101, § 2º).",
 "Falta de recursos materiais não autoriza a perda ou suspensão do poder familiar (art. 23).",
 "Adoção é medida excepcional e irrevogável (art. 39, § 1º).",
], ["ECA:23","ECA:28","ECA:39","ECA:98","ECA:100","ECA:101","ECA:105","ECA:131","ECA:136"]),

T("Ato Infracional", """
Considera-se ato infracional a conduta descrita como crime ou contravenção penal (ECA, art. 103). Os menores de 18 anos são penalmente inimputáveis (CF, art. 228), mas o adolescente que pratica ato infracional responde perante a Justiça da Infância e da Juventude, sujeito a medidas socioeducativas; à criança aplicam-se apenas medidas de proteção.

Ao adolescente são asseguradas garantias processuais: pleno conhecimento da atribuição de ato infracional, igualdade na relação processual, defesa técnica por advogado, assistência judiciária gratuita, direito de ser ouvido pessoalmente pela autoridade e de solicitar a presença dos pais (art. 111). Nenhum adolescente será privado de sua liberdade senão em flagrante ou por ordem escrita e fundamentada da autoridade judiciária (art. 106).

O procedimento envolve a apresentação ao Ministério Público, que pode arquivar, conceder remissão ou representar à autoridade judiciária para aplicação de medida socioeducativa (art. 180). A internação provisória, antes da sentença, tem prazo máximo improrrogável de 45 dias (art. 108). A remissão pode ser concedida como forma de exclusão, suspensão ou extinção do processo.
""", [
 "Conceito de ato infracional (art. 103).",
 "Inimputabilidade penal do menor de 18 (CF, art. 228; ECA, art. 104).",
 "Garantias processuais (art. 111).",
 "Internação provisória: até 45 dias (art. 108).",
 "Atuação do MP: arquivamento, remissão ou representação (art. 180).",
], [
 "A idade considerada é a da data do fato (art. 104, parágrafo único).",
 "Aplicar medida socioeducativa é competência exclusiva do juiz (Súmula 108 do STJ); a remissão concedida pelo MP depende de homologação judicial (art. 181).",
 "É nula a desistência de outras provas em razão da confissão do adolescente (Súmula 342 do STJ).",
], ["ECA:103","ECA:104","ECA:106","ECA:108","ECA:111","ECA:126","ECA:127","ECA:180","ECA:181","CF:228"], ["STJ-SUM-108","STJ-SUM-342"]),

T("Medidas Socioeducativas", """
Verificada a prática de ato infracional, a autoridade judiciária pode aplicar ao adolescente as medidas socioeducativas do art. 112: advertência, obrigação de reparar o dano, prestação de serviços à comunidade (até 6 meses), liberdade assistida (mínimo de 6 meses), inserção em regime de semiliberdade e internação, além das medidas de proteção do art. 101, I a VI. A escolha leva em conta a capacidade do adolescente de cumpri-la, as circunstâncias e a gravidade da infração.

A internação é medida privativa de liberdade sujeita aos princípios da brevidade, excepcionalidade e respeito à condição peculiar de pessoa em desenvolvimento (art. 121). Não comporta prazo determinado, deve ser reavaliada no máximo a cada 6 meses e não pode exceder 3 anos; a liberação é compulsória aos 21 anos. Só cabe nas hipóteses taxativas do art. 122: ato com grave ameaça ou violência à pessoa, reiteração em infrações graves ou descumprimento reiterado e injustificável de medida anterior (internação-sanção, até 3 meses).

A execução das medidas é disciplinada pela Lei do SINASE (Lei 12.594/2012), que prevê o plano individual de atendimento (PIA) e as reavaliações periódicas.
""", [
 "Rol de medidas socioeducativas: art. 112.",
 "Internação: brevidade, excepcionalidade e condição peculiar (art. 121).",
 "Prazo máximo de 3 anos, reavaliação semestral, liberação aos 21 (art. 121, §§ 2º a 5º).",
 "Hipóteses taxativas de internação: art. 122.",
 "Execução: Lei do SINASE (Lei 12.594/2012).",
], [
 "Ato infracional análogo ao tráfico de drogas, por si só, não conduz obrigatoriamente à internação (Súmula 492 do STJ).",
 "A internação-sanção por descumprimento de medida anterior tem prazo máximo de 3 meses (art. 122, § 1º).",
 "A gravidade abstrata do ato não justifica a internação sem as hipóteses do art. 122.",
], ["ECA:112","ECA:115","ECA:117","ECA:118","ECA:120","ECA:121","ECA:122"], ["STJ-SUM-492","STJ-SUM-265"]),
],
}
