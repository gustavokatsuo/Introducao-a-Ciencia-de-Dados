# Módulo 00 · Configuração do ambiente

**Capacitação Introdutória de Ciência de Dados · FEA.dev**

---

## Contexto

Ninguém aprende a analisar dados enquanto ainda está tentando fazer o computador
funcionar. Este módulo resolve a parte chata primeiro: onde escrever código, como
executá-lo e como trazer o material da capacitação para o seu ambiente.

Ele também apresenta o conceito que mais confunde quem está começando — o **estado** de um
notebook — e ensina a ler uma mensagem de erro sem entrar em pânico. Os dois assuntos vão
economizar horas de frustração nas semanas seguintes.

A primeira aula apresenta **dois ambientes possíveis**, e o trainee escolhe um: o Google
Colab, que roda no navegador e não exige instalação, ou o VS Code no próprio computador,
com Python, ambiente virtual e a extensão Jupyter. O Colab segue como caminho recomendado
para quem nunca programou; o VS Code está documentado passo a passo para quem prefere
trabalhar local. As duas partes são independentes — quem escolhe uma pula a outra.

Git e GitHub aparecem aqui em nível básico: o que são, como navegar em um repositório e
como clonar. *Branch*, *merge* e *pull request* ficam de fora de propósito — são assunto
de uma capacitação de ferramentas, e tentar cobrir tudo agora atrapalharia o que
realmente importa.

## Notebooks

| # | Notebook | Conteúdo | Tempo |
|---|---|---|---|
| 1 | [`01_ambiente_de_desenvolvimento.ipynb`](01_ambiente_de_desenvolvimento.ipynb) | O que é um notebook, células, ordem de execução e estado, Google Colab (Parte A), VS Code com venv e extensão Jupyter (Parte B), bibliotecas, leitura de erros | 40 min (1h pelo VS Code) |
| 2 | [`02_git_e_github.ipynb`](02_git_e_github.ipynb) | Controle de versão, Git × GitHub, vocabulário mínimo, como baixar o material, conferência do ambiente | 30 min |

**Tempo total estimado:** 1h10 — cerca de 1h30 para quem instalar o VS Code

## Exercícios

[`04_Exercicios/lista_00_configuracao.ipynb`](../04_Exercicios/lista_00_configuracao.ipynb)
— 8 exercícios, cerca de 40 minutos. Gabarito em arquivo separado.

## Ao final deste módulo você deve conseguir

- executar células de um notebook e explicar por que a ordem de execução importa;
- escolher entre Colab e VS Code sabendo o que cada um custa e o que cada um entrega;
- salvar uma cópia de um notebook do GitHub no seu Google Drive; ou, no VS Code, criar um
  ambiente virtual, instalar o `requirements.txt` e selecionar o kernel certo;
- clonar o repositório da capacitação no Colab ou na sua máquina;
- identificar o tipo de um erro pela última linha da mensagem;
- formular um pedido de ajuda que possa efetivamente ser respondido.

## Bibliografia e leituras

- [Documentação do Google Colab](https://colab.research.google.com/notebooks/basic_features_overview.ipynb) — visão geral dos recursos
- [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) — documentação oficial do editor
- [Python environments in VS Code](https://code.visualstudio.com/docs/python/environments) — ambientes virtuais e seleção de interpretador
- [Git Handbook (GitHub, em português)](https://docs.github.com/pt/get-started/using-git) — introdução oficial ao Git
- [Learn Git Branching](https://learngitbranching.js.org/?locale=pt_BR) — tutorial visual, para quando quiser ir além do básico
- [Project Jupyter](https://jupyter.org/) — o projeto por trás dos notebooks

## Palavras-chave

`notebook` · `célula` · `estado de execução` · `kernel` · `Google Colab` · `VS Code`
· `extensão Jupyter` · `ambiente virtual` · `venv` · `requirements.txt` · `biblioteca`
· `import` · `traceback` · `Git` · `GitHub` · `repositório` · `commit` · `clone` · `pull`
· `README`
