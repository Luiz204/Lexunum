# Conteúdo autoral de estudo — Lex Unum. Processo Civil, Processo Penal, Trabalho, Tributário.
from parte1 import T

DADOS = {
"processual-civil": [
T("Petição Inicial", """
A petição inicial é o ato que instaura o processo e delimita a demanda pelos seus três elementos: partes, causa de pedir e pedido. O art. 319 do CPC lista os requisitos: juízo, qualificação das partes, fatos e fundamentos jurídicos, pedido com suas especificações, valor da causa, provas e a opção pela audiência de conciliação ou mediação. Ela deve vir acompanhada dos documentos indispensáveis (art. 320).

Se a inicial tiver defeito sanável, o juiz deve determinar a emenda em 15 dias, indicando com precisão o que corrigir (art. 321); só depois pode indeferi-la. O indeferimento ocorre nos casos do art. 330 (inépcia, ilegitimidade manifesta, falta de interesse). Há ainda a improcedência liminar do pedido, sem citação do réu, quando o pedido contrariar precedentes qualificados ou se verificar desde logo a prescrição ou decadência (art. 332).

O pedido deve ser certo e determinado, admitindo-se pedido genérico nas hipóteses legais (art. 324, § 1º). O valor da causa segue os critérios do art. 292 e pode ser corrigido de ofício.
""", [
 "Requisitos: art. 319; documentos indispensáveis: art. 320.",
 "Emenda em 15 dias, com indicação precisa do vício (art. 321).",
 "Indeferimento da inicial: art. 330; cabe apelação com juízo de retratação em 5 dias (art. 331).",
 "Improcedência liminar: art. 332.",
 "Valor da causa: critérios do art. 292.",
], [
 "A falta de CPF/endereço não leva a indeferimento se for possível a citação (art. 319, §§ 1º a 3º).",
 "Inépcia inclui pedido indeterminado fora das hipóteses legais e pedidos incompatíveis (art. 330, § 1º).",
 "Improcedência liminar resolve o mérito, diferente do indeferimento da inicial.",
], ["CPC:292","CPC:319","CPC:320","CPC:321","CPC:324","CPC:330","CPC:331","CPC:332"]),

T("Resposta do Réu", """
No CPC/2015, a principal forma de resposta é a contestação, que concentra toda a matéria de defesa, inclusive a reconvenção, apresentada na mesma peça (art. 343). O prazo é de 15 dias úteis, contados, em regra, da audiência de conciliação ou mediação sem acordo, ou do protocolo do pedido de cancelamento da audiência (art. 335).

Antes do mérito, o réu deve alegar as preliminares do art. 337: inexistência ou nulidade da citação, incompetência absoluta e relativa, valor da causa, inépcia, perempção, litispendência, coisa julgada, conexão, incapacidade de parte, convenção de arbitragem, ausência de legitimidade ou interesse, falta de caução e indevida gratuidade. A incompetência relativa e a convenção de arbitragem não alegadas em contestação ficam preclusas.

Vigoram o princípio da eventualidade (toda a defesa de uma vez) e o ônus da impugnação especificada: fatos não impugnados presumem-se verdadeiros, com as exceções do art. 341. A revelia gera presunção relativa de veracidade, afastada nas hipóteses do art. 345.
""", [
 "Prazo da contestação: 15 dias úteis (art. 335).",
 "Preliminares: art. 337; incompetência relativa e arbitragem precluem se não alegadas (art. 337, §§ 5º e 6º).",
 "Impugnação especificada (art. 341).",
 "Reconvenção na própria contestação (art. 343).",
 "Revelia e suas exceções (arts. 344 e 345).",
], [
 "Fazenda Pública, MP e Defensoria têm prazo em dobro (arts. 180, 183 e 186).",
 "Litisconsortes com advogados diferentes, de escritórios distintos, têm prazo em dobro só em autos físicos (art. 229).",
 "Revelia não induz presunção se houver pluralidade de réus e algum contestar (art. 345, I).",
], ["CPC:335","CPC:336","CPC:337","CPC:341","CPC:343","CPC:344","CPC:345","CPC:229"]),

T("Provas", """
Prova é todo elemento que contribui para formar a convicção do juiz sobre os fatos. O CPC adota o livre convencimento motivado (persuasão racional): o juiz aprecia a prova constante dos autos, independentemente de quem a produziu, e indica na decisão as razões de seu convencimento (art. 371).

O ônus da prova é estático como regra (art. 373): ao autor, os fatos constitutivos; ao réu, os fatos impeditivos, modificativos ou extintivos. Admite-se a distribuição dinâmica, por decisão fundamentada, quando houver impossibilidade ou excessiva dificuldade de cumprir o encargo ou maior facilidade da parte contrária (art. 373, § 1º), sempre com oportunidade para a parte se desincumbir do ônus.

Os meios típicos de prova incluem ata notarial, depoimento pessoal, confissão, exibição de documento, prova documental, testemunhal, pericial e inspeção judicial. A produção antecipada de provas não exige mais urgência e pode servir para viabilizar autocomposição ou evitar o ajuizamento de ação (art. 381).
""", [
 "Livre convencimento motivado (art. 371).",
 "Ônus estático (art. 373, caput) e dinâmico (art. 373, § 1º).",
 "Não dependem de prova os fatos notórios, confessados, incontroversos e presumidos (art. 374).",
 "Produção antecipada de provas sem necessidade de urgência (art. 381).",
 "Testemunhas: até 10, no máximo 3 por fato (art. 357, § 6º).",
], [
 "A redistribuição do ônus não pode gerar prova diabólica para a outra parte (art. 373, § 2º).",
 "No CDC, a inversão é ope judicis, a critério do juiz (CDC, art. 6º, VIII).",
 "Confissão judicial faz prova contra o confitente, mas não prejudica litisconsortes (art. 391).",
], ["CPC:369","CPC:371","CPC:373","CPC:374","CPC:381","CPC:389","CPC:391","CPC:357","CDC:6"]),

T("Sentença e Coisa Julgada", """
Sentença é o pronunciamento pelo qual o juiz, com base nos arts. 485 ou 487, põe fim à fase cognitiva do procedimento comum ou extingue a execução (art. 203, § 1º). Sem resolução de mérito (art. 485), o processo termina por questões processuais e, em regra, a ação pode ser reproposta; com resolução de mérito (art. 487), há acolhimento ou rejeição do pedido, homologação de autocomposição ou reconhecimento de prescrição ou decadência.

A sentença deve ter relatório, fundamentos e dispositivo, e o art. 489, § 1º, lista hipóteses de decisão não fundamentada — como a que se limita a citar ato normativo ou a invocar precedente sem demonstrar a semelhança com o caso. O juiz também não pode decidir com base em fundamento sobre o qual as partes não puderam se manifestar (vedação à decisão surpresa, art. 10).

Coisa julgada material é a autoridade que torna imutável e indiscutível a decisão de mérito não mais sujeita a recurso (art. 502). O CPC/2015 estendeu, com requisitos, a coisa julgada à questão prejudicial decidida expressa e incidentalmente (art. 503, § 1º). A desconstituição se faz por ação rescisória, em 2 anos do trânsito em julgado da última decisão do processo.
""", [
 "Extinção sem mérito: art. 485; com mérito: art. 487.",
 "Elementos da sentença e fundamentação adequada: art. 489.",
 "Vedação à decisão surpresa (arts. 9º e 10).",
 "Coisa julgada material: art. 502; questão prejudicial: art. 503, § 1º.",
 "Ação rescisória: hipóteses do art. 966, prazo de 2 anos (art. 975).",
], [
 "Perempção, litispendência e coisa julgada impedem a repropositura (art. 486, § 1º).",
 "Remessa necessária não se aplica abaixo dos valores do art. 496, § 3º, nem contra precedentes qualificados (§ 4º).",
 "Os motivos e a verdade dos fatos não fazem coisa julgada (art. 504).",
], ["CPC:10","CPC:203","CPC:485","CPC:487","CPC:489","CPC:496","CPC:502","CPC:503","CPC:504","CPC:966","CPC:975"]),

T("Recursos", """
O CPC prevê como recursos a apelação, o agravo de instrumento, o agravo interno, os embargos de declaração, o recurso ordinário, o recurso especial, o recurso extraordinário, o agravo em recurso especial ou extraordinário e os embargos de divergência (art. 994). O prazo é de 15 dias úteis para todos, exceto os embargos de declaração, que têm 5 dias (art. 1.003, § 5º).

A apelação cabe contra a sentença e tem, em regra, efeito suspensivo (art. 1.012). As decisões interlocutórias não agraváveis não precluem e podem ser impugnadas como preliminar da apelação ou das contrarrazões (art. 1.009, § 1º). O agravo de instrumento cabe nas hipóteses do art. 1.015, cujo rol o STJ considerou de taxatividade mitigada: admite-se o agravo quando houver urgência decorrente da inutilidade do julgamento da questão no recurso de apelação (Tema 988).

Os recursos excepcionais (especial e extraordinário) exigem prequestionamento e não se prestam ao reexame de fatos e provas. O recurso extraordinário exige repercussão geral, e o recurso especial passou a exigir relevância da questão federal (EC 125/2022), ainda pendente de regulamentação.
""", [
 "Prazo de 15 dias úteis, exceto embargos de declaração (5 dias) (art. 1.003, § 5º).",
 "Apelação com efeito suspensivo em regra; exceções do art. 1.012, § 1º.",
 "Interlocutórias não agraváveis são impugnadas na apelação (art. 1.009, § 1º).",
 "Agravo de instrumento: rol do art. 1.015, de taxatividade mitigada (STJ, Tema 988).",
 "Embargos de declaração interrompem o prazo para outros recursos (art. 1.026).",
], [
 "Reexame de prova não cabe em recurso especial (Súmula 7 do STJ).",
 "Embargos de declaração manifestamente protelatórios geram multa de até 2% (art. 1.026, § 2º).",
 "Apelação contra improcedência liminar e indeferimento da inicial admite retratação.",
], ["CPC:994","CPC:1003","CPC:1009","CPC:1012","CPC:1015","CPC:1021","CPC:1022","CPC:1026","CPC:1029","CF:102","CF:105"], ["STJ-SUM-7","STJ-TR-988"]),

T("Execução", """
A tutela executiva satisfaz o direito já reconhecido em título executivo. Se o título é judicial (sentença, decisão homologatória etc.), a execução ocorre por cumprimento de sentença, na mesma relação processual; se é extrajudicial (cheque, nota promissória, contrato assinado por duas testemunhas etc.), por processo autônomo de execução.

No cumprimento de sentença de obrigação de pagar quantia, o devedor é intimado para pagar em 15 dias; não pagando, acrescem-se multa de 10% e honorários de 10% (art. 523). Depois desse prazo, corre outro de 15 dias para a impugnação, independentemente de penhora (art. 525). Na execução de título extrajudicial, o executado é citado para pagar em 3 dias (art. 829) e se defende por embargos à execução, em 15 dias, sem necessidade de garantir o juízo (art. 914).

A penhora segue a ordem preferencial do art. 835, com dinheiro em primeiro lugar. O art. 833 enumera bens impenhoráveis, como salários e poupança até 40 salários mínimos, com relativizações reconhecidas pela jurisprudência. Bem de família é protegido pela Lei 8.009/1990.
""", [
 "Títulos judiciais: art. 515; extrajudiciais: art. 784.",
 "Cumprimento de sentença: 15 dias para pagar, sob multa de 10% e honorários de 10% (art. 523).",
 "Impugnação ao cumprimento: art. 525.",
 "Execução de título extrajudicial: citação para pagar em 3 dias (art. 829); embargos em 15 dias (art. 914).",
 "Impenhorabilidades: art. 833; ordem de penhora: art. 835.",
], [
 "Embargos à execução não exigem garantia do juízo (art. 914), mas o efeito suspensivo sim (art. 919, § 1º).",
 "Imóvel de fiador em locação pode ser penhorado (Súmula 549 do STJ; STF, Tema 1.127).",
 "Bem de família vale também para pessoas solteiras, separadas e viúvas (Súmula 364 do STJ).",
], ["CPC:513","CPC:515","CPC:523","CPC:525","CPC:784","CPC:829","CPC:833","CPC:835","CPC:914","CPC:919","L8009:1","L8009:3"], ["STJ-SUM-364","STJ-SUM-549"]),

T("Tutelas Provisórias", """
A tutela provisória (art. 294) pode fundar-se em urgência ou em evidência. A de urgência divide-se em antecipada (satisfativa, entrega desde logo o bem da vida) e cautelar (conservativa, assegura o resultado útil), e exige probabilidade do direito e perigo de dano ou risco ao resultado útil do processo (art. 300). A antecipada não pode ser concedida quando houver perigo de irreversibilidade dos efeitos.

Ambas podem ser requeridas em caráter antecedente (antes do pedido principal) ou incidental. A tutela antecipada antecedente pode se estabilizar quando o réu não interpõe recurso contra a decisão que a concede: o processo é extinto e qualquer das partes pode, em 2 anos, propor ação para rever, reformar ou invalidar a tutela (art. 304). A decisão estabilizada não faz coisa julgada.

A tutela da evidência dispensa urgência e cabe nas hipóteses do art. 311, como abuso do direito de defesa ou tese firmada em casos repetitivos ou súmula vinculante com prova documental.
""", [
 "Urgência: probabilidade do direito + perigo de dano/risco ao resultado útil (art. 300).",
 "Vedação à antecipação irreversível (art. 300, § 3º).",
 "Estabilização da tutela antecipada antecedente (art. 304).",
 "Ação de revisão da tutela estabilizada em 2 anos (art. 304, § 5º).",
 "Tutela da evidência: art. 311.",
], [
 "Estabilização é exclusiva da tutela antecipada antecedente, não da cautelar.",
 "A tutela estabilizada não faz coisa julgada (art. 304, § 6º).",
 "Nas hipóteses dos incisos II e III do art. 311, a tutela da evidência pode ser liminar.",
], ["CPC:294","CPC:296","CPC:300","CPC:303","CPC:304","CPC:305","CPC:311"]),
],

"processual-penal": [
T("Inquérito Policial", """
O inquérito policial é procedimento administrativo, inquisitivo e preparatório, presidido pelo delegado de polícia, destinado a reunir elementos de autoria e materialidade para a propositura da ação penal. É dispensável — a denúncia pode basear-se em outras peças de informação — e sigiloso, sem que o sigilo alcance o defensor em relação às diligências já documentadas (Súmula Vinculante 14).

Pode ser instaurado de ofício, por requisição do juiz ou do MP, a requerimento do ofendido ou por auto de prisão em flagrante (art. 5º). Nos crimes de ação penal privada e pública condicionada, depende de requerimento ou representação. A autoridade policial não pode mandar arquivar o inquérito (art. 17).

Desde o Pacote Anticrime e a decisão do STF nas ADIs 6.298 e seguintes, o arquivamento é ordenado pelo Ministério Público, que comunica a vítima, o investigado e a autoridade policial e submete a decisão ao controle judicial, podendo a vítima pedir revisão à instância competente do próprio MP. Os prazos de conclusão são de 10 dias para preso e 30 para solto, em regra (art. 10).
""", [
 "Características: administrativo, inquisitivo, escrito, sigiloso, dispensável e indisponível para a autoridade policial.",
 "Formas de instauração: art. 5º.",
 "Delegado não arquiva inquérito (art. 17).",
 "Arquivamento pelo MP com controle judicial (art. 28, conforme ADI 6.298).",
 "Prazos: 10 dias (preso) e 30 dias (solto) (art. 10).",
], [
 "Vícios do inquérito não anulam a ação penal.",
 "Elementos do inquérito não podem, sozinhos, fundamentar condenação (art. 155).",
 "Defensor tem acesso amplo aos elementos já documentados (Súmula Vinculante 14).",
], ["CPP:4","CPP:5","CPP:10","CPP:14","CPP:17","CPP:18","CPP:28","CPP:155"], ["SV-14","STF-SUM-524"]),

T("Ação Penal", """
A ação penal pode ser pública (titularidade do Ministério Público, iniciada por denúncia) ou privada (titularidade do ofendido, iniciada por queixa). A pública é incondicionada ou condicionada à representação do ofendido ou à requisição do Ministro da Justiça. A privada pode ser exclusiva, personalíssima ou subsidiária da pública, esta cabível diante da inércia do MP.

A ação pública rege-se pelos princípios da obrigatoriedade (mitigada pela transação penal e pelo acordo de não persecução penal), indisponibilidade (o MP não pode desistir), oficialidade e divisibilidade. A privada, pelos princípios da oportunidade, disponibilidade e indivisibilidade: a renúncia em relação a um dos autores a todos se estende (art. 49).

O acordo de não persecução penal (art. 28-A) pode ser proposto quando o investigado confessa formal e circunstancialmente infração sem violência ou grave ameaça, com pena mínima inferior a 4 anos. A denúncia deve conter os requisitos do art. 41, e a rejeição liminar segue o art. 395.
""", [
 "Pública: incondicionada, condicionada à representação ou à requisição do Ministro da Justiça.",
 "Representação: prazo decadencial de 6 meses do conhecimento da autoria (art. 38).",
 "Retratação da representação até o oferecimento da denúncia (art. 25).",
 "ANPP: art. 28-A — sem violência ou grave ameaça, pena mínima inferior a 4 anos, confissão.",
 "Requisitos da denúncia: art. 41; rejeição: art. 395.",
], [
 "Ação privada subsidiária cabe só com inércia do MP, não com pedido de arquivamento (CF, art. 5º, LIX; CPP, art. 29).",
 "Na Lei Maria da Penha, a retratação da representação só vale em audiência perante o juiz (Lei 11.340/2006, art. 16).",
 "Lesão corporal no contexto de violência doméstica contra a mulher é de ação pública incondicionada (Súmula 542 do STJ).",
], ["CPP:24","CPP:25","CPP:28-A","CPP:29","CPP:30","CPP:38","CPP:41","CPP:48","CPP:49","CPP:395","LMP:16"], ["STJ-SUM-542","STF-SUM-714"]),

T("Prisões e Medidas Cautelares", """
No processo penal, a prisão antes do trânsito em julgado só se admite em caráter cautelar: prisão em flagrante (precautelar), prisão temporária (Lei 7.960/1989, na fase de investigação) e prisão preventiva. Desde o Pacote Anticrime, o juiz não pode decretar preventiva de ofício, e a decisão deve ser fundamentada em fatos novos ou contemporâneos.

A preventiva exige prova da existência do crime, indício suficiente de autoria e perigo gerado pelo estado de liberdade do imputado, além de um dos fundamentos do art. 312 (garantia da ordem pública ou econômica, conveniência da instrução ou aplicação da lei penal) e das hipóteses de cabimento do art. 313. A necessidade deve ser revisada a cada 90 dias (art. 316, parágrafo único).

A prisão é a ultima ratio: o juiz deve preferir as medidas cautelares diversas do art. 319 (comparecimento periódico, proibição de acesso a lugares, monitoração eletrônica etc.). Após o flagrante, o preso deve ser apresentado em audiência de custódia em até 24 horas, quando o juiz relaxa a prisão ilegal, converte em preventiva ou concede liberdade provisória (art. 310).
""", [
 "Flagrante próprio, impróprio e presumido (art. 302).",
 "Audiência de custódia em 24 horas (art. 310).",
 "Preventiva: fundamentos do art. 312 e cabimento do art. 313; vedada de ofício (art. 311).",
 "Revisão da preventiva a cada 90 dias (art. 316, parágrafo único).",
 "Medidas cautelares diversas: art. 319.",
 "Temporária: 5 + 5 dias; 30 + 30 em crimes hediondos (Lei 7.960/1989; Lei 8.072/1990).",
], [
 "Gravidade abstrata do delito não fundamenta preventiva.",
 "Uso de algemas só em caso de resistência, fundado receio de fuga ou perigo (Súmula Vinculante 11).",
 "Flagrante preparado pela polícia gera crime impossível (Súmula 145 do STF); flagrante esperado é válido.",
], ["CPP:282","CPP:302","CPP:310","CPP:311","CPP:312","CPP:313","CPP:316","CPP:319","L7960:1","L7960:2"], ["SV-11","STF-SUM-145"]),

T("Procedimentos", """
O procedimento comum se divide em ordinário (crimes com pena máxima igual ou superior a 4 anos), sumário (pena máxima inferior a 4 anos) e sumaríssimo (infrações de menor potencial ofensivo, nos Juizados Especiais Criminais). Há também procedimentos especiais, como o do Tribunal do Júri, o da Lei de Drogas e o dos crimes de responsabilidade de funcionários públicos.

No ordinário, recebida a denúncia, o acusado é citado para resposta à acusação em 10 dias (art. 396). Em seguida, o juiz pode absolvê-lo sumariamente nas hipóteses do art. 397. Não sendo o caso, designa audiência de instrução e julgamento, em que se ouvem ofendido, testemunhas de acusação e de defesa, peritos e, por último, o interrogatório do acusado (art. 400), seguido de debates orais e sentença.

O Júri é bifásico: a primeira fase (judicium accusationis) termina com pronúncia, impronúncia, desclassificação ou absolvição sumária; a segunda (judicium causae) ocorre em plenário, com os jurados decidindo por quesitos e sob a soberania dos veredictos.
""", [
 "Ordinário: pena máxima ≥ 4 anos; sumário: < 4 anos; sumaríssimo: menor potencial ofensivo (art. 394).",
 "Resposta à acusação em 10 dias (art. 396) e absolvição sumária (art. 397).",
 "Interrogatório é o último ato da instrução (art. 400).",
 "Júri: pronúncia (art. 413), impronúncia (art. 414), absolvição sumária (art. 415).",
 "Menor potencial ofensivo: pena máxima até 2 anos (Lei 9.099/1995, art. 61).",
], [
 "Contra a pronúncia cabe RESE; contra impronúncia e absolvição sumária, apelação (art. 416).",
 "A Lei 9.099/1995 não se aplica aos crimes de violência doméstica contra a mulher (Lei 11.340/2006, art. 41).",
 "Citação por edital com réu ausente e sem advogado suspende processo e prescrição (art. 366).",
], ["CPP:366","CPP:394","CPP:396","CPP:397","CPP:400","CPP:406","CPP:413","CPP:414","CPP:415","CPP:416","LJE:61","LJE:76","LJE:89","LMP:41"]),

T("Nulidades", """
Nulidade é a sanção processual que priva de efeitos o ato praticado em desconformidade com o modelo legal. A doutrina distingue nulidades absolutas (violam norma de interesse público, podem ser reconhecidas a qualquer tempo e, segundo parte da doutrina, têm prejuízo presumido) e relativas (dependem de arguição oportuna e de demonstração de prejuízo, sob pena de preclusão).

O sistema é orientado por princípios. Pelo princípio do prejuízo (pas de nullité sans grief), nenhum ato será declarado nulo se não resultar prejuízo para a acusação ou a defesa (art. 563). Pelo princípio do interesse, nenhuma parte pode arguir nulidade a que haja dado causa ou que só interesse à parte contrária (art. 565). Pela causalidade, a nulidade de um ato contamina os que dele dependam (art. 573, § 1º).

As hipóteses do art. 564 incluem incompetência, suspeição, ilegitimidade de parte e falta de citação. Atenção às súmulas sobre defesa técnica: a falta de defesa constitui nulidade absoluta, mas a deficiência só anula se houver prova de prejuízo.
""", [
 "Princípio do prejuízo (art. 563).",
 "Ninguém pode arguir nulidade a que deu causa (art. 565).",
 "Hipóteses de nulidade: art. 564.",
 "Momentos para arguir nulidades relativas: art. 571.",
 "Falta de defesa é nulidade absoluta; deficiência só anula com prejuízo (Súmula 523 do STF).",
], [
 "Provas ilícitas são inadmissíveis e devem ser desentranhadas, assim como as derivadas (art. 157).",
 "Comparecimento espontâneo do réu supre a falta ou nulidade da citação (art. 570).",
 "Nulidade por falta de intimação da expedição de precatória é relativa (Súmula 155 do STF).",
], ["CPP:157","CPP:563","CPP:564","CPP:565","CPP:566","CPP:570","CPP:571","CPP:572","CPP:573"], ["STF-SUM-523","STF-SUM-155"]),

T("Recursos", """
No processo penal, os recursos são voluntários, com exceção dos casos de recurso de ofício (reexame necessário), como o da sentença que concede habeas corpus. O prazo geral é de 5 dias para interposição de apelação e recurso em sentido estrito, com razões em prazo próprio (8 dias para a apelação; 2 dias para o RESE).

O recurso em sentido estrito (RESE) tem hipóteses taxativas no art. 581, como a decisão que rejeita a denúncia, a que pronuncia o réu e a que concede ou nega fiança. A apelação cabe contra sentenças definitivas de condenação ou absolvição e contra decisões do Júri nas hipóteses do art. 593, III. Também integram o sistema os embargos de declaração (2 dias), os embargos infringentes e de nulidade (privativos da defesa, quando a decisão de segunda instância não for unânime) e a revisão criminal.

Pelo princípio da vedação da reformatio in pejus, em recurso exclusivo da defesa a situação do réu não pode ser agravada, nem mesmo indiretamente, após a anulação da sentença.
""", [
 "Apelação e RESE: 5 dias para interpor (arts. 586 e 593).",
 "RESE: hipóteses do art. 581.",
 "Apelação no Júri: hipóteses taxativas do art. 593, III.",
 "Embargos infringentes e de nulidade: exclusivos da defesa, em 10 dias (art. 609, parágrafo único).",
 "Revisão criminal a qualquer tempo, só em favor do réu (arts. 621 e 622).",
], [
 "Vedação da reformatio in pejus, inclusive indireta (art. 617).",
 "Apelação por decisão manifestamente contrária à prova dos autos só pode ser usada uma vez (art. 593, § 3º).",
 "A interposição do recurso não depende de o réu se recolher à prisão.",
], ["CPP:574","CPP:581","CPP:586","CPP:593","CPP:600","CPP:609","CPP:617","CPP:619","CPP:621","CPP:622"]),
],

"trabalho": [
T("Contrato de Trabalho", """
A relação de emprego exige a presença simultânea de cinco elementos: trabalho prestado por pessoa física, com pessoalidade, não eventualidade, onerosidade e subordinação jurídica (CLT, arts. 2º e 3º). Presentes esses elementos, o vínculo se reconhece pelo princípio da primazia da realidade, ainda que o contrato tenha outro nome.

O contrato de trabalho pode ser tácito ou expresso, verbal ou escrito, por prazo indeterminado (regra) ou determinado. O contrato por prazo determinado só é válido nas hipóteses do art. 443, § 2º, e não pode exceder 2 anos; o contrato de experiência tem limite de 90 dias. A Reforma Trabalhista (Lei 13.467/2017) introduziu o trabalho intermitente e regulou o teletrabalho.

Na sucessão de empregadores, a mudança na propriedade ou na estrutura jurídica da empresa não afeta os contratos de trabalho (arts. 10 e 448), e o sucessor responde pelas obrigações. O grupo econômico gera responsabilidade solidária, exigindo comunhão de interesses e atuação conjunta, não bastando a mera identidade de sócios (art. 2º, §§ 2º e 3º).
""", [
 "Requisitos do vínculo: pessoa física, pessoalidade, não eventualidade, onerosidade e subordinação (art. 3º).",
 "Prazo determinado: máximo de 2 anos; experiência: até 90 dias (art. 445).",
 "Trabalho intermitente: art. 452-A.",
 "Sucessão trabalhista: arts. 10, 448 e 448-A.",
 "Grupo econômico: art. 2º, §§ 2º e 3º.",
], [
 "Contrato de experiência pode ser prorrogado uma única vez, dentro dos 90 dias (Súmula 188 do TST).",
 "Terceirização é lícita em qualquer atividade, inclusive a atividade-fim (STF, Tema 725).",
 "Empregado doméstico tem lei própria (LC 150/2015) e exige trabalho por mais de 2 dias por semana.",
], ["CLT:2","CLT:3","CLT:9","CLT:10","CLT:442","CLT:443","CLT:445","CLT:448","CLT:448-A","CLT:452-A","LC150:1"], ["STF-RG-725"]),

T("Jornada e Remuneração", """
A Constituição limita a duração normal do trabalho a 8 horas diárias e 44 semanais, facultada a compensação de horários e a redução mediante negociação coletiva (art. 7º, XIII). As horas extras são remuneradas com adicional mínimo de 50% e limitadas, em regra, a 2 por dia (CLT, art. 59). A Reforma admitiu banco de horas semestral por acordo individual escrito e a jornada 12x36 por acordo individual.

Os intervalos são obrigatórios: intrajornada de 1 a 2 horas para jornadas acima de 6 horas e de 15 minutos entre 4 e 6 horas (art. 71); interjornada de 11 horas (art. 66); e descanso semanal remunerado de 24 horas consecutivas. Após a Reforma, a supressão do intervalo intrajornada gera o pagamento apenas do período suprimido, com natureza indenizatória.

Remuneração é o gênero que abrange o salário (pago pelo empregador) e as gorjetas (pagas por terceiros). Integram o salário as comissões, percentagens e gratificações legais (art. 457, § 1º); não integram ajuda de custo, auxílio-alimentação (não pago em dinheiro), diárias, prêmios e abonos (§ 2º). Também são direitos o 13º salário, as férias com 1/3 e os adicionais de insalubridade, periculosidade e noturno.
""", [
 "8h diárias e 44h semanais (CF, art. 7º, XIII; CLT, art. 58).",
 "Hora extra: adicional mínimo de 50%, até 2 horas por dia (CLT, art. 59).",
 "Jornada 12x36: art. 59-A.",
 "Intervalos: intrajornada (art. 71) e interjornada (art. 66).",
 "Composição da remuneração: art. 457.",
 "Férias de 30 dias após 12 meses (art. 130), com 1/3 constitucional.",
], [
 "Supressão de intervalo após a Reforma: paga-se só o tempo suprimido, com natureza indenizatória (art. 71, § 4º).",
 "Horas in itinere deixaram de ser computadas na jornada (art. 58, § 2º).",
 "Adicional noturno urbano: 20%, das 22h às 5h, com hora reduzida de 52min30s (art. 73).",
], ["CF:7","CLT:58","CLT:59","CLT:59-A","CLT:66","CLT:71","CLT:73","CLT:130","CLT:457","CLT:458"]),

T("Rescisão Contratual", """
O contrato de trabalho pode terminar por iniciativa do empregador (dispensa sem justa causa ou por justa causa), do empregado (pedido de demissão ou rescisão indireta), por acordo entre as partes (art. 484-A) ou por fatores alheios, como a morte do empregado ou o fim do prazo do contrato determinado.

As faltas graves do empregado que autorizam a justa causa estão no art. 482 (improbidade, mau procedimento, desídia, embriaguez habitual, abandono de emprego etc.). A rescisão indireta é a "justa causa do empregador", nas hipóteses do art. 483, como exigir serviços superiores às forças do empregado ou descumprir obrigações do contrato. A punição deve observar imediatidade, proporcionalidade e vedação ao bis in idem.

O aviso prévio é de no mínimo 30 dias, acrescido de 3 dias por ano de serviço, até 90 dias (Lei 12.506/2011). A rescisão por acordo garante metade do aviso prévio indenizado e da multa do FGTS, saque de 80% do saldo e não dá direito ao seguro-desemprego. As verbas rescisórias devem ser pagas em até 10 dias do término do contrato.
""", [
 "Justa causa do empregado: art. 482.",
 "Rescisão indireta: art. 483.",
 "Distrato (acordo): art. 484-A.",
 "Prazo de pagamento das verbas: 10 dias do término (art. 477, § 6º), sob multa (§ 8º).",
 "Aviso prévio proporcional: 30 dias + 3 por ano, até 90 (Lei 12.506/2011).",
], [
 "Abandono de emprego presume-se após 30 dias de ausência injustificada (Súmula 32 do TST).",
 "Gestante tem estabilidade desde a confirmação da gravidez, mesmo desconhecida pelo empregador (ADCT, art. 10, II, b).",
 "Pedido de demissão não dá direito a saque do FGTS nem à multa de 40%.",
], ["CLT:477","CLT:482","CLT:483","CLT:484-A","CLT:487","L12506:1","ADCT:10"]),

T("FGTS e Verbas Rescisórias", """
O Fundo de Garantia do Tempo de Serviço é um depósito mensal de 8% da remuneração do empregado, feito pelo empregador em conta vinculada (Lei 8.036/1990, art. 15). Substituiu a antiga estabilidade decenal e protege o trabalhador contra a dispensa arbitrária. Na dispensa sem justa causa, o empregador paga multa de 40% sobre o total depositado; na culpa recíproca ou força maior, 20%; no acordo do art. 484-A, também 20%.

As hipóteses de saque estão no art. 20 da Lei 8.036/1990: dispensa sem justa causa, aposentadoria, aquisição de moradia, doenças graves, entre outras, além do saque-aniversário. O STF fixou que a pretensão de cobrar depósitos do FGTS prescreve em 5 anos, respeitado o limite de 2 anos após o fim do contrato (Tema 608).

As verbas rescisórias variam conforme a modalidade de extinção. Na dispensa sem justa causa, o empregado recebe saldo de salário, aviso prévio, 13º proporcional, férias vencidas e proporcionais com 1/3, saque do FGTS com multa de 40% e guias do seguro-desemprego. Na justa causa, apenas saldo de salário e férias vencidas com 1/3.
""", [
 "Depósito mensal de 8% (Lei 8.036/1990, art. 15).",
 "Multa de 40% na dispensa sem justa causa (art. 18, § 1º).",
 "Hipóteses de saque: art. 20.",
 "Prescrição quinquenal do FGTS (STF, Tema 608).",
 "Prescrição trabalhista: 5 anos, até o limite de 2 anos após a extinção do contrato (CF, art. 7º, XXIX).",
], [
 "Na justa causa, o empregado perde aviso prévio, 13º proporcional, férias proporcionais e multa do FGTS (Súmula 171 do TST quanto às férias).",
 "Aprendiz tem FGTS de 2% (art. 15, § 7º).",
 "No acordo do art. 484-A, o saque é limitado a 80% do saldo.",
], ["FGTS:15","FGTS:18","FGTS:20","CF:7","CLT:477","CLT:484-A"], ["STF-RG-608"]),

T("Direito Coletivo", """
O Direito Coletivo do Trabalho regula as relações entre entidades coletivas: sindicatos de trabalhadores e de empregadores (ou empresas). Rege-se pela liberdade sindical (art. 8º da CF), ainda limitada pela unicidade sindical — uma única entidade por categoria na mesma base territorial, não inferior a um município — e, desde a Reforma de 2017, pelo fim da contribuição sindical obrigatória.

Os instrumentos coletivos são a convenção coletiva (entre sindicato profissional e sindicato econômico) e o acordo coletivo (entre sindicato profissional e uma ou mais empresas). A Reforma consagrou a prevalência do negociado sobre o legislado nas matérias do art. 611-A, vedando a negociação sobre os direitos do art. 611-B. O acordo coletivo prevalece sobre a convenção (art. 620), e a ultratividade das normas coletivas é vedada (art. 614, § 3º).

A greve é direito dos trabalhadores, que decidem sobre a oportunidade de exercê-lo (CF, art. 9º; Lei 7.783/1989), com exigências de aviso prévio e de manutenção de serviços essenciais. O dissídio coletivo de natureza econômica exige comum acordo entre as partes (CF, art. 114, § 2º).
""", [
 "Unicidade sindical por base territorial (CF, art. 8º, II).",
 "Contribuição sindical facultativa após a Reforma (CLT, art. 578); contribuição assistencial com direito de oposição (STF, Tema 935).",
 "Prevalência do negociado sobre o legislado: art. 611-A; limites: art. 611-B.",
 "Acordo coletivo prevalece sobre a convenção (art. 620).",
 "Greve: aviso prévio de 48h, ou 72h em serviços essenciais (Lei 7.783/1989, arts. 3º e 13).",
], [
 "Vedada a ultratividade das normas coletivas (CLT, art. 614, § 3º).",
 "Normas coletivas que limitam direitos disponíveis são válidas, respeitados os absolutamente indisponíveis (STF, Tema 1.046).",
 "Dirigente sindical tem estabilidade desde o registro da candidatura até 1 ano após o mandato (CF, art. 8º, VIII).",
], ["CF:8","CF:9","CF:114","CLT:578","CLT:611","CLT:611-A","CLT:611-B","CLT:614","CLT:620","L7783:3","L7783:13"], ["STF-RG-1046","STF-RG-935"]),
],

"tributario": [
T("Espécies Tributárias", """
Tributo é toda prestação pecuniária compulsória, em moeda ou cujo valor nela se possa exprimir, que não constitua sanção de ato ilícito, instituída em lei e cobrada mediante atividade administrativa plenamente vinculada (CTN, art. 3º). O STF adota a teoria pentapartida: impostos, taxas, contribuições de melhoria, empréstimos compulsórios e contribuições especiais.

Impostos são tributos não vinculados: o fato gerador independe de atividade estatal específica relativa ao contribuinte, e sua receita não pode, em regra, ser vinculada a órgão, fundo ou despesa (CF, art. 167, IV). Taxas são vinculadas ao exercício do poder de polícia ou à utilização de serviço público específico e divisível. Contribuições de melhoria decorrem de obra pública que valoriza o imóvel.

Empréstimos compulsórios, de competência exclusiva da União por lei complementar, atendem a calamidade, guerra externa ou investimento público urgente e relevante. As contribuições especiais (sociais, de intervenção no domínio econômico e de interesse das categorias) caracterizam-se pela destinação. A Reforma Tributária (EC 132/2023) criou o IBS e a CBS, em substituição gradual a ICMS, ISS, PIS e Cofins.
""", [
 "Conceito de tributo: CTN, art. 3º.",
 "A natureza jurídica do tributo é determinada pelo fato gerador (CTN, art. 4º).",
 "Taxa: poder de polícia ou serviço específico e divisível (CF, art. 145, II; CTN, art. 77).",
 "Empréstimo compulsório: União, por lei complementar (CF, art. 148).",
 "Contribuições especiais: CF, art. 149.",
], [
 "Taxa não pode ter base de cálculo própria de imposto (CF, art. 145, § 2º; Súmula Vinculante 29 admite elementos da base de imposto sem identidade integral).",
 "Serviço de iluminação pública não pode ser remunerado por taxa (Súmula Vinculante 41); cabe contribuição (CF, art. 149-A).",
 "Taxa de coleta de lixo domiciliar é constitucional (Súmula Vinculante 19).",
], ["CTN:3","CTN:4","CTN:5","CTN:16","CTN:77","CTN:81","CF:145","CF:148","CF:149","CF:149-A","CF:167"], ["SV-29","SV-41","SV-19"]),

T("Competência Tributária", """
Competência tributária é a aptidão constitucional para instituir tributos por lei. É indelegável, irrenunciável, facultativa e incaducável (CTN, arts. 7º e 8º). O que se pode delegar é a capacidade tributária ativa — as funções de arrecadar e fiscalizar —, como ocorre com conselhos profissionais e o ITR fiscalizado por municípios conveniados.

A Constituição reparte os impostos entre os entes: à União, II, IE, IR, IPI, IOF, ITR e IGF (art. 153), além da competência residual (por lei complementar, não cumulativos, com fato gerador e base próprios) e extraordinária (guerra); aos Estados e DF, ITCMD, ICMS e IPVA (art. 155); aos Municípios e DF, IPTU, ITBI e ISS (art. 156). Com a EC 132/2023, foram criados a CBS (União), o IBS (compartilhado por Estados e Municípios) e o Imposto Seletivo (União).

As limitações ao poder de tributar (art. 150) incluem legalidade, isonomia, irretroatividade, anterioridade de exercício e nonagesimal, vedação ao confisco e as imunidades.
""", [
 "Competência é indelegável; capacidade tributária ativa é delegável (CTN, art. 7º).",
 "Impostos da União: art. 153; dos Estados: art. 155; dos Municípios: art. 156.",
 "Competência residual da União: art. 154, I.",
 "Anterioridade de exercício e nonagesimal: art. 150, III, b e c.",
 "Exceções à legalidade e à anterioridade: II, IE, IPI, IOF e alguns casos de CIDE e ICMS-combustível.",
], [
 "IPI respeita a noventena, mas não a anterioridade de exercício.",
 "IR respeita a anterioridade de exercício, mas não a noventena.",
 "Alteração do prazo de recolhimento não se sujeita à anterioridade (Súmula Vinculante 50).",
], ["CTN:6","CTN:7","CTN:8","CF:150","CF:153","CF:154","CF:155","CF:156","CF:156-A","CF:195"], ["SV-50"]),

T("Obrigação Tributária", """
A obrigação tributária nasce com a ocorrência do fato gerador (CTN, art. 113). A obrigação principal tem por objeto o pagamento de tributo ou penalidade pecuniária; a acessória, prestações positivas ou negativas no interesse da arrecadação ou fiscalização (emitir nota, escriturar livros). O descumprimento da acessória converte-a em principal quanto à multa.

O sujeito ativo é a pessoa jurídica de direito público titular da competência de exigir o tributo. O sujeito passivo pode ser o contribuinte (relação pessoal e direta com o fato gerador) ou o responsável (terceiro a quem a lei atribui o dever de pagar). A responsabilidade pode ser por sucessão (arts. 129 a 133), de terceiros (arts. 134 e 135) ou por infrações (arts. 136 a 138).

O crédito tributário é constituído pelo lançamento, que pode ser de ofício, por declaração ou por homologação. A Fazenda tem 5 anos para lançar (decadência, arts. 150, § 4º, e 173) e 5 anos, a partir da constituição definitiva, para cobrar (prescrição, art. 174). O CTN prevê ainda as causas de suspensão (art. 151), extinção (art. 156) e exclusão (art. 175) do crédito.
""", [
 "Obrigação principal e acessória (CTN, art. 113).",
 "Contribuinte e responsável (CTN, art. 121).",
 "Responsabilidade do sócio-gerente por atos com excesso de poderes ou infração de lei (CTN, art. 135).",
 "Denúncia espontânea exclui multa (CTN, art. 138).",
 "Suspensão: art. 151; extinção: art. 156; exclusão: art. 175.",
 "Decadência: arts. 150, § 4º, e 173; prescrição: art. 174.",
], [
 "Simples inadimplemento não gera responsabilidade do sócio-gerente (Súmula 430 do STJ).",
 "Dissolução irregular da empresa presume redirecionamento ao sócio-gerente (Súmula 435 do STJ).",
 "Não cabe denúncia espontânea em tributo declarado e pago com atraso (Súmula 360 do STJ).",
], ["CTN:113","CTN:114","CTN:121","CTN:128","CTN:131","CTN:133","CTN:134","CTN:135","CTN:138","CTN:142","CTN:150","CTN:151","CTN:156","CTN:173","CTN:174","CTN:175"], ["STJ-SUM-430","STJ-SUM-435","STJ-SUM-360"]),

T("Imunidades e Isenções", """
Imunidade é norma constitucional que retira determinadas pessoas, bens ou situações do campo de competência tributária: o ente simplesmente não pode instituir o tributo. Isenção, ao contrário, é dispensa legal do pagamento de tributo que o ente tinha competência para instituir; atua no plano do exercício da competência e depende de lei do próprio ente (CTN, art. 176).

As imunidades genéricas do art. 150, VI, alcançam impostos sobre: patrimônio, renda e serviços dos entes federados entre si (recíproca); templos de qualquer culto; partidos políticos, entidades sindicais dos trabalhadores, instituições de educação e de assistência social sem fins lucrativos; livros, jornais, periódicos e o papel destinado à sua impressão; e fonogramas e videofonogramas musicais produzidos no Brasil.

A imunidade recíproca estende-se a autarquias e fundações públicas e, segundo o STF, a empresas públicas e sociedades de economia mista prestadoras de serviço público em regime de monopólio ou não concorrencial, como a ECT. Há também imunidades específicas, como as das contribuições sociais para entidades beneficentes de assistência social (art. 195, § 7º), que exigem requisitos de lei complementar.
""", [
 "Imunidades genéricas: CF, art. 150, VI (alcançam apenas impostos).",
 "Isenção decorre de lei específica (CF, art. 150, § 6º; CTN, art. 176).",
 "Imunidade recíproca estendida às autarquias e fundações (art. 150, § 2º).",
 "Entidades beneficentes: imunidade das contribuições sociais (art. 195, § 7º).",
 "Requisitos das entidades de educação e assistência: CTN, art. 14.",
], [
 "IPTU de imóvel de entidade imune alugado a terceiros continua imune se a renda é aplicada nas finalidades (Súmula Vinculante 52).",
 "Livro eletrônico e seus suportes exclusivos estão imunes (Súmula Vinculante 57).",
 "Isenção não alcança taxas e contribuições de melhoria, salvo lei (CTN, art. 177).",
], ["CF:150","CF:195","CTN:9","CTN:14","CTN:176","CTN:177","CTN:178"], ["SV-52","SV-57"]),

T("Processo Tributário", """
O processo tributário se divide em administrativo e judicial. No âmbito federal, o processo administrativo fiscal (Decreto 70.235/1972) se inicia pela impugnação do lançamento, em 30 dias, com julgamento em primeira instância pelas Delegacias de Julgamento e, em segunda, pelo CARF. A impugnação e o recurso administrativo suspendem a exigibilidade do crédito (CTN, art. 151, III).

No âmbito judicial, o contribuinte dispõe de ações como o mandado de segurança (preventivo ou repressivo, com prova pré-constituída), a ação declaratória de inexistência de relação jurídica, a ação anulatória de débito fiscal, a ação de repetição de indébito e a ação de consignação em pagamento. A Fazenda cobra seus créditos por execução fiscal (Lei 6.830/1980), com base na Certidão de Dívida Ativa.

Na execução fiscal, o executado se defende por embargos, após garantir o juízo, em 30 dias (LEF, art. 16), ou por exceção de pré-executividade, para matérias de ordem pública que dispensem dilação probatória. A Fazenda Pública responde por honorários e pode desistir da execução.
""", [
 "Execução fiscal: Lei 6.830/1980; embargos em 30 dias após garantia (LEF, art. 16).",
 "Exceção de pré-executividade: matérias conhecíveis de ofício sem dilação probatória (Súmula 393 do STJ).",
 "Repetição de indébito: CTN, arts. 165 a 169; prazo de 5 anos (art. 168).",
 "Compensação só após o trânsito em julgado da decisão (CTN, art. 170-A).",
 "Depósito integral suspende a exigibilidade (CTN, art. 151, II; Súmula 112 do STJ).",
], [
 "Mandado de segurança não é substitutivo de ação de cobrança (Súmula 269 do STF).",
 "Mandado de segurança é via adequada para declarar o direito à compensação (Súmula 213 do STJ).",
 "Prescrição intercorrente na execução fiscal após 1 ano de suspensão + 5 anos (LEF, art. 40; Súmula 314 do STJ).",
], ["CTN:151","CTN:165","CTN:168","CTN:170-A","LEF:2","LEF:16","LEF:40","D70235:15","LMS:1"], ["STJ-SUM-393","STJ-SUM-112","STJ-SUM-213","STJ-SUM-314","STF-SUM-269"]),
],
}
