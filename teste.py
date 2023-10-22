# este é um script de teste para o projeto de análise de dados

import main

main.candidatos.update(
	fernandofernandes=main.get_formated(main.get_dict([2,2,2,3])),
	almerindaneves=main.get_formated(main.get_dict([2,2,3,3])),
	alexchaves=main.get_formated(main.get_dict([2,3,3,3])),
	nandomoura=main.get_formated(main.get_dict([3,3,3,3])),
	juliamota=main.get_formated(main.get_dict([7,6,6,7])),
)

print(main.filtrar_por_notas([2,2,3,3], main.candidatos))
