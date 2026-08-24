# Módulo 01 · Fundamentos de Python

**Capacitação Introdutória de Ciência de Dados · FEA.dev**

---

## Contexto

Este é o módulo mais longo da capacitação, e o único que não trata de dados diretamente.
Ele constrói a base: como guardar valores, tomar decisões, repetir tarefas, organizar
informação em coleções e empacotar lógica em funções.

A tentação de pular direto para o pandas é grande e é um erro. Praticamente todo problema
que trainees enfrentam no módulo 02 tem raiz aqui — um `for` mal entendido, a confusão
entre `return` e `print`, a diferença entre uma lista e um dicionário. O tempo investido
neste módulo é recuperado com juros no seguinte.

Os exemplos são de finanças desde a primeira aula, mas nada aqui exige conhecimento
prévio da área.

## Notebooks

| # | Notebook | Conteúdo | Tempo |
|---|---|---|---|
| 1 | [`01_sintaxe_tipos_operadores.ipynb`](01_sintaxe_tipos_operadores.ipynb) | Variáveis, convenções de nome, tipos (`int`, `float`, `str`, `bool`, `None`), operadores, conversão, f-strings | 60 min |
| 2 | [`02_estruturas_de_controle.ipynb`](02_estruturas_de_controle.ipynb) | `if`/`elif`/`else`, indentação, `for`, `while`, `range`, `enumerate`, `zip`, `break`, `continue` | 60 min |
| 3 | [`03_estruturas_de_dados.ipynb`](03_estruturas_de_dados.ipynb) | Listas, compreensões, dicionários, tuplas, conjuntos, escolha da estrutura, referências × cópias | 70 min |
| 4 | [`04_funcoes_e_escopo.ipynb`](04_funcoes_e_escopo.ipynb) | `def`, parâmetros e argumentos, **`return` × `print`**, valores padrão, docstrings, escopo local e global, `lambda` | 60 min |

**Tempo total estimado:** 4h10

## Exercícios

[`04_Exercicios/lista_01_fundamentos.ipynb`](../04_Exercicios/lista_01_fundamentos.ipynb)
— 16 exercícios, cerca de 2h30. É a lista mais importante da capacitação.

## Ao final deste módulo você deve conseguir

- escrever e depurar um programa de algumas dezenas de linhas;
- escolher entre lista, dicionário, tupla e conjunto para cada situação;
- explicar a diferença entre `return` e `print` e quando usar cada um;
- escrever funções com docstring, parâmetros nomeados e valores padrão;
- entender por que uma variável criada dentro de uma função não existe fora dela.

## Conceitos que costumam travar

| Ponto | Onde está tratado |
|---|---|
| `=` atribui, `==` compara | Aula 1, seção 4 |
| `float` é aproximado (`0.1 + 0.2 != 0.3`) | Aula 1, seção 2 |
| Indentação é sintaxe, não estética | Aula 2, seção 2 |
| A ordem das condições em `if`/`elif` muda o resultado | Aula 2, seção 1 |
| `sorted()` devolve cópia; `.sort()` altera no lugar | Aula 3, seção 1 |
| Atribuir uma lista a outra variável não copia | Aula 3, seção 7 |
| `return` devolve; `print` só mostra | Aula 4, seção 3 |

## Bibliografia e leituras

- [Tutorial oficial do Python (em português)](https://docs.python.org/pt-br/3/tutorial/) — a referência
- Downey, A. *Pense em Python* — [versão livre em português](https://penseallen.github.io/PensePython2e/)
- [PEP 8 — guia de estilo](https://peps.python.org/pep-0008/) — a origem do `snake_case` e das demais convenções
- Matthes, E. *Curso Intensivo de Python*, Novatec — capítulos 2 a 8

## Palavras-chave

`variável` · `tipo` · `int` · `float` · `str` · `bool` · `None` · `operador` · `f-string`
· `condicional` · `indentação` · `loop` · `range` · `enumerate` · `zip` · `lista`
· `compreensão de lista` · `dicionário` · `tupla` · `conjunto` · `função` · `parâmetro`
· `argumento` · `return` · `docstring` · `escopo` · `lambda`
