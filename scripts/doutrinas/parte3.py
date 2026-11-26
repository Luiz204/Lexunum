# Conteúdo autoral de estudo — Lex Unum. Empresarial, Ambiental, Consumidor, Internacional.
from parte1 import T

DADOS = {
"empresarial": [
T("Empresário e Sociedade Empresária", """
O Código Civil adotou a teoria da empresa: empresário é quem exerce profissionalmente atividade econômica organizada para a produção ou a circulação de bens ou de serviços (art. 966). Ficam fora do conceito, em regra, os profissionais intelectuais (natureza científica, literária ou artística), salvo se o exercício da profissão constituir elemento de empresa.

O empresário individual responde com todo o seu patrimônio pelas obrigações da atividade. Para limitar a responsabilidade, pode-se constituir uma sociedade limitada unipessoal (art. 1.052, § 1º), que substituiu a antiga EIRELI. A inscrição na Junta Comercial é obrigatória antes do início das atividades (art. 967), mas tem natureza declaratória: o empresário irregular continua sendo empresário, embora sofra restrições (não pode pedir recuperação judicial, por exemplo).

O estabelecimento empresarial é o complexo de bens organizado para o exercício da empresa (art. 1.142). Sua alienação (trespasse) exige anuência dos credores se não restarem bens suficientes para pagá-los, e o adquirente responde pelos débitos anteriores regularmente contabilizados (art. 1.146).
""", [
 "Conceito de empresário: art. 966.",
 "Inscrição obrigatória antes do início das atividades (art. 967), com natureza declaratória.",
 "Sociedade limitada unipessoal (art. 1.052, § 1º).",
 "Estabelecimento: art. 1.142; trespasse: arts. 1.144 a 1.149.",
 "Desconsideração da personalidade jurídica exige desvio de finalidade ou confusão patrimonial (art. 50).",
], [
 "Profissional intelectual só é empresário se a profissão for elemento de empresa (art. 966, parágrafo único).",
 "Produtor rural tem inscrição facultativa (art. 971).",
 "Cláusula de não concorrência implícita no trespasse: 5 anos (art. 1.147).",
], ["CC:50","CC:966","CC:967","CC:971","CC:974","CC:1052","CC:1142","CC:1144","CC:1145","CC:1146","CC:1147"]),

T("Tipos Societários", """
As sociedades dividem-se em não personificadas (em comum e em conta de participação) e personificadas. Entre as personificadas, há a sociedade simples (atividade não empresarial) e as empresárias: em nome coletivo, em comandita simples, em comandita por ações, limitada e anônima. A cooperativa é sempre simples, e a sociedade por ações é sempre empresária (art. 982, parágrafo único).

Na sociedade limitada, a responsabilidade de cada sócio é restrita ao valor de suas quotas, mas todos respondem solidariamente pela integralização do capital social (art. 1.052). Ela é administrada por uma ou mais pessoas designadas no contrato ou em ato separado, e as deliberações seguem os quóruns do art. 1.076. A exclusão de sócio minoritário por justa causa é possível se prevista no contrato (art. 1.085).

A sociedade anônima (Lei 6.404/1976) tem o capital dividido em ações, e cada acionista responde apenas pelo preço de emissão das ações subscritas ou adquiridas. Pode ser aberta (valores mobiliários negociados no mercado) ou fechada. Seus órgãos são a assembleia geral, o conselho de administração (obrigatório nas abertas), a diretoria e o conselho fiscal.
""", [
 "Sociedade empresária × simples: art. 982.",
 "Limitada: responsabilidade restrita às quotas, solidariedade na integralização (art. 1.052).",
 "Quóruns da limitada: art. 1.076.",
 "Exclusão extrajudicial de minoritário: art. 1.085.",
 "S.A.: responsabilidade limitada ao preço de emissão das ações (Lei 6.404/1976, art. 1º).",
], [
 "Na sociedade em comum, os sócios respondem solidária e ilimitadamente (art. 990).",
 "Cooperativa é sempre sociedade simples, independentemente do objeto.",
 "Conselho de administração é obrigatório na S.A. aberta e na de capital autorizado (LSA, art. 138, § 2º).",
], ["CC:981","CC:982","CC:983","CC:986","CC:990","CC:991","CC:1052","CC:1053","CC:1076","CC:1085","LSA:1","LSA:4","LSA:138"]),

T("Títulos de Crédito", """
Título de crédito é o documento necessário ao exercício do direito literal e autônomo nele contido (art. 887 do CC, na clássica definição de Vivante). Daí os três princípios cambiários: cartularidade (o direito se materializa no documento), literalidade (vale o que está escrito) e autonomia (as obrigações cambiais são independentes entre si), da qual decorrem a abstração e a inoponibilidade das exceções pessoais ao terceiro de boa-fé.

Os principais títulos são a letra de câmbio e a nota promissória (Decreto 2.044/1908 e Lei Uniforme de Genebra), o cheque (Lei 7.357/1985) e a duplicata (Lei 5.474/1968). A circulação se faz por endosso (transfere o título e, em regra, torna o endossante coobrigado), e a garantia pessoal, pelo aval, que é autônomo e dispensa outorga conjugal nos títulos regidos por lei especial.

O protesto prova a inadimplência e é necessário para garantir o direito de regresso contra endossantes e seus avalistas, mas dispensável contra o devedor principal. O cheque é ordem de pagamento à vista, apresentável em 30 dias (mesma praça) ou 60 dias (praças diferentes), e a execução prescreve em 6 meses após o fim do prazo de apresentação.
""", [
 "Princípios: cartularidade, literalidade e autonomia.",
 "Aval é garantia autônoma; fiança é acessória.",
 "Cheque: apresentação em 30/60 dias e prescrição em 6 meses (Lei 7.357/1985, arts. 33 e 59).",
 "Duplicata é título causal, vinculado a compra e venda ou prestação de serviços.",
 "Protesto: necessário para o regresso contra coobrigados.",
], [
 "Cheque pré-datado apresentado antes da data gera dano moral (Súmula 370 do STJ).",
 "Ação monitória com base em cheque prescrito prescreve em 5 anos do dia seguinte à data de emissão (Súmula 503 do STJ).",
 "Endosso posterior ao protesto produz efeitos de cessão civil.",
], ["CC:887","CC:897","CC:898","CC:910","L7357:1","L7357:32","L7357:33","L7357:59","L5474:1","L5474:15","D2044:1"], ["STJ-SUM-370","STJ-SUM-503","STJ-SUM-299"]),

T("Falência", """
A falência (Lei 11.101/2005) é a execução concursal do devedor empresário insolvente: afasta o devedor de suas atividades para preservar e otimizar a utilização produtiva dos bens e pagar os credores segundo a ordem legal. Pode ser requerida pelo credor com base em impontualidade injustificada (título protestado acima de 40 salários mínimos), execução frustrada ou atos de falência (art. 94), ou pelo próprio devedor (autofalência).

A sentença que decreta a falência gera vencimento antecipado das dívidas, suspensão das execuções contra o falido, arrecadação dos bens e nomeação do administrador judicial. Os bens são realizados (vendidos) e o produto é distribuído na ordem do art. 83, depois dos créditos extraconcursais do art. 84.

A ordem do art. 83, após a Lei 14.112/2020, é: créditos trabalhistas até 150 salários mínimos por credor e de acidente de trabalho; créditos com garantia real até o valor do bem; créditos tributários; quirografários; multas; subordinados; e juros vencidos após a decretação. Os sócios de responsabilidade ilimitada também são atingidos pela falência.
""", [
 "Hipóteses de decretação: art. 94.",
 "Defesa do devedor: contestação em 10 dias, com possibilidade de depósito elisivo (arts. 95 e 98).",
 "Créditos extraconcursais (art. 84) são pagos antes dos concursais (art. 83).",
 "Ordem de classificação: art. 83.",
 "Ineficácia de atos praticados no termo legal (art. 129) e ação revocatória (art. 130).",
], [
 "Empresas públicas, sociedades de economia mista, instituições financeiras e outras estão excluídas (art. 2º).",
 "Créditos trabalhistas acima de 150 salários mínimos viram quirografários.",
 "Na falência, o crédito tributário não prefere aos trabalhistas e aos com garantia real (CTN, art. 186, parágrafo único).",
], ["LREF:1","LREF:2","LREF:75","LREF:83","LREF:84","LREF:94","LREF:95","LREF:98","LREF:99","LREF:129","LREF:130","CTN:186"]),

T("Recuperação Judicial", """
A recuperação judicial tem por objetivo viabilizar a superação da crise econômico-financeira do devedor, permitindo a manutenção da fonte produtora, do emprego dos trabalhadores e dos interesses dos credores, promovendo a preservação da empresa e sua função social (art. 47). Pode ser requerida pelo devedor que exerça regularmente suas atividades há mais de 2 anos e preencha os requisitos do art. 48.

Deferido o processamento, suspendem-se por 180 dias (stay period, prorrogável uma vez) as execuções contra o devedor. O devedor apresenta plano em 60 dias, e os credores podem objetar; havendo objeção, o plano é votado em assembleia geral de credores por classes (trabalhistas, garantia real, quirografários, ME/EPP). O juiz pode conceder a recuperação mesmo sem aprovação integral, pelo cram down, preenchidos os requisitos do art. 58, § 1º.

Nem todos os créditos se sujeitam: ficam de fora, por exemplo, os do proprietário fiduciário e os de arrendamento mercantil (art. 49, § 3º), além dos tributários, que exigem regularidade fiscal e podem ser objeto de transação ou parcelamento. Existe ainda a recuperação extrajudicial, negociada diretamente com os credores e homologada pelo juiz.
""", [
 "Finalidade: preservação da empresa (art. 47).",
 "Requisitos: mais de 2 anos de atividade regular e demais condições do art. 48.",
 "Stay period de 180 dias (art. 6º, § 4º).",
 "Plano em 60 dias, sob pena de falência (art. 53).",
 "Cram down: art. 58, § 1º.",
 "Créditos não sujeitos: art. 49, § 3º.",
], [
 "Descumprimento de obrigação do plano nos 2 anos seguintes leva à convolação em falência (art. 61).",
 "O produtor rural pode pedir recuperação comprovando 2 anos de atividade, mesmo com registro recente (STJ, Tema 1.145).",
 "A recuperação judicial não suspende execuções contra coobrigados, fiadores e avalistas (Súmula 581 do STJ).",
], ["LREF:6","LREF:47","LREF:48","LREF:49","LREF:51","LREF:53","LREF:56","LREF:58","LREF:61","LREF:161"], ["STJ-SUM-581","STJ-SUM-480"]),
],

"ambiental": [
T("Princípios Ambientais", """
O direito ao meio ambiente ecologicamente equilibrado é bem de uso comum do povo e essencial à sadia qualidade de vida, impondo-se ao Poder Público e à coletividade o dever de defendê-lo e preservá-lo para as presentes e futuras gerações (CF, art. 225). É direito fundamental de terceira dimensão, marcado pela solidariedade intergeracional.

Os princípios mais cobrados são: prevenção (diante de riscos conhecidos, adotam-se medidas para evitar o dano); precaução (diante de incerteza científica, a dúvida favorece o meio ambiente — in dubio pro natura); poluidor-pagador (o poluidor internaliza os custos da degradação); usuário-pagador; desenvolvimento sustentável; participação e informação ambiental; e vedação do retrocesso ecológico.

A Política Nacional do Meio Ambiente (Lei 6.938/1981) organiza o SISNAMA, define poluidor e degradação e instituiu os instrumentos de gestão, como o licenciamento, a avaliação de impacto, o zoneamento e as unidades de conservação. A competência material para proteger o meio ambiente é comum a todos os entes (CF, art. 23, VI e VII), com cooperação disciplinada pela LC 140/2011.
""", [
 "Direito fundamental ao meio ambiente equilibrado (CF, art. 225).",
 "Prevenção (risco certo) × precaução (incerteza científica).",
 "Poluidor-pagador e usuário-pagador (Lei 6.938/1981, art. 4º, VII).",
 "Conceitos de poluidor e degradação: Lei 6.938/1981, art. 3º.",
 "Competência material comum (CF, art. 23, VI e VII).",
], [
 "Princípio da precaução permite a inversão do ônus da prova em ações de degradação ambiental (Súmula 618 do STJ).",
 "Não se admite a aplicação da teoria do fato consumado em matéria ambiental (Súmula 613 do STJ).",
 "Obrigações ambientais são propter rem: o adquirente responde pela recomposição (Súmula 623 do STJ).",
], ["CF:23","CF:225","L6938:2","L6938:3","L6938:4","L6938:9"], ["STJ-SUM-618","STJ-SUM-613","STJ-SUM-623"]),

T("Responsabilidade Ambiental Tríplice", """
A Constituição estabelece que as condutas lesivas ao meio ambiente sujeitam os infratores, pessoas físicas ou jurídicas, a sanções penais e administrativas, independentemente da obrigação de reparar os danos (art. 225, § 3º). São três esferas independentes, que podem incidir cumulativamente sobre o mesmo fato.

A responsabilidade civil é objetiva (Lei 6.938/1981, art. 14, § 1º) e, segundo o STJ, regida pela teoria do risco integral: não admite excludentes como caso fortuito, força maior ou fato de terceiro. A pretensão de reparação civil do dano ambiental é imprescritível (STF, Tema 999), e o poluidor indireto também responde solidariamente.

A responsabilidade administrativa, segundo a Primeira Seção do STJ, é subjetiva: exige dolo ou culpa do infrator e nexo entre sua conduta e o dano (EREsp 1.318.051). Já a omissão do Estado no dever de fiscalizar gera responsabilidade civil solidária, de execução subsidiária (Súmula 652 do STJ). A responsabilidade penal está na Lei 9.605/1998 e alcança a pessoa jurídica, independentemente da responsabilização simultânea da pessoa física (STF, RE 548.181).
""", [
 "Tríplice responsabilidade: civil, administrativa e penal (CF, art. 225, § 3º).",
 "Responsabilidade civil objetiva (Lei 6.938/1981, art. 14, § 1º) e por risco integral (STJ).",
 "Reparação civil do dano ambiental é imprescritível (STF, Tema 999).",
 "Pessoa jurídica responde penalmente (Lei 9.605/1998, art. 3º).",
 "Desconsideração da pessoa jurídica sempre que for obstáculo ao ressarcimento (Lei 9.605/1998, art. 4º).",
], [
 "Na esfera penal, não se exige a dupla imputação: a pessoa jurídica pode ser processada sozinha.",
 "Risco integral afasta o fato de terceiro como excludente da reparação civil.",
 "Cumulação de obrigação de fazer (recuperar) com indenização é possível (Súmula 629 do STJ).",
], ["CF:225","L6938:14","L9605:2","L9605:3","L9605:4","L9605:70","L9605:72"], ["STF-RG-999","STJ-SUM-629","STJ-SUM-652"]),

T("Licenciamento Ambiental", """
O licenciamento ambiental é o procedimento administrativo pelo qual o órgão competente autoriza a localização, instalação, ampliação e operação de empreendimentos e atividades que utilizem recursos ambientais ou sejam efetiva ou potencialmente poluidores (LC 140/2011, art. 2º, I). É um dos instrumentos da Política Nacional do Meio Ambiente.

Em regra, ocorre em três etapas: licença prévia (fase de planejamento, aprova localização e concepção), licença de instalação (autoriza a implantação) e licença de operação (autoriza o funcionamento). Para obras ou atividades potencialmente causadoras de significativa degradação, a Constituição exige estudo prévio de impacto ambiental (EIA), a que se dará publicidade por meio do RIMA (CF, art. 225, § 1º, IV).

A LC 140/2011 define a competência para licenciar pelo critério da abrangência do impacto e da localização: a União licencia, por exemplo, empreendimentos em terras indígenas, no mar territorial ou em dois ou mais Estados; os Estados têm competência residual; e os Municípios licenciam atividades de impacto local. O licenciamento é feito por um único ente federativo, sem prejuízo da fiscalização supletiva dos demais.
""", [
 "Conceito de licenciamento: LC 140/2011, art. 2º, I.",
 "Licenças prévia, de instalação e de operação.",
 "EIA/RIMA para significativa degradação (CF, art. 225, § 1º, IV).",
 "Licenciamento por um único ente (LC 140/2011, art. 13).",
 "Instrumentos da PNMA, incluindo o licenciamento (Lei 6.938/1981, art. 9º, IV).",
], [
 "Licença ambiental não é ato definitivo: pode ser revista por mudança de condições ou descumprimento.",
 "Constituição estadual não pode dispensar EIA para atividades de significativa degradação (jurisprudência do STF).",
 "Fiscalização é competência comum, mas prevalece o auto de infração do ente licenciador (LC 140/2011, art. 17, § 3º).",
], ["CF:225","L6938:9","L6938:10"]),
],

"consumidor": [
T("Relação de Consumo", """
O Código de Defesa do Consumidor é norma de ordem pública e interesse social (art. 1º) que concretiza o mandamento constitucional de defesa do consumidor (CF, arts. 5º, XXXII, e 170, V). Aplica-se sempre que houver relação de consumo, composta por consumidor, fornecedor e produto ou serviço.

Consumidor é quem adquire ou utiliza produto ou serviço como destinatário final (art. 2º). O STJ adota a teoria finalista mitigada (ou aprofundada): em regra, destinatário final é quem retira o bem do mercado sem reempregá-lo na atividade produtiva, mas admite-se aplicar o CDC a profissionais e empresas que demonstrem vulnerabilidade técnica, jurídica, fática ou informacional. Há ainda consumidores por equiparação: a coletividade (art. 2º, parágrafo único), as vítimas de acidente de consumo (art. 17) e os expostos às práticas comerciais (art. 29).

Fornecedor é toda pessoa física ou jurídica, pública ou privada, que desenvolve atividade de produção, comercialização ou prestação de serviços no mercado, mediante remuneração (art. 3º). Estão sujeitos ao CDC, por exemplo, bancos, planos de saúde (exceto autogestão) e concessionárias de serviço público.
""", [
 "Conceito de consumidor: art. 2º (teoria finalista mitigada).",
 "Consumidores por equiparação: arts. 2º, parágrafo único, 17 e 29.",
 "Conceito de fornecedor, produto e serviço: art. 3º.",
 "CDC aplica-se às instituições financeiras (Súmula 297 do STJ).",
 "CDC não se aplica aos planos de saúde de autogestão (Súmula 608 do STJ).",
], [
 "Vulnerabilidade é presumida para o consumidor pessoa física; para a pessoa jurídica, deve ser demonstrada.",
 "Remuneração indireta (como estacionamento gratuito de shopping) também caracteriza o serviço.",
 "CDC não se aplica a contratos de locação regidos pela Lei 8.245/1991.",
], ["CDC:1","CDC:2","CDC:3","CDC:4","CDC:17","CDC:29","CF:5","CF:170"], ["STJ-SUM-297","STJ-SUM-608","STJ-SUM-563"]),

T("Responsabilidade do Fornecedor", """
O CDC distingue responsabilidade pelo fato (acidente de consumo, que atinge a segurança do consumidor) e pelo vício (defeito que compromete a adequação ou o valor do produto ou serviço). Ambas são objetivas, salvo para os profissionais liberais, cuja responsabilidade pessoal por fato do serviço depende de culpa (art. 14, § 4º).

No fato do produto (art. 12), respondem fabricante, produtor, construtor e importador; o comerciante responde subsidiariamente, só nas hipóteses do art. 13. No fato do serviço (art. 14), responde o fornecedor. As excludentes são não ter colocado o produto no mercado, inexistência do defeito e culpa exclusiva do consumidor ou de terceiro. A pretensão prescreve em 5 anos (art. 27).

No vício do produto (art. 18), todos os fornecedores da cadeia respondem solidariamente. O fornecedor tem 30 dias para sanar o vício; não sanado, o consumidor escolhe entre substituição, restituição do valor ou abatimento do preço. Para reclamar de vícios aparentes, o prazo decadencial é de 30 dias (não duráveis) ou 90 dias (duráveis); nos vícios ocultos, conta-se da descoberta (art. 26).
""", [
 "Fato do produto (art. 12) e do serviço (art. 14): responsabilidade objetiva.",
 "Comerciante responde subsidiariamente pelo fato do produto (art. 13).",
 "Vício do produto: solidariedade de toda a cadeia (art. 18).",
 "Decadência para vícios: 30 dias (não duráveis) e 90 dias (duráveis) (art. 26).",
 "Prescrição da reparação por fato: 5 anos (art. 27).",
 "Profissionais liberais: responsabilidade subjetiva (art. 14, § 4º).",
], [
 "Fortuito interno não exclui a responsabilidade dos bancos por fraudes de terceiros (Súmula 479 do STJ).",
 "Vício (adequação) e fato (segurança) têm prazos diferentes: decadência × prescrição.",
 "Desconsideração da personalidade jurídica no CDC adota a teoria menor (art. 28, § 5º).",
], ["CDC:12","CDC:13","CDC:14","CDC:18","CDC:19","CDC:20","CDC:26","CDC:27","CDC:28"], ["STJ-SUM-479"]),

T("Práticas Abusivas", """
O CDC protege o consumidor desde antes da contratação. A oferta suficientemente precisa vincula o fornecedor (art. 30), que, se recusar cumpri-la, fica sujeito à execução específica, à aceitação de produto equivalente ou à rescisão com restituição (art. 35). A publicidade enganosa (que induz em erro) e a abusiva (discriminatória, que explora o medo, a superstição ou a deficiência de julgamento da criança) são proibidas (art. 37).

O art. 39 traz um rol exemplificativo de práticas abusivas: venda casada, recusa de atendimento, envio de produto sem solicitação (equiparado a amostra grátis), prevalecer-se da fraqueza ou ignorância do consumidor, exigir vantagem manifestamente excessiva, executar serviço sem orçamento e elevar preços sem justa causa. Na cobrança de dívidas, o consumidor não pode ser exposto a ridículo nem a constrangimento, e a cobrança indevida paga gera devolução em dobro, salvo engano justificável (art. 42).

Nos contratos, são nulas de pleno direito as cláusulas abusivas do art. 51, como as que exoneram a responsabilidade do fornecedor ou estabelecem obrigações iníquas. O consumidor tem direito de arrependimento de 7 dias nas compras fora do estabelecimento comercial (art. 49).
""", [
 "Oferta vincula o fornecedor (arts. 30 e 35).",
 "Publicidade enganosa e abusiva (art. 37); ônus da prova é de quem patrocina (art. 38).",
 "Práticas abusivas: rol exemplificativo do art. 39.",
 "Devolução em dobro do que foi pago indevidamente (art. 42, parágrafo único).",
 "Direito de arrependimento: 7 dias fora do estabelecimento (art. 49).",
 "Cláusulas abusivas são nulas (art. 51).",
], [
 "Devolução em dobro independe de má-fé, bastando conduta contrária à boa-fé objetiva (STJ, EAREsp 676.608).",
 "Produto enviado sem solicitação é amostra grátis (art. 39, parágrafo único).",
 "O juiz não pode reconhecer de ofício a abusividade de cláusulas em contratos bancários (Súmula 381 do STJ).",
], ["CDC:30","CDC:31","CDC:35","CDC:36","CDC:37","CDC:38","CDC:39","CDC:42","CDC:43","CDC:49","CDC:51"], ["STJ-SUM-381","STJ-SUM-359","STJ-SUM-385"]),

T("Direitos Básicos", """
O art. 6º do CDC lista os direitos básicos do consumidor: proteção da vida, saúde e segurança; educação para o consumo; informação adequada e clara sobre produtos e serviços, com especificação de quantidade, características, tributos e preço; proteção contra publicidade enganosa e abusiva e práticas abusivas; modificação de cláusulas desproporcionais e revisão por fatos supervenientes que as tornem excessivamente onerosas; prevenção e reparação de danos; acesso à justiça; e facilitação da defesa, inclusive com inversão do ônus da prova.

A revisão contratual no CDC adota a teoria da base objetiva do negócio: basta o fato superveniente que torne a prestação excessivamente onerosa, sem exigir imprevisibilidade, diferente do Código Civil. A inversão do ônus da prova é ope judicis: depende de decisão do juiz, quando verossímil a alegação ou hipossuficiente o consumidor (art. 6º, VIII).

A Lei 14.181/2021 incluiu a prevenção e o tratamento do superendividamento, com a preservação do mínimo existencial, a repactuação de dívidas e o crédito responsável. A tutela coletiva do consumidor (arts. 81 a 104) abrange interesses difusos, coletivos e individuais homogêneos.
""", [
 "Rol de direitos básicos: art. 6º.",
 "Revisão por fato superveniente sem exigência de imprevisibilidade (art. 6º, V).",
 "Inversão do ônus da prova ope judicis (art. 6º, VIII).",
 "Superendividamento: arts. 54-A a 54-G e 104-A.",
 "Tutela coletiva: interesses difusos, coletivos e individuais homogêneos (art. 81).",
], [
 "A inversão do ônus da prova é regra de instrução e deve ser decidida antes da sentença (STJ).",
 "Informação clara inclui o preço com tributos incidentes (art. 6º, III).",
 "Na ação civil pública consumerista, a sentença de procedência beneficia vítimas individuais (art. 103, § 3º).",
], ["CDC:4","CDC:6","CDC:54-A","CDC:81","CDC:101","CDC:103","CDC:104-A"]),
],

"internacional": [
T("Tratados Internacionais", """
Tratado é o acordo formal concluído entre sujeitos de Direito Internacional (Estados e organizações internacionais), regido pelo Direito Internacional e destinado a produzir efeitos jurídicos. A Convenção de Viena sobre o Direito dos Tratados (1969), promulgada no Brasil pelo Decreto 7.030/2009, é a principal fonte sobre o tema e consagra o pacta sunt servanda e a vedação de invocar o direito interno para descumprir tratado (art. 27).

No Brasil, a celebração segue um procedimento complexo: o Presidente da República celebra o tratado (CF, art. 84, VIII); o Congresso Nacional resolve definitivamente sobre os que acarretem encargos ou compromissos gravosos ao patrimônio nacional, por decreto legislativo (art. 49, I); o Presidente ratifica no plano internacional; e, por fim, o decreto presidencial promulga o tratado, dando-lhe executoriedade interna.

Quanto à hierarquia, tratados comuns ingressam com status de lei ordinária; tratados de direitos humanos aprovados pelo rito do art. 5º, § 3º, equivalem a emendas constitucionais; e os demais tratados de direitos humanos têm status supralegal, conforme o STF (RE 466.343 — prisão do depositário infiel).
""", [
 "Celebração pelo Presidente (CF, art. 84, VIII) e aprovação do Congresso (art. 49, I).",
 "Promulgação por decreto presidencial dá vigência interna.",
 "Tratados comuns: status de lei ordinária.",
 "Tratados de direitos humanos: supralegais ou equivalentes a emendas (art. 5º, § 3º).",
 "Convenção de Viena de 1969: pacta sunt servanda e vedação de invocar o direito interno (art. 27).",
], [
 "É ilícita a prisão civil do depositário infiel, qualquer que seja a modalidade do depósito (Súmula Vinculante 25).",
 "Reserva é declaração unilateral que exclui ou modifica efeitos de cláusulas do tratado.",
 "Tratados tributários: discute-se a prevalência sobre a lei interna posterior (CTN, art. 98).",
], ["CF:5","CF:49","CF:84","CTN:98"], ["SV-25"]),

T("Direitos Humanos", """
No Direito Internacional, a proteção dos direitos humanos se organiza em um sistema global (ONU) e em sistemas regionais (interamericano, europeu e africano), que coexistem e se complementam, prevalecendo a norma mais favorável à pessoa (princípio pro persona). Os direitos humanos são universais, indivisíveis, interdependentes e inter-relacionados.

O Brasil rege-se, nas relações internacionais, pela prevalência dos direitos humanos (CF, art. 4º, II) e propugna pela formação de um tribunal internacional dos direitos humanos (ADCT, art. 7º). Submete-se à jurisdição do Tribunal Penal Internacional, a cuja criação tenha manifestado adesão (CF, art. 5º, § 4º), que julga crimes de genocídio, contra a humanidade, de guerra e de agressão, de forma complementar às jurisdições nacionais.

O controle de convencionalidade é a verificação da compatibilidade das normas internas com os tratados de direitos humanos e pode ser exercido por qualquer juiz (difuso) ou pelo STF (concentrado, para tratados com status de emenda). A federalização de graves violações de direitos humanos permite deslocar a competência para a Justiça Federal, por incidente suscitado pelo Procurador-Geral da República ao STJ (CF, art. 109, § 5º).
""", [
 "Prevalência dos direitos humanos nas relações internacionais (CF, art. 4º, II).",
 "Submissão ao Tribunal Penal Internacional (CF, art. 5º, § 4º).",
 "Incidente de deslocamento de competência (CF, art. 109, V-A e § 5º).",
 "Controle de convencionalidade difuso e concentrado.",
 "Princípio pro persona: aplica-se a norma mais favorável.",
], [
 "O TPI tem jurisdição complementar: só atua se o Estado não puder ou não quiser julgar.",
 "O incidente de deslocamento de competência é suscitado pelo PGR perante o STJ.",
 "A entrega ao TPI não se confunde com a extradição vedada ao brasileiro nato.",
], ["CF:4","CF:5","CF:109","ADCT:7"]),

T("Direito Internacional Privado", """
O Direito Internacional Privado resolve conflitos de leis no espaço: indica qual ordenamento jurídico se aplica a uma relação com elemento estrangeiro (elemento de conexão). No Brasil, suas regras estão sobretudo na Lei de Introdução às Normas do Direito Brasileiro (LINDB, arts. 7º a 19), no CPC (competência internacional e cooperação) e em tratados.

Os principais elementos de conexão da LINDB são: lei do domicílio para começo e fim da personalidade, nome, capacidade e direitos de família (art. 7º); lei do lugar da situação dos bens (art. 8º); lei do lugar da constituição das obrigações (art. 9º); e lei do domicílio do de cujus para a sucessão, com a ressalva da lei mais favorável a cônjuge ou filhos brasileiros quanto a bens situados no Brasil (art. 10, § 1º). A aplicação da lei estrangeira encontra limite na ordem pública, na soberania nacional e nos bons costumes (art. 17).

Quanto à jurisdição, o CPC define competência concorrente (arts. 21 e 22) e exclusiva da autoridade brasileira (art. 23), como ações sobre imóveis situados no Brasil. Sentenças estrangeiras dependem de homologação pelo STJ para produzir efeitos no Brasil (CF, art. 105, I, i), salvo a sentença estrangeira de divórcio consensual puro, que pode ser averbada diretamente em cartório.
""", [
 "Lei do domicílio para estatuto pessoal (LINDB, art. 7º).",
 "Lex rei sitae para bens (LINDB, art. 8º).",
 "Sucessão: lei do domicílio do falecido, com proteção do cônjuge/filhos brasileiros (art. 10).",
 "Limite da ordem pública (LINDB, art. 17).",
 "Homologação de sentença estrangeira pelo STJ (CF, art. 105, I, i; CPC, art. 960).",
 "Competência exclusiva brasileira: CPC, art. 23.",
], [
 "A LINDB veda o reenvio: considera-se a lei estrangeira sem suas remissões a outra lei (art. 16).",
 "Divórcio consensual puro estrangeiro dispensa homologação do STJ (CPC, art. 961, § 5º).",
 "A existência de ação no estrangeiro não induz litispendência no Brasil (CPC, art. 24).",
], ["LINDB:7","LINDB:8","LINDB:9","LINDB:10","LINDB:12","LINDB:16","LINDB:17","CPC:21","CPC:22","CPC:23","CPC:24","CPC:960","CPC:961","CF:105"]),
],
}
