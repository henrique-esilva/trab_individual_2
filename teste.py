# este é um script de teste para o projeto de análise de dados

from main import *

candidatos.update(
	fernandofernandes=dict_to_str(args_to_dict(2,2,2,3)),
	almerindaneves=dict_to_str(args_to_dict(2,2,3,3)),
	alexchaves=dict_to_str(args_to_dict(2,3,3,3)),
	nandomoura=dict_to_str(args_to_dict(3,3,3,3)),
	juliamota=dict_to_str(args_to_dict(7,6,6,7)),
)

print(filtrar_por_notas([8,6,6,3]))
