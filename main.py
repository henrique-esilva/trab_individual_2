#! python3.11

# padrao eX_tX_pX_sX

# uma string de formato padrão para notas
_templateStr = "e{}_t{}_p{}_s{}"
# formato padrão em dicionário
_templateDict = {"e": 0, "t": 0, "p": 0, "s": 0}
# lista de candidatos
candidatos = {
	'candidato 1': 'e5_t10_p8_s8',
	'candidato 2': 'e10_t7_p7_s8',
	'candidato 3': 'e8_t5_p4_s9',
	'candidato 4': 'e2_t2_p2_s1',
	'candidato 5': 'e10_t10_p8_s9',
}

def str_to_dict(arg:str):
	"""\
Retorna as notas em formato de dicionário.
Forneça uma string no formato "eX_tX_pX_sX"
onde cada X é substituído por um número correspondente
à nota em cada avaliação indicada pela letra anterior"""
	arg = arg.split(sep="_")
	result = _templateDict
	for i in _templateDict:
		for j in arg:
			if j[:1] == i:
				result[i] = int(j[1:])
	return result
	# return {element[:1]: int(element[1:]) for element in arg.split(sep="_")}


def args_to_dict(notaEntrevista,notaTesteTeorico,notaTestePratico,notaSoftSkills):
	"""\
Retorna um dicionário no formato
letra: nota_correspondente
onde
    'letra' é uma string
    'nota_correspondente' é um inteiro
cada letra corresponde a uma nota
    e = entrevista
    t = teste teórico
    p = teste prático
    s = soft skills
Forneça as notas nesta ordem"""
	a = [i for i in'etps']
	notas = [notaEntrevista, notaTesteTeorico, notaTestePratico, notaSoftSkills]
	return {key:notas[a.index(key)] for key in a}


def dict_to_str(arg:dict):
	"""\
Retorna uma string no formato
'eX_tX_pX_sX' onde cada 'X' é a nota obtida na avaliação
indicada pela letra anterior:
    e = entrevista
    t = teste teórico
    p = teste prático
    s = soft skills
Deve receber um dicionário no formato
letra: nota_correspondente
onde
    'letra' deve ser string
    'nota_correspondente' deve ser inteiro
ou uma lista de 4 inteiros correspondentes às notas
na ordem [e, t, p, s]"""
	return _templateStr.format(arg["e"], arg["t"], arg["p"], arg["s"])


def filtrar_por_notas(etps:list|tuple, vetor:dict=candidatos):
	"""\
Forneça uma lista ou tupla de quatro números inteiros
e um dicionário no formato
    candidato: notas
onde
    'candidato' pode ser qualquer tipo e
    'notas' precisa ser uma string no formato eX_tX_pX_sX
    onde cada 'X' é a nota obtida na avaliação indicada pela letra precedente
    esta podendo ser 'e', 'p', 't' ou 's'
Retorna um dicionário contendo apenas os elementos do dicionario fornecido
que possuírem notas todas de valor igual ou superior ao correspondente na
lista ou tupla fornecida."""
	aprovados = {}
	for candidato, notas in vetor.items():
		v = str_to_dict(notas)
		print(etps, v.values())
		if (
      		tuple(etps)[0] <= v['e'] and\
    		tuple(etps)[1] <= v['p'] and\
      		tuple(etps)[2] <= v['t'] and\
            tuple(etps)[3] <= v['s']
        ):
			aprovados[candidato] = notas
	return aprovados


print(filtrar_por_notas([4,4,8,8]))
