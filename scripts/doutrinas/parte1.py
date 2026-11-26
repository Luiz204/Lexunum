# Conteúdo autoral de estudo — Lex Unum. Civil, Penal, Constitucional, Administrativo.
def T(titulo, resumo, pontos, prova, artigos=(), prec=()):
    return {"titulo": titulo, "resumo": resumo.strip(), "pontos": list(pontos), "prova": list(prova),
            "artigos": list(artigos), "precedentes": list(prec)}

DADOS = {
"civil": [
T("Parte Geral", """
A Parte Geral do Código Civil organiza três grandes blocos: as pessoas (naturais e jurídicas), os bens e os fatos jurídicos. Para a pessoa natural, o Código adota a teoria natalista — a personalidade começa do nascimento com vida —, mas resguarda desde a concepção os direitos do nascituro, o que a jurisprudência amplia (por exemplo, para reconhecer dano moral ao nascituro).

Após o Estatuto da Pessoa com Deficiência (Lei 13.146/2015), só o menor de 16 anos é absolutamente incapaz. A deficiência, por si só, não afeta a capacidade civil; quem não pode exprimir a vontade passou a ser relativamente incapaz. Os direitos da personalidade são intransmissíveis e irrenunciáveis e recebem tutela inibitória e reparatória.

No negócio jurídico, separe os planos de existência, validade e eficácia. A validade exige agente capaz, objeto lícito, possível e determinável e forma prescrita ou não proibida. Nulidade (absoluta) não convalesce e pode ser declarada de ofício; anulabilidade (relativa) depende de provocação do interessado e se sujeita a prazo decadencial.
""", [
 "Personalidade: nascimento com vida (teoria natalista), com proteção ao nascituro desde a concepção (art. 2º).",
 "Absolutamente incapaz: apenas o menor de 16 anos (art. 3º). Relativamente: 16–18, ébrios habituais e viciados, quem não pode exprimir vontade, pródigos (art. 4º).",
 "Emancipação voluntária (pais, por instrumento público, a partir dos 16) dispensa homologação judicial (art. 5º, parágrafo único, I).",
 "Nulidade: não se convalida e não corre prazo (art. 169). Anulabilidade: prazo decadencial de 4 anos, em regra (art. 178).",
 "Defeitos do negócio: erro, dolo, coação, estado de perigo, lesão e fraude contra credores; a simulação gera nulidade (art. 167).",
 "Prescrição atinge a pretensão (art. 189); decadência atinge o próprio direito potestativo.",
], [
 "Deficiência mental não torna, por si, a pessoa incapaz — cai muito após a Lei 13.146/2015.",
 "Simulação é causa de nulidade, não de anulabilidade, e subsiste o negócio dissimulado se válido na substância e na forma.",
 "Prazo geral de prescrição é de 10 anos (art. 205); reparação civil prescreve em 3 anos (art. 206, § 3º, V).",
], ["CC:1","CC:2","CC:3","CC:4","CC:5","CC:11","CC:104","CC:166","CC:167","CC:171","CC:178","CC:189","CC:205","CC:206"]),

T("Obrigações", """
Obrigação é o vínculo jurídico transitório pelo qual o devedor fica adstrito a cumprir uma prestação (dar, fazer ou não fazer) em favor do credor. Seus elementos são subjetivo (credor e devedor), objetivo (a prestação) e o vínculo jurídico, que se decompõe em débito (Schuld) e responsabilidade (Haftung).

O Código disciplina as modalidades (dar coisa certa e incerta, fazer, não fazer, alternativas, divisíveis e indivisíveis, solidárias), a transmissão (cessão de crédito e assunção de dívida), o adimplemento e suas formas especiais (pagamento em consignação, sub-rogação, imputação, dação, novação, compensação, confusão e remissão) e o inadimplemento.

No inadimplemento, distinga o absoluto (a prestação se tornou inútil ou impossível) da mora (atraso ainda útil ao credor). O devedor responde por perdas e danos, juros, atualização monetária e honorários. A cláusula penal pré-fixa as perdas e danos e não pode exceder o valor da obrigação principal.
""", [
 "Solidariedade não se presume: resulta da lei ou da vontade das partes (art. 265).",
 "Na solidariedade passiva, o credor pode cobrar de qualquer devedor a dívida toda (art. 275).",
 "Mora ex re (termo certo) constitui em mora automaticamente — dies interpellat pro homine (art. 397).",
 "Inadimplemento gera perdas e danos, juros, atualização monetária e honorários (art. 389).",
 "Cláusula penal limitada ao valor da obrigação principal (art. 412) e redutível pelo juiz (art. 413).",
 "Cessão de crédito só é eficaz contra o devedor depois de notificado (art. 290).",
], [
 "Obrigação indivisível ≠ solidária: convertida em perdas e danos, a indivisível perde essa qualidade (art. 263); a solidária não.",
 "Novação exige ânimo de novar; sem ele, a segunda obrigação apenas confirma a primeira (art. 361).",
 "Juros de mora na responsabilidade extracontratual contam do evento danoso (Súmula 54 do STJ).",
], ["CC:233","CC:247","CC:250","CC:263","CC:265","CC:275","CC:286","CC:290","CC:304","CC:360","CC:368","CC:389","CC:394","CC:397","CC:402","CC:412","CC:413"], ["STJ-SUM-54"]),

T("Contratos", """
Contrato é o negócio jurídico bilateral (ou plurilateral) que cria, modifica ou extingue relações patrimoniais. A teoria geral moderna equilibra a autonomia privada com os princípios sociais: a função social do contrato (art. 421) e a boa-fé objetiva (art. 422), que gera deveres anexos de informação, cooperação e lealdade em todas as fases — pré-contratual, execução e pós-contratual.

A Lei da Liberdade Econômica (Lei 13.874/2019) reforçou a intervenção mínima e a excepcionalidade da revisão contratual nas relações paritárias (art. 421, parágrafo único, e art. 421-A). Ainda assim, permanecem os institutos de equilíbrio: lesão, estado de perigo, resolução por onerosidade excessiva (arts. 478 a 480) e vícios redibitórios.

Na formação, proposta obriga o proponente (art. 427) e, entre ausentes, o contrato se forma com a expedição da aceitação (teoria da expedição, art. 434). Nos contratos bilaterais, vale a exceção de contrato não cumprido (art. 476).
""", [
 "Função social limita a liberdade contratual (art. 421); boa-fé objetiva gera deveres anexos (art. 422).",
 "Revisão contratual é excepcional nas relações civis e empresariais paritárias (art. 421-A, III).",
 "Onerosidade excessiva por fato extraordinário e imprevisível permite resolução (art. 478) ou revisão equitativa (art. 479).",
 "Exceção de contrato não cumprido: nenhum contratante pode exigir a prestação do outro antes de cumprir a sua (art. 476).",
 "Vícios redibitórios: defeitos ocultos em contrato comutativo; ação redibitória ou quanti minoris (arts. 441 e 442).",
 "Evicção: perda da coisa por decisão judicial ou administrativa; o alienante responde (art. 447).",
], [
 "Prazo para reclamar de vício redibitório: 30 dias (móvel) ou 1 ano (imóvel), contados da entrega (art. 445).",
 "Contrato entre ausentes: regra é a expedição (art. 434), com exceções.",
 "Venda de ascendente a descendente é anulável sem consentimento dos demais descendentes e do cônjuge (art. 496).",
], ["CC:421","CC:421-A","CC:422","CC:427","CC:434","CC:441","CC:442","CC:445","CC:447","CC:476","CC:478","CC:479","CC:496"]),

T("Responsabilidade Civil", """
A responsabilidade civil impõe o dever de reparar o dano causado a outrem. Na modalidade subjetiva (regra geral), exige conduta culposa ou dolosa, dano e nexo causal (art. 186 c/c art. 927, caput). Na objetiva, dispensa-se a culpa: basta conduta, dano e nexo, nos casos previstos em lei ou quando a atividade normalmente desenvolvida implicar risco (art. 927, parágrafo único — cláusula geral do risco).

Também comete ato ilícito quem exerce um direito excedendo manifestamente os limites impostos pelo fim econômico ou social, pela boa-fé ou pelos bons costumes (abuso de direito, art. 187). Há responsabilidade por fato de terceiro — pais pelos filhos menores, empregador pelos empregados —, que é objetiva quanto ao responsável (art. 933).

Excluem o nexo causal o caso fortuito ou força maior, a culpa exclusiva da vítima e o fato exclusivo de terceiro. A indenização mede-se pela extensão do dano (art. 944), cabendo redução equitativa se houver excessiva desproporção entre a gravidade da culpa e o dano.
""", [
 "Elementos da subjetiva: conduta, culpa ou dolo, dano e nexo causal (arts. 186 e 927).",
 "Cláusula geral de responsabilidade objetiva pelo risco da atividade (art. 927, parágrafo único).",
 "Abuso de direito é ato ilícito com critério objetivo, sem necessidade de culpa (art. 187).",
 "Responsabilidade dos pais, tutores e empregadores por terceiros é objetiva (arts. 932 e 933).",
 "Dano moral é indenizável, inclusive à pessoa jurídica (Súmula 227 do STJ).",
 "Pretensão de reparação civil prescreve em 3 anos (art. 206, § 3º, V).",
], [
 "Responsabilidade civil independe da criminal, mas não se discute mais a existência do fato ou a autoria decididas no crime (art. 935).",
 "Inscrição indevida em cadastro não gera dano moral se havia inscrição legítima anterior (Súmula 385 do STJ).",
 "Juros de mora: evento danoso na extracontratual (Súmula 54); correção do dano moral: data do arbitramento (Súmula 362 do STJ).",
], ["CC:186","CC:187","CC:927","CC:932","CC:933","CC:935","CC:944","CC:206"], ["STJ-SUM-227","STJ-SUM-385","STJ-SUM-54","STJ-SUM-362","STJ-SUM-37"]),

T("Família", """
O Direito de Família contemporâneo é orientado pela dignidade da pessoa humana, pela igualdade entre cônjuges e entre filhos e pela afetividade. A Constituição reconhece como entidades familiares o casamento, a união estável e a família monoparental, e o STF estendeu a união estável e o casamento aos casais do mesmo sexo (ADI 4277 e ADPF 132).

O casamento estabelece comunhão plena de vida. Os regimes de bens são comunhão parcial (regime legal supletivo), comunhão universal, separação convencional, separação obrigatória e participação final nos aquestos. Desde a EC 66/2010, o divórcio é direto, sem prazo e sem discussão de culpa.

A união estável exige convivência pública, contínua e duradoura com objetivo de constituir família, e se aplica a ela, no que couber, o regime da comunhão parcial. No parentesco e na filiação, vigoram a igualdade absoluta entre os filhos e o reconhecimento da multiparentalidade (Tema 622 do STF). Alimentos seguem o binômio necessidade–possibilidade.
""", [
 "Regime legal supletivo: comunhão parcial (art. 1.640).",
 "Separação obrigatória para maiores de 70 anos (art. 1.641, II), afastável por escritura pública, conforme o STF (Tema 1.236).",
 "União estável: convivência pública, contínua e duradoura com objetivo de família (art. 1.723).",
 "Filhos têm os mesmos direitos, vedadas designações discriminatórias (art. 1.596; CF, art. 227, § 6º).",
 "Alimentos: necessidade de quem pede e possibilidade de quem paga (art. 1.694, § 1º).",
 "Guarda compartilhada é a regra quando ambos estão aptos (art. 1.584, § 2º).",
], [
 "Divórcio não exige prévia separação nem prazo desde a EC 66/2010.",
 "Paternidade socioafetiva não impede o reconhecimento da biológica, com efeitos jurídicos próprios (Tema 622 do STF).",
 "Prisão civil só cabe por dívida alimentar atual: as três prestações anteriores ao ajuizamento e as que vencerem no curso do processo (Súmula 309 do STJ).",
], ["CC:1511","CC:1583","CC:1584","CC:1596","CC:1640","CC:1641","CC:1694","CC:1723","CC:1725"], ["STJ-SUM-309","STF-RG-622"]),

T("Sucessões", """
Aberta a sucessão, a herança transmite-se desde logo aos herdeiros legítimos e testamentários (princípio de saisine, art. 1.784). A sucessão pode ser legítima (segundo a ordem legal) ou testamentária. Havendo herdeiros necessários — descendentes, ascendentes e cônjuge —, o testador só pode dispor de metade da herança (legítima).

A ordem de vocação hereditária do art. 1.829 chama: descendentes em concorrência com o cônjuge (conforme o regime de bens); ascendentes em concorrência com o cônjuge; o cônjuge sozinho; e os colaterais até o quarto grau. O STF declarou inconstitucional o art. 1.790 e equiparou o companheiro ao cônjuge para fins sucessórios (Tema 809).

Estude também aceitação e renúncia da herança, exclusão por indignidade e deserdação, as formas de testamento (público, cerrado e particular) e o inventário, que pode ser extrajudicial quando todos forem capazes e concordes.
""", [
 "Saisine: transmissão imediata da herança com a morte (art. 1.784).",
 "Herdeiros necessários: descendentes, ascendentes e cônjuge (art. 1.845); a legítima é metade (art. 1.846).",
 "Ordem de vocação: art. 1.829 — o cônjuge concorre com descendentes conforme o regime de bens.",
 "Companheiro equiparado ao cônjuge na sucessão (STF, Tema 809).",
 "Renúncia deve ser expressa, por instrumento público ou termo judicial (art. 1.806).",
 "Direito real de habitação do cônjuge sobrevivente sobre o imóvel residencial (art. 1.831).",
], [
 "Na comunhão universal e na separação obrigatória, o cônjuge não concorre com descendentes (art. 1.829, I).",
 "Na comunhão parcial, o cônjuge só concorre se o falecido deixou bens particulares, e apenas sobre eles.",
 "Indignidade depende de sentença (art. 1.815); deserdação exige testamento com causa expressa (art. 1.964).",
], ["CC:1784","CC:1806","CC:1814","CC:1815","CC:1829","CC:1831","CC:1845","CC:1846","CC:1964"], ["STF-RG-809"]),

T("Direitos Reais", """
Direitos reais são poderes jurídicos diretos sobre a coisa, oponíveis a todos (erga omnes), dotados de sequela e preferência e sujeitos ao princípio da tipicidade: só existem os previstos em lei (rol do art. 1.225). A propriedade é o direito real mais amplo — usar, gozar, dispor e reaver —, condicionado à sua função social.

A posse é a situação de fato de quem exerce algum dos poderes inerentes à propriedade (teoria objetiva de Ihering, art. 1.196). É protegida por interditos possessórios: manutenção (turbação), reintegração (esbulho) e interdito proibitório (ameaça). A ação possessória tem natureza dúplice e admite fungibilidade.

A propriedade imóvel adquire-se pelo registro, pela acessão e pela usucapião. Memorize as espécies de usucapião e seus prazos: extraordinária (15 anos, ou 10 com moradia ou obras produtivas), ordinária (10 anos, ou 5 em hipóteses especiais), especial urbana e rural (5 anos) e familiar (2 anos).
""", [
 "Rol taxativo de direitos reais no art. 1.225 (inclui laje, desde 2017).",
 "Posse: exercício de fato de algum poder da propriedade (art. 1.196).",
 "Usucapião extraordinária: 15 anos sem justo título nem boa-fé, reduzida a 10 com moradia ou obras (art. 1.238).",
 "Usucapião ordinária: 10 anos com justo título e boa-fé (art. 1.242).",
 "Usucapião familiar: 2 anos, imóvel urbano até 250 m², ex-cônjuge que abandonou o lar (art. 1.240-A).",
 "Imóveis se adquirem pelo registro no Registro de Imóveis (art. 1.245).",
], [
 "Bens públicos não são usucapíveis (CF, art. 183, § 3º; CC, art. 102).",
 "Usucapião especial urbana: até 250 m², 5 anos, moradia, sem outro imóvel (CF, art. 183; CC, art. 1.240).",
 "Composse e posse indireta convivem: locatário (direta) e locador (indireta) podem defender a posse.",
], ["CC:1196","CC:1197","CC:1210","CC:1225","CC:1228","CC:1238","CC:1240","CC:1240-A","CC:1242","CC:1245","CC:102","CF:183"]),
],

"penal": [
T("Teoria Geral do Crime", """
Pelo conceito analítico tripartido, crime é fato típico, ilícito (antijurídico) e culpável. O fato típico reúne conduta (dolosa ou culposa), resultado, nexo causal e tipicidade. O Código Penal adota a teoria da equivalência dos antecedentes (conditio sine qua non), temperada pela causa superveniente relativamente independente que, por si só, produz o resultado (art. 13, § 1º).

A ilicitude é a contrariedade do fato ao ordenamento e é afastada pelas excludentes do art. 23: estado de necessidade, legítima defesa, estrito cumprimento de dever legal e exercício regular de direito. A culpabilidade é juízo de reprovação que exige imputabilidade, potencial consciência da ilicitude e exigibilidade de conduta diversa.

Distinga erro de tipo (recai sobre elemento do tipo, exclui o dolo — art. 20) de erro de proibição (recai sobre a ilicitude; se inevitável, isenta de pena; se evitável, reduz — art. 21). No iter criminis, só a execução é punível: tentativa reduz a pena de 1 a 2/3; desistência voluntária e arrependimento eficaz fazem o agente responder apenas pelos atos já praticados.
""", [
 "Crime = fato típico + ilicitude + culpabilidade (conceito tripartido).",
 "Dolo direto e eventual (art. 18, I); culpa por imprudência, negligência ou imperícia (art. 18, II).",
 "Tentativa: pena do consumado reduzida de 1 a 2/3 (art. 14, parágrafo único).",
 "Desistência voluntária e arrependimento eficaz: responde só pelos atos praticados (art. 15).",
 "Arrependimento posterior: crime sem violência ou grave ameaça, reparação até o recebimento da denúncia — redução de 1 a 2/3 (art. 16).",
 "Crime impossível por ineficácia absoluta do meio ou impropriedade absoluta do objeto (art. 17).",
], [
 "Erro de tipo inevitável exclui dolo e culpa; evitável permite punição por culpa, se prevista (art. 20).",
 "Legítima defesa exige agressão injusta, atual ou iminente, e uso moderado dos meios necessários (art. 25).",
 "Inimputabilidade por doença mental adota o critério biopsicológico (art. 26); a do menor de 18 é puramente biológica (art. 27).",
], ["CP:13","CP:14","CP:15","CP:16","CP:17","CP:18","CP:20","CP:21","CP:23","CP:24","CP:25","CP:26","CP:27","CP:28"]),

T("Concurso de Pessoas", """
O Código Penal adota, como regra, a teoria monista (unitária): quem, de qualquer modo, concorre para o crime incide nas penas a ele cominadas, na medida de sua culpabilidade (art. 29). Há exceções pluralistas, em que a lei cria tipos distintos para coautores (por exemplo, corrupção ativa e passiva; aborto consentido e provocado por terceiro).

São requisitos do concurso de pessoas: pluralidade de agentes e de condutas, relevância causal de cada conduta, liame subjetivo (vontade de participar da obra comum, sem necessidade de acordo prévio) e identidade de infração. Para distinguir autor de partícipe, a doutrina majoritária adota a teoria do domínio do fato para crimes dolosos: autor é quem tem o controle final do fato.

A participação é acessória e, pela teoria da acessoriedade limitada, exige que o fato principal seja típico e ilícito. A participação de menor importância reduz a pena de 1/6 a 1/3, e se algum concorrente quis participar de crime menos grave, aplica-se a ele a pena deste (cooperação dolosamente distinta).
""", [
 "Teoria monista como regra (art. 29, caput).",
 "Participação de menor importância: redução de 1/6 a 1/3 (art. 29, § 1º).",
 "Cooperação dolosamente distinta: responde pelo crime menos grave que quis, com aumento até metade se o mais grave era previsível (art. 29, § 2º).",
 "Circunstâncias de caráter pessoal não se comunicam, salvo quando elementares do crime (art. 30).",
 "Ajuste, determinação, instigação e auxílio não são puníveis se o crime não chega a ser tentado (art. 31).",
], [
 "Liame subjetivo dispensa acordo prévio; autoria colateral (sem liame) não é concurso de pessoas.",
 "A condição de funcionário público, elementar do peculato, comunica-se ao particular que sabe dela (art. 30).",
 "Não há participação dolosa em crime culposo, nem participação culposa em crime doloso.",
], ["CP:29","CP:30","CP:31","CP:62"]),

T("Penas", """
As penas previstas no Código Penal são privativas de liberdade (reclusão e detenção), restritivas de direitos e multa. A aplicação segue o sistema trifásico (art. 68): na primeira fase, o juiz fixa a pena-base com as circunstâncias judiciais do art. 59; na segunda, considera agravantes e atenuantes; na terceira, aplica causas de aumento e diminuição.

O regime inicial depende da quantidade de pena, da reincidência e das circunstâncias judiciais: acima de 8 anos, fechado; mais de 4 até 8, semiaberto (não reincidente); até 4, aberto (não reincidente). Reclusão admite os três regimes; detenção, em regra, só semiaberto e aberto.

A substituição por restritivas de direitos cabe quando a pena não supera 4 anos, o crime não foi cometido com violência ou grave ameaça à pessoa (ou é culposo), o réu não é reincidente em crime doloso e as circunstâncias indicam ser suficiente. Estude também o sursis, o livramento condicional e as causas extintivas da punibilidade, em especial a prescrição.
""", [
 "Sistema trifásico: pena-base (art. 59), agravantes/atenuantes, causas de aumento/diminuição (art. 68).",
 "Na segunda fase a pena não pode ficar abaixo do mínimo legal (Súmula 231 do STJ).",
 "Regimes iniciais: art. 33, § 2º.",
 "Substituição por restritivas de direitos: art. 44.",
 "Limite de cumprimento das penas privativas de liberdade: 40 anos (art. 75, após a Lei 13.964/2019).",
 "Prescrição da pretensão punitiva regulada pelo máximo da pena em abstrato (art. 109).",
], [
 "Gravidade abstrata do crime não justifica regime mais severo que o cabível pela pena (Súmulas 718 e 719 do STF; Súmula 440 do STJ).",
 "Reincidência: novo crime após trânsito em julgado de condenação anterior, por 5 anos (arts. 63 e 64).",
 "Confissão espontânea e menoridade relativa (menor de 21 na data do fato) são atenuantes (art. 65).",
], ["CP:32","CP:33","CP:44","CP:59","CP:61","CP:63","CP:64","CP:65","CP:68","CP:75","CP:77","CP:83","CP:107","CP:109"], ["STJ-SUM-231","STF-SUM-718","STF-SUM-719","STJ-SUM-440"]),

T("Crimes contra a Pessoa", """
O Título I da Parte Especial protege a vida, a integridade corporal, a honra e a liberdade individual. O homicídio (art. 121) admite as formas simples, privilegiada (relevante valor social ou moral, ou domínio de violenta emoção logo após injusta provocação da vítima), qualificada e culposa. Desde a Lei 14.994/2024, o feminicídio é crime autônomo (art. 121-A), com pena de 20 a 40 anos.

A competência para os crimes dolosos contra a vida é do Tribunal do Júri (CF, art. 5º, XXXVIII). Também integram o capítulo o induzimento, instigação ou auxílio a suicídio ou automutilação (art. 122), o infanticídio (art. 123) e o aborto (arts. 124 a 128), com as hipóteses legais de aborto necessário e no caso de gravidez resultante de estupro.

Nas lesões corporais, a gravidade se mede pelo resultado: leve, grave (§ 1º), gravíssima (§ 2º) e seguida de morte (§ 3º, preterdoloso). Nos crimes contra a honra, distinga calúnia (imputar falsamente fato definido como crime), difamação (fato ofensivo à reputação) e injúria (ofensa à dignidade ou ao decoro, sem imputação de fato).
""", [
 "Homicídio privilegiado: redução de 1/6 a 1/3 (art. 121, § 1º).",
 "Qualificadoras objetivas podem coexistir com o privilégio (homicídio qualificado-privilegiado), que não é hediondo.",
 "Feminicídio como crime autônomo (art. 121-A, Lei 14.994/2024).",
 "Infanticídio: mãe, sob influência do estado puerperal, durante o parto ou logo após (art. 123).",
 "Aborto legal: necessário ou em gravidez resultante de estupro (art. 128); o STF também afastou a punição no caso de anencefalia (ADPF 54).",
 "Calúnia, difamação e injúria: arts. 138 a 140; só a calúnia admite, em regra, exceção da verdade ampla.",
], [
 "Lesão gravíssima inclui perda ou inutilização de membro, sentido ou função e aborto (art. 129, § 2º).",
 "Injúria racial foi equiparada ao racismo e passou à Lei 7.716/1989 (art. 2º-A, Lei 14.532/2023).",
 "Homicídio culposo na direção de veículo segue o CTB (art. 302), não o Código Penal.",
], ["CP:121","CP:121-A","CP:122","CP:123","CP:124","CP:128","CP:129","CP:138","CP:139","CP:140","CF:5","CTB:302"]),

T("Crimes contra o Patrimônio", """
Os crimes patrimoniais (arts. 155 a 183) protegem a posse e a propriedade. O ponto central é distinguir as figuras próximas. Furto é subtrair coisa alheia móvel sem violência ou grave ameaça; roubo é a subtração com violência ou grave ameaça à pessoa (ou após reduzi-la à impossibilidade de resistência); extorsão exige a colaboração da vítima, constrangida a fazer, tolerar ou deixar de fazer algo.

Estelionato é obter vantagem ilícita induzindo ou mantendo alguém em erro mediante fraude — a vítima entrega o bem iludida. Na apropriação indébita, o agente já tem a posse lícita da coisa e inverte o ânimo, passando a agir como dono. Desde a Lei 13.964/2019, o estelionato é, em regra, de ação pública condicionada à representação.

O STF e o STJ consolidaram o momento consumativo: furto e roubo consumam-se com a inversão da posse, ainda que breve e sem posse mansa e pacífica (teoria da amotio). O princípio da insignificância pode afastar a tipicidade material do furto em casos de mínima ofensividade, mas não se aplica ao roubo.
""", [
 "Furto (art. 155) × roubo (art. 157): presença de violência ou grave ameaça à pessoa.",
 "Furto privilegiado: réu primário e coisa de pequeno valor (art. 155, § 2º), compatível com qualificadoras objetivas (Súmula 511 do STJ).",
 "Latrocínio é crime contra o patrimônio, julgado pelo juiz singular (Súmula 603 do STF).",
 "Estelionato (art. 171) é de ação condicionada à representação, com exceções do § 5º.",
 "Escusas absolutórias entre cônjuges e parentes próximos (art. 181), salvo violência, grave ameaça ou vítima idosa (art. 183).",
], [
 "Consumação do roubo com a inversão da posse, dispensada a posse mansa e pacífica (Súmula 582 do STJ).",
 "Insignificância não se aplica a crimes com violência ou grave ameaça.",
 "Apropriação indébita: a posse é anterior e lícita; no estelionato a fraude é anterior à obtenção do bem.",
], ["CP:155","CP:157","CP:158","CP:168","CP:171","CP:180","CP:181","CP:183"], ["STJ-SUM-511","STJ-SUM-582","STF-SUM-603"]),

T("Execução Penal", """
A Lei de Execução Penal (Lei 7.210/1984) tem por objetivo efetivar a sentença e proporcionar condições para a integração social do condenado. A execução é jurisdicionalizada: o juiz da execução decide sobre progressão, livramento, remição, unificação de penas e incidentes, sempre com contraditório.

O sistema é progressivo. Após o Pacote Anticrime, a progressão segue percentuais escalonados no art. 112: de 16% (primário, crime sem violência ou grave ameaça) até 70% (reincidente em crime hediondo ou equiparado com resultado morte, vedado o livramento condicional). Além do requisito objetivo, exige-se boa conduta carcerária.

A remição permite descontar pena pelo trabalho (1 dia a cada 3 trabalhados) e pelo estudo (1 dia a cada 12 horas de frequência escolar). A falta grave pode regredir o regime e interromper o prazo para nova progressão, mas não interrompe o prazo para livramento condicional, indulto e comutação.
""", [
 "Progressão por percentuais escalonados (LEP, art. 112, redação da Lei 13.964/2019).",
 "Remição: 1 dia por 3 de trabalho ou por 12 horas de estudo (LEP, art. 126).",
 "Falta grave interrompe o prazo de progressão (Súmula 534 do STJ), mas não o de livramento condicional (Súmula 441 do STJ).",
 "Regressão de regime por falta grave ou novo crime doloso (LEP, art. 118).",
 "Falta de vaga no regime adequado não autoriza manter o condenado em regime mais gravoso (Súmula Vinculante 56).",
], [
 "Exame criminológico pode ser exigido por decisão fundamentada (Súmula 439 do STJ; Súmula Vinculante 26).",
 "Progressão per saltum (do fechado direto ao aberto) é vedada (Súmula 491 do STJ).",
 "Prática de falta grave deve ser apurada em procedimento com defesa técnica (Súmula 533 do STJ).",
], ["LEP:1","LEP:66","LEP:112","LEP:118","LEP:126","LEP:127"], ["STJ-SUM-534","STJ-SUM-441","SV-56","SV-26","STJ-SUM-491","STJ-SUM-439","STJ-SUM-533"]),
],

"constitucional": [
T("Direitos Fundamentais", """
Os direitos e garantias fundamentais estão espalhados pela Constituição, mas concentram-se no Título II: direitos individuais e coletivos (art. 5º), sociais (arts. 6º a 11), de nacionalidade (arts. 12 e 13) e políticos (arts. 14 a 17). Têm aplicabilidade imediata (art. 5º, § 1º), são cláusulas pétreas e vinculam também os particulares (eficácia horizontal).

Costuma-se classificá-los em gerações ou dimensões: liberdades negativas (1ª), direitos sociais prestacionais (2ª) e direitos difusos de solidariedade (3ª). Nenhum direito fundamental é absoluto: conflitos são resolvidos por ponderação, com o princípio da proporcionalidade (adequação, necessidade e proporcionalidade em sentido estrito).

Os remédios constitucionais garantem esses direitos: habeas corpus (liberdade de locomoção), mandado de segurança (direito líquido e certo), habeas data (dados pessoais), mandado de injunção (falta de norma regulamentadora) e ação popular (ato lesivo ao patrimônio público e à moralidade).
""", [
 "Aplicabilidade imediata das normas definidoras de direitos fundamentais (art. 5º, § 1º).",
 "Rol do art. 5º é exemplificativo (art. 5º, § 2º).",
 "Tratados de direitos humanos aprovados com rito de emenda equivalem a emendas constitucionais (art. 5º, § 3º).",
 "Remédios constitucionais: art. 5º, LXVIII a LXXIII.",
 "Direitos sociais: rol do art. 6º.",
], [
 "Estrangeiros não residentes também são titulares de direitos fundamentais, apesar da redação literal do caput.",
 "Habeas corpus e habeas data são gratuitos (art. 5º, LXXVII); a ação popular é isenta de custas, salvo má-fé.",
 "Inviolabilidade do domicílio admite ingresso sem consentimento em flagrante delito, desastre, socorro ou, durante o dia, por ordem judicial (art. 5º, XI).",
], ["CF:5","CF:6","CF:12","CF:14","CF:60"], ["SV-11","SV-14"]),

T("Organização do Estado", """
O Brasil é uma federação formada pela união indissolúvel de Estados, Municípios e Distrito Federal, todos autônomos (arts. 1º e 18). Autonomia significa capacidade de auto-organização, autogoverno, autoadministração e autolegislação, distinta da soberania, que pertence à República Federativa do Brasil.

A repartição de competências segue a predominância do interesse. A União tem competências materiais exclusivas (art. 21) e legislativas privativas (art. 22, delegáveis aos Estados por lei complementar). Há competência material comum a todos os entes (art. 23) e legislativa concorrente entre União, Estados e DF (art. 24), em que a União edita normas gerais e os Estados suplementam. Os Municípios legislam sobre assuntos de interesse local e suplementam a legislação federal e estadual no que couber (art. 30).

A intervenção federal é medida excepcional, cabível apenas nas hipóteses taxativas do art. 34, e a criação de novos Estados e Municípios depende de plebiscito e de lei, nos termos do art. 18.
""", [
 "Forma federativa é cláusula pétrea (art. 60, § 4º, I).",
 "Competências privativas da União: art. 22, delegáveis por lei complementar (parágrafo único).",
 "Competência concorrente: União edita normas gerais; inexistindo lei federal, os Estados exercem competência plena (art. 24, § 3º).",
 "Municípios: interesse local (art. 30, I).",
 "Intervenção federal: hipóteses taxativas do art. 34.",
], [
 "Direito civil, penal, processual e do trabalho são privativos da União (art. 22, I).",
 "Horário de funcionamento do comércio local é de competência municipal (Súmula Vinculante 38).",
 "Superveniência de lei federal sobre normas gerais suspende a eficácia da lei estadual no que lhe for contrário (art. 24, § 4º).",
], ["CF:1","CF:18","CF:21","CF:22","CF:23","CF:24","CF:30","CF:34"], ["SV-38"]),

T("Controle de Constitucionalidade", """
O controle de constitucionalidade verifica a compatibilidade de leis e atos normativos com a Constituição. O Brasil adota sistema misto: difuso (qualquer juiz ou tribunal, no caso concreto, com efeitos em regra inter partes) e concentrado (no STF, por ação direta, com efeitos erga omnes e vinculantes).

As ações do controle concentrado no STF são a ADI (lei ou ato normativo federal ou estadual), a ADC (lei federal, exige controvérsia judicial relevante), a ADO (omissão) e a ADPF (subsidiária, admite lei municipal e direito pré-constitucional). Os legitimados estão no art. 103 — parte deles precisa demonstrar pertinência temática.

Nos tribunais, só a maioria absoluta dos membros ou do órgão especial pode declarar a inconstitucionalidade (cláusula de reserva de plenário, art. 97), regra reforçada pela Súmula Vinculante 10. O STF pode modular os efeitos da decisão por 2/3 dos membros, por razões de segurança jurídica ou excepcional interesse social.
""", [
 "Controle difuso: qualquer juízo, incidental, efeitos inter partes em regra.",
 "Controle concentrado: ADI, ADC, ADO e ADPF no STF (art. 102, I, a, e § 1º).",
 "Legitimados: art. 103 — governadores, mesas de assembleias e confederações sindicais precisam de pertinência temática.",
 "Reserva de plenário: art. 97 e Súmula Vinculante 10.",
 "Modulação de efeitos: 2/3 dos ministros (Lei 9.868/1999, art. 27).",
 "ADPF é subsidiária: só cabe se não houver outro meio eficaz (Lei 9.882/1999, art. 4º, § 1º).",
], [
 "Lei municipal em face da Constituição Federal não pode ser objeto de ADI no STF, mas cabe ADPF.",
 "Normas anteriores à Constituição não são declaradas inconstitucionais, mas não recepcionadas.",
 "Decisão em ADI e ADC tem eficácia contra todos e efeito vinculante para o Judiciário e a Administração (art. 102, § 2º).",
], ["CF:97","CF:102","CF:103","L9868:27","L9882:4"], ["SV-10"]),

T("Poder Judiciário", """
O Poder Judiciário tem por função típica julgar, aplicando o direito com força de definitividade. Seus órgãos estão no art. 92: STF, CNJ, STJ, TST, tribunais e juízes federais, do trabalho, eleitorais, militares e dos Estados e do DF. O CNJ é órgão de controle administrativo e financeiro, sem função jurisdicional.

As garantias da magistratura asseguram independência: vitaliciedade (adquirida após 2 anos de exercício no primeiro grau), inamovibilidade e irredutibilidade de subsídio (art. 95). Há também vedações, como exercer outro cargo salvo um de magistério e dedicar-se a atividade político-partidária.

O STF é o guardião da Constituição (art. 102), com competência originária, recursal ordinária e extraordinária; o STJ uniformiza a interpretação da lei federal (art. 105), especialmente pelo recurso especial. A Reforma do Judiciário (EC 45/2004) criou o CNJ, a súmula vinculante e a repercussão geral.
""", [
 "Órgãos do Judiciário: art. 92.",
 "Garantias dos magistrados: vitaliciedade, inamovibilidade e irredutibilidade (art. 95).",
 "Quinto constitucional nos TRFs e TJs (art. 94).",
 "Súmula vinculante: aprovação por 2/3 do STF, após reiteradas decisões (art. 103-A).",
 "Repercussão geral como requisito do recurso extraordinário (art. 102, § 3º).",
 "CNJ: controle administrativo e financeiro do Judiciário (art. 103-B).",
], [
 "CNJ não tem competência sobre o STF nem função jurisdicional.",
 "Recurso extraordinário cabe contra decisão de única ou última instância, inclusive de turma recursal (Súmula 640 do STF); recurso especial não cabe contra turma recursal (Súmula 203 do STJ).",
 "Reexame de prova não cabe em recurso especial (Súmula 7 do STJ) nem extraordinário (Súmula 279 do STF).",
], ["CF:92","CF:93","CF:94","CF:95","CF:102","CF:103-A","CF:103-B","CF:105"], ["STJ-SUM-7","STF-SUM-279","STJ-SUM-203","STF-SUM-640"]),

T("Processo Legislativo", """
O processo legislativo compreende a elaboração de emendas à Constituição, leis complementares, leis ordinárias, leis delegadas, medidas provisórias, decretos legislativos e resoluções (art. 59). O procedimento ordinário tem fase introdutória (iniciativa), constitutiva (deliberação parlamentar e sanção ou veto) e complementar (promulgação e publicação).

A iniciativa pode ser geral, concorrente, privativa (por exemplo, do Presidente da República nas matérias do art. 61, § 1º) ou popular (1% do eleitorado nacional, distribuído por pelo menos cinco Estados). O vício de iniciativa não é sanado pela sanção. Lei complementar exige maioria absoluta; lei ordinária, maioria simples.

As emendas constitucionais exigem proposta de 1/3 dos membros de uma das Casas, do Presidente ou de mais da metade das Assembleias Legislativas, aprovação em dois turnos em cada Casa por 3/5 e respeito às limitações materiais (cláusulas pétreas), circunstanciais (intervenção federal, estado de defesa ou de sítio) e formais. Medidas provisórias valem por 60 dias, prorrogáveis por mais 60, e não podem tratar das matérias do art. 62, § 1º.
""", [
 "Espécies normativas: art. 59.",
 "Iniciativa popular: 1% do eleitorado, em 5 Estados, com 0,3% em cada (art. 61, § 2º).",
 "Lei complementar: maioria absoluta (art. 69).",
 "Emenda constitucional: 3/5, dois turnos, em cada Casa (art. 60, § 2º).",
 "Medida provisória: 60 + 60 dias; trancamento de pauta após 45 dias (art. 62).",
 "Veto: 15 dias úteis; derrubada por maioria absoluta em sessão conjunta (art. 66).",
], [
 "A sanção não convalida vício de iniciativa.",
 "Matéria de PEC rejeitada não pode ser reapresentada na mesma sessão legislativa (art. 60, § 5º).",
 "Medida provisória não pode tratar de direito penal, processual penal e processual civil, entre outros (art. 62, § 1º).",
], ["CF:59","CF:60","CF:61","CF:62","CF:64","CF:66","CF:69"]),
],

"administrativo": [
T("Atos Administrativos", """
Ato administrativo é a manifestação unilateral de vontade da Administração, no exercício de prerrogativas públicas, sob regime de direito público e sujeita a controle judicial. Seus elementos (requisitos de validade) são competência, finalidade, forma, motivo e objeto. Competência, finalidade e forma são vinculados; motivo e objeto podem ser discricionários, compondo o mérito administrativo.

Os atributos do ato são a presunção de legitimidade e veracidade, a imperatividade, a autoexecutoriedade e a tipicidade. Pela teoria dos motivos determinantes, a validade do ato fica vinculada aos motivos indicados como seu fundamento: se forem falsos ou inexistentes, o ato é nulo.

O ato se extingue por anulação (vício de legalidade, com efeitos retroativos, pela Administração ou pelo Judiciário), revogação (conveniência e oportunidade, apenas pela Administração e com efeitos prospectivos) e cassação (descumprimento de condições pelo beneficiário). O direito de anular atos favoráveis decai em 5 anos, salvo má-fé.
""", [
 "Elementos: competência, finalidade, forma, motivo e objeto.",
 "Mérito administrativo = conveniência e oportunidade (motivo e objeto nos atos discricionários).",
 "Autotutela: anular atos ilegais e revogar inconvenientes (Súmula 473 do STF).",
 "Decadência de 5 anos para anular atos favoráveis, salvo má-fé (Lei 9.784/1999, art. 54).",
 "Convalidação de vícios sanáveis (Lei 9.784/1999, art. 55).",
], [
 "O Judiciário controla a legalidade, mas não revoga atos de outro Poder por conveniência.",
 "Atos vinculados não podem ser revogados.",
 "A LINDB exige considerar as consequências práticas da decisão que invalida ato (art. 21).",
], ["L9784:50","L9784:53","L9784:54","L9784:55","LINDB:20","LINDB:21"], ["STF-SUM-473","STF-SUM-346"]),

T("Licitações e Contratos", """
A Lei 14.133/2021 é o regime geral de licitações e contratos administrativos, tendo substituído as Leis 8.666/1993, 10.520/2002 e o RDC. As modalidades são pregão, concorrência, concurso, leilão e diálogo competitivo; deixaram de existir a tomada de preços e o convite.

A licitação segue, em regra, a sequência: preparatória, divulgação do edital, apresentação de propostas e lances, julgamento, habilitação, recursos e homologação — com a habilitação depois do julgamento. Os critérios de julgamento incluem menor preço, maior desconto, melhor técnica ou conteúdo artístico, técnica e preço, maior lance e maior retorno econômico.

A contratação direta ocorre por inexigibilidade (inviabilidade de competição, art. 74) ou dispensa (competição possível, mas a lei autoriza não licitar, art. 75). Os contratos administrativos têm cláusulas exorbitantes, como a alteração e a extinção unilaterais, a fiscalização e a aplicação de sanções, sempre preservado o equilíbrio econômico-financeiro.
""", [
 "Modalidades: pregão, concorrência, concurso, leilão e diálogo competitivo (Lei 14.133/2021, art. 28).",
 "Fases em regra: julgamento antes da habilitação (art. 17).",
 "Inexigibilidade: competição inviável (art. 74). Dispensa: hipóteses legais (art. 75).",
 "Prerrogativas da Administração no contrato (art. 104).",
 "Restabelecimento do equilíbrio econômico-financeiro (art. 124, II, d).",
], [
 "Tomada de preços e convite não existem mais na Lei 14.133/2021.",
 "Pregão cabe para bens e serviços comuns, inclusive serviços comuns de engenharia.",
 "Licitação dispensada (alienações, art. 76) é diferente de licitação dispensável (art. 75).",
], ["LLC:5","LLC:6","LLC:17","LLC:28","LLC:33","LLC:74","LLC:75","LLC:104","LLC:124"]),

T("Servidores Públicos", """
Os agentes públicos abrangem agentes políticos, servidores (estatutários, empregados públicos e temporários) e particulares em colaboração. O acesso aos cargos e empregos públicos depende de aprovação prévia em concurso público, ressalvados os cargos em comissão, de livre nomeação e exoneração (art. 37, II).

No âmbito federal, o regime estatutário é disciplinado pela Lei 8.112/1990. A estabilidade é adquirida após 3 anos de efetivo exercício, com avaliação especial de desempenho, e o servidor estável só perde o cargo por sentença transitada em julgado, processo administrativo com ampla defesa ou avaliação periódica de desempenho (art. 41).

A acumulação de cargos públicos é vedada, salvo as exceções constitucionais com compatibilidade de horários: dois de professor; um de professor com outro técnico ou científico; dois privativos de profissionais de saúde com profissões regulamentadas. O teto remuneratório é o subsídio dos ministros do STF.
""", [
 "Concurso público obrigatório, salvo cargos em comissão (CF, art. 37, II).",
 "Estabilidade: 3 anos + avaliação especial de desempenho (CF, art. 41).",
 "Acumulação de cargos: hipóteses do art. 37, XVI.",
 "Teto remuneratório: art. 37, XI.",
 "PAD: processo administrativo disciplinar com contraditório (Lei 8.112/1990, art. 143 e seguintes).",
], [
 "Ausência de advogado no processo administrativo disciplinar não ofende a Constituição (Súmula Vinculante 5).",
 "Nomeação de parentes até o 3º grau para cargo em comissão viola a Constituição — nepotismo (Súmula Vinculante 13).",
 "Investidura sem concurso em cargo de carreira diversa é inconstitucional (Súmula Vinculante 43).",
], ["CF:37","CF:39","CF:41","L8112:20","L8112:143"], ["SV-5","SV-13","SV-43"]),

T("Responsabilidade Civil do Estado", """
A responsabilidade civil do Estado é objetiva, fundada na teoria do risco administrativo (CF, art. 37, § 6º): pessoas jurídicas de direito público e as de direito privado prestadoras de serviço público respondem pelos danos que seus agentes, nessa qualidade, causarem a terceiros, independentemente de culpa. Basta comprovar conduta, dano e nexo causal.

O risco administrativo admite excludentes: culpa exclusiva da vítima, caso fortuito ou força maior e fato exclusivo de terceiro; a culpa concorrente atenua a indenização. Já a teoria do risco integral, que não admite excludentes, aplica-se a hipóteses especiais, como o dano ambiental e o dano nuclear.

Para omissões, a jurisprudência oscila entre a responsabilidade subjetiva (faute du service) e a objetiva quando há dever específico de agir — por exemplo, a morte de detento sob custódia (Tema 592 do STF). A vítima deve acionar o Estado, que tem ação regressiva contra o agente em caso de dolo ou culpa; o STF não admite a ação direta contra o agente (Tema 940).
""", [
 "Responsabilidade objetiva do Estado e das prestadoras de serviço público (CF, art. 37, § 6º).",
 "Prestadora de serviço público responde objetivamente também perante não usuários (Tema 130 do STF).",
 "Teoria da dupla garantia: a ação é contra o Estado; regresso contra o agente por dolo ou culpa (Tema 940).",
 "Morte de detento: responsabilidade do Estado por inobservância do dever de proteção (Tema 592).",
 "Prescrição contra a Fazenda: 5 anos (Decreto 20.910/1932), conforme a jurisprudência do STJ.",
], [
 "Excludentes do risco administrativo: culpa exclusiva da vítima, força maior e fato de terceiro.",
 "Risco integral (sem excludentes) em dano ambiental e nuclear.",
 "O agente público não responde diretamente perante a vítima.",
], ["CF:37","CC:43"], ["STF-RG-130","STF-RG-940","STF-RG-592"]),

T("Poderes Administrativos", """
Os poderes administrativos são instrumentos para que a Administração persiga o interesse público: poder-dever, irrenunciável e limitado pela lei. São eles: vinculado e discricionário (quanto à liberdade de atuação), hierárquico, disciplinar, regulamentar e de polícia.

O poder hierárquico organiza a estrutura interna, permitindo dar ordens, fiscalizar, delegar e avocar. O poder disciplinar permite apurar infrações e aplicar sanções a servidores e a particulares com vínculo especial com a Administração. O poder regulamentar autoriza o chefe do Executivo a expedir decretos para a fiel execução da lei (art. 84, IV), sem inovar na ordem jurídica, salvo o decreto autônomo do art. 84, VI.

O poder de polícia limita o exercício de direitos individuais em benefício do interesse público, com atributos de discricionariedade, autoexecutoriedade e coercibilidade. Pode ser preventivo ou repressivo e se desenvolve em ciclo: ordem, consentimento, fiscalização e sanção. O STF admite a delegação das fases de consentimento, fiscalização e sanção a estatais de direito privado prestadoras de serviço público em regime não concorrencial (Tema 532).
""", [
 "Abuso de poder = excesso de poder (competência) ou desvio de finalidade.",
 "Decreto regulamentar não inova; decreto autônomo apenas nas hipóteses do art. 84, VI.",
 "Delegação e avocação: Lei 9.784/1999, arts. 11 a 17.",
 "Poder de polícia: definição legal no CTN, art. 78.",
 "Ciclo de polícia: ordem, consentimento, fiscalização e sanção.",
], [
 "Não podem ser delegados: edição de atos normativos, decisão de recursos administrativos e matérias de competência exclusiva (Lei 9.784/1999, art. 13).",
 "Guardas municipais podem exercer poder de polícia de trânsito, inclusive aplicar multas previstas em lei (STF, Tema 472).",
 "Poder de polícia pode ser remunerado por taxa (CF, art. 145, II).",
], ["CF:84","CF:145","L9784:11","L9784:13","L9784:15","CTN:78"], ["STF-RG-532","STF-RG-472"]),
],
}
