#! python3.11

# padrao eX_tX_pX_sX

# uma string de formato padrão para notas
_templateStr = "e{}_t{}_p{}_s{}"
# formato padrão em dicionário
_templateDict = {"e": 0, "t": 0, "p": 0, "s": 0}
# lista de candidatos
candidatos = dict()

def get_crude(arg:str):
	"""\
Retorna as notas em formato de dicionário.
Forneça uma string no formato "eX_tX_pX_sX"
onde cada X é substituído por um número correspondente
à nota em cada avaliação indicada pela letra"""
	return {element[:1]: int(element[1:]) for element in arg.split(sep="_")}


def get_dict(arg:list|tuple):
	a = [i for i in'etps']
	return {key:arg[a.index(key)] for key in a}


def get_formated(arg:dict):
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


def filtrar_por_notas(etps:list|tuple, vetor:dict):
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
		v = get_crude(notas) # try 'with get_crude(notas) as v: [...]' or something like
		if not tuple(etps) > (v['e'], v['p'], v['t'], v['s']):
			aprovados[candidato] = notas
	return aprovados


