# Módulo 03 · Visualização e Análise Exploratória

**Capacitação Introdutória de Ciência de Dados · FEA.dev**

---

## Contexto

Uma tabela com dez mil linhas não cabe na cabeça de ninguém; um gráfico, sim. Este módulo
ensina a produzir gráficos que comunicam, os números que os sustentam e — o mais
importante — o **processo** que transforma tudo isso em análise.

A última aula é o centro da capacitação. Ela percorre quatro ciclos completos de
pergunta → exploração → descoberta → hipótese sobre dados reais, incluindo um ciclo em que
a hipótese inicial **não se confirma**. Isso é deliberado: uma análise honesta registra o
que não funcionou, e saber conduzir esse momento é o que distingue análise de coleção de
gráficos.

O módulo também insiste em um ponto que atravessa toda a área: estatística descritiva
descreve o passado observado. Não é previsão.

## Notebooks

| # | Notebook | Conteúdo | Tempo |
|---|---|---|---|
| 1 | [`01_matplotlib.ipynb`](01_matplotlib.ipynb) | Figura e eixos, linha, barras, histograma, dispersão, rótulos, painéis, exportação, erros comuns | 60 min |
| 2 | [`02_seaborn.ipynb`](02_seaborn.ipynb) | `set_theme`, `histplot`, `boxplot`, `barplot`, `countplot`, `scatterplot`, `regplot`, `lineplot`, `heatmap`, `pairplot`, `hue` | 60 min |
| 3 | [`03_estatistica_descritiva.ipynb`](03_estatistica_descritiva.ipynb) | Média × mediana, desvio padrão, IQR, coeficiente de variação, quantis, VaR, assimetria, outliers, correlação | 60 min |
| 4 | [`04_processo_de_eda.ipynb`](04_processo_de_eda.ipynb) | O ciclo da EDA em quatro voltas, teste de robustez, síntese, checklist e armadilhas | 90 min |

**Tempo total estimado:** 4h30

## Exercícios

[`04_Exercicios/lista_03_visualizacao.ipynb`](../04_Exercicios/lista_03_visualizacao.ipynb)
— 11 exercícios, cerca de 2h30, terminando em um ciclo completo de EDA feito por você.

## Ao final deste módulo você deve conseguir

- escolher o gráfico adequado a cada tipo de pergunta;
- produzir gráficos que outra pessoa entenda em dez segundos, sem você explicando;
- escolher entre média e mediana, e justificar a escolha;
- interpretar uma correlação — inclusive para dizer o que ela **não** significa;
- conduzir uma análise exploratória completa, com síntese e limitações declaradas.

## Conceitos que costumam travar

| Ponto | Onde está tratado |
|---|---|
| A escolha do que plotar é decisão analítica (nível × base 100) | Aula 1, seção 2 |
| Painéis com escalas diferentes não são comparáveis | Aula 1, seção 6 |
| `barplot` mostra a **média** por padrão | Aula 2, seção 3 |
| Média × mediana em distribuições assimétricas | Aula 3, seção 1 |
| Outlier não é erro | Aula 3, seção 4 |
| Correlação mede relação **linear** — sempre olhe o gráfico | Aula 3, seção 5 |
| Correlação não é causalidade | Aula 3, seção 5 |
| Descoberta que depende de um único ponto é artefato | Aula 4, ciclo 2 |

## Bibliografia e leituras

- Tukey, J. W. *Exploratory Data Analysis*, 1977 — o livro que criou o campo
- Wilke, C. *Fundamentals of Data Visualization* — [versão livre online](https://clauswilke.com/dataviz/)
- Healy, K. *Data Visualization: A Practical Introduction* — [versão livre online](https://socviz.co/)
- [Documentação do Seaborn — tutorial](https://seaborn.pydata.org/tutorial.html)
- [Matplotlib — guia de início rápido](https://matplotlib.org/stable/users/explain/quick_start.html)
- Huff, D. *Como Mentir com Estatística* — curto, antigo e ainda atual sobre gráficos enganosos

## Palavras-chave

`figura` · `eixos` · `gráfico de linha` · `barras` · `histograma` · `dispersão`
· `boxplot` · `mapa de calor` · `painel` · `hue` · `paleta` · `média` · `mediana`
· `moda` · `desvio padrão` · `variância` · `IQR` · `quantil` · `percentil` · `VaR`
· `assimetria` · `outlier` · `correlação` · `Pearson` · `Spearman` · `causalidade`
· `EDA` · `robustez`
