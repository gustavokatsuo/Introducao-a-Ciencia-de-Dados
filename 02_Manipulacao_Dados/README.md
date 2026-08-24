# Módulo 02 · Manipulação de Dados

**Capacitação Introdutória de Ciência de Dados · FEA.dev**

---

## Contexto

Aqui começa a ciência de dados propriamente dita. O módulo apresenta as duas bibliotecas
que sustentam todo o ecossistema Python de dados — **NumPy** e **pandas** — e ensina o
trabalho que ocupa a maior parte do tempo de qualquer projeto real: carregar, selecionar,
filtrar, agrupar, cruzar e limpar.

A última aula, sobre limpeza, é a que costuma ser pulada em cursos introdutórios e a que
mais separa quem sabe usar as ferramentas de quem sabe fazer análise. Ela usa uma base
propositalmente suja, com os defeitos que aparecem em dados reais: valores faltantes,
duplicatas, números salvos como texto, datas em formatos misturados e categorias
inconsistentes.

Todos os dados usados estão em [`data/`](../data) e vêm do mercado brasileiro — cinco
anos de cotações da B3 e indicadores do Banco Central.

## Notebooks

| # | Notebook | Conteúdo | Tempo |
|---|---|---|---|
| 1 | [`01_numpy.ipynb`](01_numpy.ipynb) | Arrays, vetorização, indexação, máscaras booleanas, agregações, `axis`, `NaN`, retornos e volatilidade | 60 min |
| 2 | [`02_pandas_series_dataframes.ipynb`](02_pandas_series_dataframes.ipynb) | Series e DataFrames, leitura de CSV e Excel, inspeção, seleção, **`.loc` × `.iloc`**, índice, criação de colunas | 75 min |
| 3 | [`03_filtros_e_agrupamentos.ipynb`](03_filtros_e_agrupamentos.ipynb) | Filtros compostos, `isin`, `between`, `.str`, `query`, `.dt`, `groupby`, `.agg`, `pivot_table` | 75 min |
| 4 | [`04_merge_e_limpeza.ipynb`](04_merge_e_limpeza.ipynb) | `concat`, `merge` e seus tipos, validação de junções, faltantes, duplicatas, tipos, categorias, valores impossíveis | 80 min |

**Tempo total estimado:** 4h50

## Exercícios

[`04_Exercicios/lista_02_manipulacao.ipynb`](../04_Exercicios/lista_02_manipulacao.ipynb)
— 14 exercícios sobre os dados reais, cerca de 2h30.

## Ao final deste módulo você deve conseguir

- abrir uma base que você nunca viu e descrever o que há nela em cinco minutos;
- selecionar linhas e colunas com `.loc` e `.iloc`, sabendo qual usar em cada caso;
- responder perguntas de negócio com `groupby` e `pivot_table`;
- cruzar tabelas com `merge` e **conferir** se a junção fez o que você esperava;
- identificar e tratar os cinco problemas clássicos de qualidade de dados, justificando
  cada decisão.

## Conceitos que costumam travar

| Ponto | Onde está tratado |
|---|---|
| `axis=0` × `axis=1` | Aula 1, seção 5 |
| Use `&`, `|`, `~` — nunca `and`, `or`, `not` | Aula 1, seção 4 |
| `.loc` usa rótulos, `.iloc` usa posições; a fatia se comporta diferente | Aula 2, seção 6 |
| Métodos devolvem cópias — é preciso reatribuir | Aula 2, seção 8 |
| `groupby` sobre categorias inconsistentes produz resultado errado | Aula 3, seção 5 |
| Todo `merge` precisa de conferência (`shape`, `validate`, `indicator`) | Aula 4, seção 2 |
| Valor impossível não é a mesma coisa que valor extremo | Aula 4, seção 3.5 |
| Atribua sempre com `.loc[mascara, "coluna"] = valor` | Aula 4, seção 3.5 |

## Bibliografia e leituras

- McKinney, W. *Python for Data Analysis*, 3ª ed. — [versão livre online](https://wesmckinney.com/book/), escrita pelo criador do pandas
- [Documentação do pandas — *10 minutes to pandas*](https://pandas.pydata.org/docs/user_guide/10min.html)
- [Documentação do pandas — indexação e seleção](https://pandas.pydata.org/docs/user_guide/indexing.html)
- [Documentação do NumPy — *absolute basics for beginners*](https://numpy.org/doc/stable/user/absolute_beginners.html)
- Wickham, H. *Tidy Data* — [artigo](https://vita.had.co.nz/papers/tidy-data.pdf) sobre o formato em que dados devem ser organizados

## Palavras-chave

`ndarray` · `vetorização` · `broadcasting` · `máscara booleana` · `axis` · `NaN`
· `Series` · `DataFrame` · `índice` · `read_csv` · `read_excel` · `.loc` · `.iloc`
· `dtype` · `filtro` · `isin` · `query` · `.str` · `.dt` · `groupby` · `agg`
· `pivot_table` · `concat` · `merge` · `join` · `validate` · `dados faltantes`
· `duplicatas` · `outlier` · `limpeza de dados`
