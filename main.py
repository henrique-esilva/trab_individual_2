# padrao eX_tX_pX_sX

# dados fictícios de candidato para fins de teste
candidato1 = "e0_t6_p10_s20"
# uma string de formato padrão para notas
_format = "e{}_t{}_p{}_x{}"
# formato padrão em dicionário
_form_dict = {"e": 0, "t": 0, "p": 0, "s": 0}

print(_format)
print( candidato1.split(sep="_") )

def get_crude(arg:str):
	__doc__ = "Retorna as notas em formato de dicionário.\
\nForneça uma string no formato \"eX_tX_pX_sX\"\
\nonde cada X é substituído por um número correspondente\
\nà nota em cada avaliação indicada pela letra"
	return {element[:1]: element[1:] for element in arg.split(sep="_")}
	#return [element[1:] for element in arg.split(sep="_")]


def get_formated(arg:list):
	__doc__ = "Retorna as notas convertidas no formato de string\
\neX_tX_pX_sX onde "
	return _format.format(arg["e"], arg["t"], arg["p"], arg["s"])


def 


print( get_crude(candidato1) )
print( get_formated( get_crude(candidato1) ) )
