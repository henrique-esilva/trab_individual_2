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
str_to_dict
args_to_dict
dict_to_str
filtrar_por_notas

Para ver as documentações das funções, use a função `help()` na CLI do Python ou num arquivo depois de importar o `main.py`. Exemplo:
```
>>> from main import *
[4, 4, 8, 8] dict_values([5, 10, 8, 8])
[4, 4, 8, 8] dict_values([10, 7, 7, 8])
[4, 4, 8, 8] dict_values([8, 5, 4, 9])
[4, 4, 8, 8] dict_values([2, 2, 2, 1])
[4, 4, 8, 8] dict_values([10, 10, 8, 9])
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

## ⚙️ Executando os testes

Explicar como executar os testes automatizados para este sistema.

### 🔩 Analise os testes de ponta a ponta

Explique que eles verificam esses testes e porquê.

```
Dar exemplos
```

### ⌨️ E testes de estilo de codificação

Explique que eles verificam esses testes e porquê.

```
Dar exemplos
```

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [Python](https://www.python.org/) - Linguagem de programação utilizada

## 🖇️ Colaborando

Por favor, leia o [COLABORACAO.md](https://gist.github.com/usuario/linkParaInfoSobreContribuicoes) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.


## ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

* **henrique-esilva** - *Trabalho Inicial* - [henrique-esilva](https://github.com/henrique-esilva)
* **Fulano De Tal** - *Documentação* - [fulanodetal](https://github.com/linkParaPerfil)

## 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

## 🎁 Expressões de gratidão

* Conte a outras pessoas sobre este projeto 📢;
* Convide alguém da equipe para uma cerveja 🍺;
* Um agradecimento publicamente 🫂;
* etc.


---
⌨️ com ❤️ por [Armstrong Lohãns](https://gist.github.com/lohhans) 😊
