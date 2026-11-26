# Helpers para os modelos de peças do Lex Unum (conteúdo autoral).
def P(id, nome, grupo, cabimento, prazo, fundamento, requisitos, dicas, modelo, artigos=()):
    return {"id": id, "nome": nome, "area": grupo, "grupo": grupo, "cabimento": cabimento.strip(), "prazo": prazo,
            "fundamento": fundamento, "requisitos": list(requisitos), "dicas": list(dicas),
            "modelo": modelo.strip("\n"), "artigos": list(artigos)}

def PF(papel):
    return (f"[NOME COMPLETO DO(A) {papel}], [nacionalidade], [estado civil], [profissão], portador(a) da "
            f"Cédula de Identidade RG nº [número], inscrito(a) no CPF sob o nº [número], residente e domiciliado(a) "
            f"na [endereço completo, CEP], endereço eletrônico [e-mail]")

def PJ(papel):
    return (f"[RAZÃO SOCIAL DO(A) {papel}], pessoa jurídica de direito privado, inscrita no CNPJ sob o nº [número], "
            f"com sede na [endereço completo, CEP], endereço eletrônico [e-mail], neste ato representada por [nome e cargo do representante]")

ADV = ("por seu(sua) advogado(a) que esta subscreve (procuração anexa), com escritório profissional na "
       "[endereço completo], onde recebe intimações")

FECHO = """Termos em que,
pede deferimento.

[Local], [data].

[Nome do(a) advogado(a)]
OAB/[UF] nº [número]"""

JUIZO_CIVEL = "AO JUÍZO DE DIREITO DA ___ VARA CÍVEL DA COMARCA DE [CIDADE/UF]"
JUIZO_FAMILIA = "AO JUÍZO DE DIREITO DA ___ VARA DE FAMÍLIA E SUCESSÕES DA COMARCA DE [CIDADE/UF]"
JUIZO_CRIMINAL = "AO JUÍZO DE DIREITO DA ___ VARA CRIMINAL DA COMARCA DE [CIDADE/UF]"
JUIZO_TRABALHO = "AO JUÍZO DA ___ VARA DO TRABALHO DE [CIDADE/UF]"
JUIZO_FAZENDA = "AO JUÍZO DE DIREITO DA ___ VARA DA FAZENDA PÚBLICA DA COMARCA DE [CIDADE/UF]"
JUIZO_FEDERAL = "AO JUÍZO FEDERAL DA ___ VARA FEDERAL DA SEÇÃO JUDICIÁRIA DE [UF]"
PROC = "Processo nº [número]"
