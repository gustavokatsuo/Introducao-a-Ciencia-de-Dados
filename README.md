<p align="center">
  <img src="assets/banner.png" width="100%">
</p>

# Introdução à Ciência de Dados

**Capacitação Introdutória de trainees · [FEA.dev](https://fea.dev)**

---

## Sobre

Este repositório contém o material completo da Capacitação Introdutória de Ciência de
Dados da FEA.dev — a organização estudantil de finanças quantitativas e ciência de dados
da USP.

O curso parte do **zero absoluto** em programação e chega, em cinco módulos, a uma
análise exploratória completa, com dados reais do mercado brasileiro.

### O que este material não cobre

- **Machine learning.** Fica para a capacitação avançada. Aqui, o objetivo é fazer bem o
  que vem antes: entender, limpar, resumir e visualizar dados. É a parte que consome a
  maior parte do tempo em qualquer projeto real e a que costuma ser pulada.
- **Python intermediário e avançado** — decoradores, classes, programação funcional,
  estruturas internas do interpretador. Nada disso é necessário para analisar dados, e
  tentar cobrir tudo só atrapalharia quem está começando.

---

## Como usar

### Google Colab (recomendado)

Não exige instalar nada. Abra o notebook do módulo **primeiro**: em
[colab.research.google.com](https://colab.research.google.com), menu
`Arquivo → Abrir notebook`, aba **GitHub**, colando a URL deste repositório.

Todo notebook que usa dados já traz uma célula de *setup* no topo. Ela clona o
repositório na máquina da sessão e entra na pasta do módulo, de modo que os caminhos
`../data/...` funcionem sem alteração. Execute-a antes das demais e pronto.

> **A ordem importa.** Cada notebook do Colab roda em uma máquina própria e efêmera.
> Clonar o repositório em um notebook não vale para outro: o *setup* precisa rodar dentro
> do notebook que você está usando, e de novo a cada nova sessão.

> **Atenção:** Ao abrir um notebook direto do GitHub, o Colab cria uma cópia temporária.
> Faça `Arquivo → Salvar uma cópia no Drive` antes de trabalhar, ou você perde tudo ao
> fechar a aba.

### No seu computador (VS Code)

Requer **Python 3.9 ou superior**.

```bash
git clone https://github.com/gustavokatsuo/Introducao-a-Ciencia-de-Dados.git
cd Introducao-a-Ciencia-de-Dados

python -m venv .venv
source .venv/bin/activate        # no Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

Depois abra a pasta do repositório no [VS Code](https://code.visualstudio.com/download),
instale as extensões **Python** e **Jupyter** (ambas da Microsoft), abra um `.ipynb` e
selecione o kernel do `.venv`. Quem preferir o Jupyter no navegador pode rodar
`jupyter lab` em vez disso.

O notebook
[`00_Configuracao/01_ambiente_de_desenvolvimento.ipynb`](00_Configuracao/01_ambiente_de_desenvolvimento.ipynb)
explica os dois caminhos passo a passo, para quem nunca abriu um terminal — Colab na
Parte A, VS Code na Parte B.

---

## Estrutura

| Módulo | Conteúdo | Notebooks | Tempo estimado |
|---|---|---|---|
| [**00 · Configuração**](00_Configuracao) | Notebooks, estado de execução, Colab ou VS Code, Git e GitHub | 2 | 1h10 |
| [**01 · Fundamentos de Python**](01_Fundamentos_Python) | Tipos, operadores, condicionais, loops, listas, dicionários, funções, escopo | 4 | 4h10 |
| [**02 · Manipulação de Dados**](02_Manipulacao_Dados) | NumPy, pandas, seleção, filtros, `groupby`, `merge`, limpeza | 4 | 4h50 |
| [**03 · Visualização e EDA**](03_Visualizacao_EDA) | Matplotlib, Seaborn, estatística descritiva, o processo de EDA | 4 | 4h30 |
| [**04 · Exercícios**](04_Exercicios) | Uma lista por módulo, com gabarito em arquivo separado | 8 | 8h |

**Carga total estimada:** cerca de 22 horas, distribuídas em 6 a 8 semanas.

Cada módulo tem seu próprio `README.md`, com contexto, lista de notebooks, tempo
estimado, bibliografia e palavras-chave.

### Ordem sugerida

```
00 → 01 → lista 01 → 02 → lista 02 → 03 → lista 03
```

A lista 00 pode ser feita junto com o módulo 00. **Não pule as listas**: cada módulo
assume o anterior com fluência, e a diferença entre ler o material e conseguir usá-lo
está inteiramente nos exercícios.

---

## Os dados

Todos os dados usados estão em [`data/`](data), **dentro do repositório**. Nenhum
notebook baixa dados da internet durante a execução — o material funciona offline, e os
números das aulas não mudam no meio do semestre.

| Arquivo | Conteúdo | Fonte |
|---|---|---|
| `acoes_b3.csv` | Cotações diárias de 8 ações da B3, 2021–2025 | Yahoo Finance |
| `ibovespa.csv` | Ibovespa diário no mesmo período | Yahoo Finance |
| `indicadores_macro.csv` | IPCA, Selic e dólar, mensais | Banco Central (SGS) |
| `empresas_b3.csv` | Cadastro das empresas (setor, controle, fundação) | Informação pública |
| `clientes_corretora.csv` | Base de clientes de corretora — **fictícia**, propositalmente suja | Gerada |
| `acoes_2025.xlsx` | Recorte em Excel, com duas abas | Yahoo Finance |

A coleta está documentada e é reproduzível: veja
[`data/coleta/coletar_dados.py`](data/coleta/coletar_dados.py) e
[`data/README.md`](data/README.md).

As figuras didáticas em [`assets/`](assets) são geradas por
[`assets/gerar_figuras.py`](assets/gerar_figuras.py). Nenhuma imagem do material é
carregada de site de terceiros.

---

## Qualidade do material

Todo `push` dispara um workflow que **executa todos os notebooks do começo ao fim**, em
Python 3.9 e 3.12 ([`test-notebooks.yml`](.github/workflows/test-notebooks.yml)). Se um
notebook quebrar, a falha aparece antes da aula — e não no meio dela, com trinta pessoas
esperando.

Os notebooks são versionados **sem saídas**. Isso mantém o repositório leve, os *diffs*
legíveis e garante que ninguém confunda o resultado salvo com o resultado do próprio
código.

---

## Contribuindo

Achou um erro, uma explicação confusa ou um exercício ambíguo? **Abra uma
[issue](../../issues).** Isso é uma contribuição de verdade para as turmas seguintes, e
uma boa primeira experiência de colaboração em um repositório.

Ao propor alterações, mantenha as três regras que sustentam este material:

1. **dados vendorizados** — nada de download em tempo de execução;
2. **imagens em `assets/`** — nada de hotlink;
3. **notebooks que rodam do zero** — rode `Reiniciar e executar tudo` antes de enviar.

---

## Créditos

Material desenvolvido pela **FEA.dev** para a formação de trainees.

Os dados de mercado vêm do Yahoo Finance e do Sistema Gerenciador de Séries Temporais do
Banco Central do Brasil, ambos de acesso público, e são usados aqui exclusivamente para
fins educacionais.

> **Atenção — Nada neste repositório é recomendação de investimento.** As análises são
> exercícios didáticos sobre dados históricos, e desempenho passado não indica resultado
> futuro.
