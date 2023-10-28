# Projeto individual Análise de Dados módulo 2

Este projeto foi feito com o intuito de satisfazer as entregas nessessárias ao módulo 2 do curso de Análise de Dados do Senac. O objetivo é fornecer um conjunto de funções que seja capaz de filtrar uma série de dados acerca de participantes de um processo seletivo. 

## 🚀 Começando

### Contexto

Para este projeto, foi pedido o desenvolvimento de uma ferramenta em Python que fosse capaz de ler e filtrar conjuntos de dados recebidos, estando cada conjunto contido em um padrão de texto.

Recebendo um conjunto de dados referentes a candidatos de um processo seletivo fictício, o programa deve ser capaz de reconhecer cada nota, bem como a avaliação a qual esta se refere.

Os dados devem ficar armazenados em um dicionário onde as chaves são identificadores dos participantes e os valores são as notas.

Assim:
```
participante_1 : notas_do_p1
participante_2 : notas_do_p2
participante_3 : notas_do_p3
...
```

### Padrão das notas

As notas dos participantes estarão em uma string de texto no formato eX_tX_pX_sX, onde cada letra 'X' é substituída por um número inteiro correspondente à nota na avaliação indicada pela letra precedente. Abaixo uma legenda das avaliações.

* e - entrevista;
* t - teste teórico;
* p - teste prático;
* s - avaliação de soft skills;

Assim sendo, a string 'e8_t10_p7_s3' designa nota 8 na entrevista, 10 no teste teórico, 7 no teste prático e 3 em soft skills.

Exemplos de strings válidas neste formato:

* 'e7_t8_p9_s10';
* 'e0_t0_p0_s0';
* 'e100_t200_p300_s1000';
* 'e4_t4_p4_s4';

Exemplos de strings inválidas para este formato:

* 't9_p4_s4';
* 'e4t4p4s4';

No próprio arquivo main.py existe um dicionário com os dados padrão para fins de teste e ao final um exemplo de uso das funções definidas ao longo do código.

O arquivo main.py contém algumas variáveis e funções necessárias para o funcionamento da filtragem de candidatos. A variável `candidatos` é um dicionário com alguns valores fictícios para fins de teste.

### 📋 Pré-requisitos

Para rodar o programa main.py você precisará ter instalado o interpretador Python na versão 3.x ou mais recente.

Visite a [página de downloads oficial do python](https://www.python.org/downloads/) para obter o interpretador do python.

### 🔧 Instalação

Não é necessária instalação desta biblioteca. Apenas clone o repositório e salve o arquivo main.py na pasta em que for usar. Mude o nome caso seja conveniente.

```
git clone git@github.com:henrique-esilva/trab_individual_2
```
Isto lhe fornecerá uma cópia deste repositório em sua máquina.

#### importação

Para usar as funções definidas no arquivo main.py, você terá que copiá-lo para a pasta onde estiver trabalhando.
Ex.: se estiver trabalhando na pasta `C:/users/user/scripts`, o arquivo deverá ser salvo como: `C:/users/user/scripts/main.py`.

É possível que você já tenha um arquivo `main.py` em sua pasta. Recomendo mudar o nome do arquivo copiado para algo mais discreto, que não interfira em seu trabalho.

Que tal `filtra_notas.py`? Neste caso o arquivo ficaria salvo como `C:/users/user/scripts/filtra_notas.py` ou algo de sua preferência.

##### import

Tendo uma cópia do arquivo na sua pasta, importe o módulo em outro arquivo Python na mesma pasta. Em seu código faça:

```
import main
```
Substitua 'main' pelo nome que você salvou o arquivo, caso tenha mudado. Para importar, não escreva a extensão .py no código.

Após importar, você poderá acessar e usar as funções do módulo importado durante o restante da execução do código usando a seguinte sintaxe: nome do módulo importado, ponto, seguido pelo nome da variável ou função que quer acessar.
`main.function_or_variable`

##### from import

Se não quiser usar 'main.algumacoisa' toda vez que for acessar uma variável, você pode importar tudo diretamente usando
```
from main import *
```
Desse jeito, as variáveis serão importadas diretamente. Assim, em vez de main.nomeDaFunção, use apenas nomeDaFunção no restante do código.

Em main.py são definidas algumas funções.
* str_to_dict
* args_to_dict
* dict_to_str
* filtrar_por_notas

Para ver as documentações das funções, use a função `help()` na CLI do Python ou num arquivo depois de importar o `main.py`. Exemplo na CLI Python:
```
>>> from main import *
{'candidato 1': 'e5_t10_p8_s8', 'candidato 5': 'e10_t10_p8_s9'}
pressione ENTER para encerrar
>>> help(str_to_dict)
Help on function str_to_dict in module main:

str_to_dict(arg: str)
    Retorna as notas em formato de dicionário.
    Forneça uma string no formato "eX_tX_pX_sX"
    onde cada X é substituído por um número correspondente
    à nota em cada avaliação indicada pela letra anterior
```

## Usando na prática

Para filtrar um conjunto de candidatos, armazene os canidatos em um dicionário. Este dicionário deve estar no formato {candidato: notas}, onde 'candidato' é um identificador qualquer, podendo ser uma string de texto, um inteiro, desde que não hajam identificadores duplicados. 'notas' deve ser uma string no formato padrão citado anteriormente [aqui](/README.md#padrão-das-notas).
Use a função filtrar_por_notas() que está no módulo `main.py` fornecendo como argumentos:
* uma lista ou tupla contendo as notas de corte; e
* o dicionário onde estão armazenados os candidatos e suas notas.

Observe que:
* As notas devem estar numa TUPLA ou LISTA
* Elas devem ser apenas quatro números inteiros
* Usar números de ponto flutuante não resultará em erro, mas algmas partes do módulo transformam as notas em inteiros, fazendo com que a parte decimal se perca
* As notas devem estar na seguinte ordem: (entrevista, teste teórico, teste prático, soft skills) é pela ordem que a função identificará as notas
* Foneça um dicionário com as notas formatadas. Para formatar notas, use as funções `dict_to_str` e `args_to_dict`
* Ao não fornecer um dicionário, será usado o dicionário de teste definido no módulo `main.py`

A função retornará um dicionário {candidato: notas} com todos os candidatos no dicionário fornecido cujas notas forem iguais ou maiores que as notas de corte correspondentes.

### Exemplo
```
meus_candidatos = {
    'helena': dict_to_str(args_to_dict(10,10,10,10)),
    'ramon': dict_to_str(args_to_dict(5,10,10,10)),
    'joseilson': dict_to_str(args_to_dict(5,5,10,10))
}
filtrar_por_notas([5, 10, 10, 10], meus_candidatos)
```
Saída:
```
{'helena': 'e10_t10_p10_s10', 'ramon': 'e5_t10_p10_s10'}
```

## 🛠️ Construído com

* [Python](https://www.python.org/) - Linguagem de programação utilizada

## ✒️ Autores

* **henrique-esilva** - *Trabalho Inicial* - [henrique-esilva](https://github.com/henrique-esilva)

## 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

## 🎁 Meus agradecimentos a:

Meus colegas do curso:
* Drielli, que me ensinou a usar o codespace do GitHub
* Isabele e Bea, pela ideia de buscar um template para o README
Meus professores:
* Douglas, sempre muito solícito
* Diogo Guimarães, uma rocha de paciência e saber, mestre e amigo
E também a:
* A comunidade Python, pelo conteúdo e ferramentas grátis
* A equipe da Resília e do Senac pela oportunidade de estudar Análise de Dados <3
---
⌨️ Este MarkDown foi feito a partir de um template de [Armstrong Lohãns](https://gist.github.com/lohhans) 😊 muito obrigado, Armstrong =^-^=
