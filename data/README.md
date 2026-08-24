# Dados

**Capacitação Introdutória de Ciência de Dados · FEA.dev**

---

Todos os dados usados no material estão nesta pasta, **versionados junto com o
repositório**. Nenhum notebook baixa dados da internet durante a execução.

Essa decisão é deliberada e tem três motivos:

1. **funciona sempre** — sem internet, com internet ruim, atrás do firewall da faculdade;
2. **os números não mudam** no meio do semestre, então os resultados do material batem
   com o que o aluno vê na tela;
3. **não depende de terceiros** — APIs mudam de formato, mudam de endereço e saem do ar,
   e um curso não pode quebrar por causa disso.

Como os notebooks ficam em pastas de módulo, o caminho até aqui é sempre `../data/`.

---

## `acoes_b3.csv`

Cotações diárias de oito ações da B3.

**9.968 linhas × 8 colunas** · 2021-01-04 a 2025-12-30 · uma linha por ativo e por pregão

| Coluna | Tipo | Descrição |
|---|---|---|
| `data` | data | Data do pregão (`AAAA-MM-DD`) |
| `ticker` | texto | Código de negociação do papel |
| `abertura` | número | Preço de abertura, em R$ |
| `maxima` | número | Maior preço do dia, em R$ |
| `minima` | número | Menor preço do dia, em R$ |
| `fechamento` | número | Preço de fechamento, em R$, ajustado por desdobramentos e grupamentos |
| `fechamento_ajustado` | número | Fechamento ajustado também por **dividendos e JCP** — é o que mede o retorno de quem investiu |
| `volume` | inteiro | Quantidade de ações negociadas no dia |

**Ativos:** ABEV3, B3SA3, BBDC4, ITUB4, MGLU3, PETR4, VALE3, WEGE3.
Todos com 1.246 pregões, o que mantém as séries alinhadas no tempo.

> **Atenção — Use `fechamento_ajustado` para calcular retornos.** O `fechamento` bruto
> ignora os proventos e subestima o retorno de ações que pagam muito dividendo — como
> várias desta amostra.

> **Atenção — MGLU3 passou por um grupamento de ações (1:10) em 2025.** Como os preços
> históricos são ajustados retroativamente por esse evento, a série mostra valores em
> torno de R$ 200 em 2021 — o papel não era negociado a esse preço na época. O ajuste é o
> correto para calcular retorno; só não confunda com o preço de tela daquele dia.

**Fonte:** Yahoo Finance (endpoint público de *chart*).

---

## `ibovespa.csv`

O índice Ibovespa no mesmo período, para servir de referência de mercado.

**1.246 linhas × 6 colunas** · 2021-01-04 a 2025-12-30

| Coluna | Tipo | Descrição |
|---|---|---|
| `data` | data | Data do pregão |
| `abertura`, `maxima`, `minima`, `fechamento` | número | Pontos do índice |
| `volume` | inteiro | Volume do índice |

**Fonte:** Yahoo Finance (`^BVSP`).

---

## `indicadores_macro.csv`

Indicadores macroeconômicos brasileiros, mensais.

**60 linhas × 5 colunas** · janeiro/2021 a dezembro/2025

| Coluna | Tipo | Descrição |
|---|---|---|
| `data` | data | Primeiro dia do mês de referência |
| `ipca_mes_pct` | número | Variação do IPCA no mês, em % (série SGS 433) |
| `selic_mes_pct` | número | Selic acumulada no mês, em % (série SGS 4390) |
| `dolar_medio` | número | Cotação média do dólar comercial (venda) no mês, em R$ (série SGS 1) |
| `dolar_fim_mes` | número | Cotação do dólar no último dia útil do mês, em R$ |

**Fonte:** Banco Central do Brasil — Sistema Gerenciador de Séries Temporais (SGS),
[dadosabertos.bcb.gov.br](https://dadosabertos.bcb.gov.br/).

---

## `empresas_b3.csv`

Cadastro das oito empresas, para exercícios de junção.

**8 linhas × 5 colunas**

| Coluna | Tipo | Descrição |
|---|---|---|
| `ticker` | texto | Código de negociação — a **chave** de junção com `acoes_b3.csv` |
| `empresa` | texto | Razão social |
| `setor` | texto | Setor de atuação |
| `controle` | texto | `Estatal` ou `Privada` |
| `ano_fundacao` | inteiro | Ano de fundação da empresa |

**Fonte:** informação pública das próprias companhias, compilada manualmente.

---

## `clientes_corretora.csv`

Base de clientes de uma corretora **fictícia**.

**400 linhas × 10 colunas**

> **Atenção — Estes dados são inventados.** Nenhuma pessoa real está representada aqui. A
> base foi gerada aleatoriamente com semente fixa e depois **deteriorada de propósito**,
> para servir de matéria-prima à aula de limpeza de dados.

| Coluna | Tipo esperado | Descrição |
|---|---|---|
| `id_cliente` | inteiro | Identificador do cliente |
| `nome` | texto | Nome fictício |
| `idade` | inteiro | Idade em anos |
| `cidade` | texto | Cidade de residência |
| `estado` | texto | UF |
| `perfil_investidor` | categoria | `Conservador`, `Moderado` ou `Arrojado` |
| `data_cadastro` | data | Data de abertura da conta |
| `patrimonio_investido` | número | Patrimônio na corretora, em R$ |
| `aporte_mensal` | número | Aporte médio mensal, em R$ |
| `ativo` | booleano | Se o cliente ainda opera |

### Defeitos intencionais

| Problema | Onde aparece |
|---|---|
| **20 linhas totalmente duplicadas** | qualquer lugar da base |
| **70 células vazias** | `idade`, `cidade`, `perfil_investidor`, `patrimonio_investido` |
| **Idades impossíveis** (−3, 0, 199) | `idade` |
| **Número salvo como texto**, em formato brasileiro (`"R$ 412.666,21"`) | `patrimonio_investido` |
| **Dois formatos de data misturados** (`2020-09-25` e `27/02/2024`) | `data_cadastro` |
| **Categorias inconsistentes** (`Conservador`, `CONSERVADOR`, `conservador`, `" Conservador "`) | `perfil_investidor` |
| **Acentuação e caixa inconsistentes** (`São Paulo`, `SAO PAULO`, `são paulo`) — 34 valores distintos para 10 cidades | `cidade` |
| **Quatro valores para duas situações** (`sim`, `nao`, `1`, `0`) | `ativo` |

---

## `acoes_2025.xlsx`

Um recorte em Excel, para a aula de leitura de planilhas.

| Aba | Conteúdo |
|---|---|
| `cotacoes` | PETR4, VALE3 e ITUB4 em 2025 (750 linhas) |
| `cadastro` | Cópia de `empresas_b3.csv` |

Ler exige a biblioteca `openpyxl`, já incluída no `requirements.txt`.

---

## `capacitacao.db`

O banco **SQLite** usado no módulo 04. Não traz dado novo: é uma reorganização dos CSVs
acima em quatro tabelas relacionais, com chaves de verdade.

| Tabela | Linhas | Origem | Chave |
|---|---|---|---|
| `empresas` | 8 | `empresas_b3.csv` | `ticker` (primária) |
| `cotacoes` | 9.968 | `acoes_b3.csv` | `data` + `ticker` (primária); `ticker` → `empresas` |
| `indicadores` | 60 | `indicadores_macro.csv` | `data` (primária) |
| `clientes` | 400 | `clientes_corretora.csv` | sem chave — a tabela suja |

A escolha de reaproveitar exatamente os mesmos dados é deliberada: **a mesma pergunta,
respondida em pandas e em SQL, tem que dar o mesmo número.** É o que permite ao trainee
conferir sozinho se entendeu, e é o eixo do módulo 04 inteiro.

Duas decisões de esquema que aparecem nas aulas:

- **As datas são texto em formato ISO (`AAAA-MM-DD`).** O SQLite não tem tipo de data; o
  ISO é o formato em que a ordem alfabética coincide com a cronológica, o que faz
  `WHERE data BETWEEN '2025-01-01' AND '2025-01-31'` funcionar como se espera.
- **A tabela `clientes` entra suja, e sem tipos numéricos.** `patrimonio_investido` é
  `TEXT` porque guarda coisas como `'R$ 412.666,21'` — e limpar isso é o exercício.

Gerado por [`coleta/gerar_banco.py`](coleta/gerar_banco.py), que reconstrói o banco do zero
a partir dos CSVs e confere linha a linha:

```bash
cd data/coleta
python gerar_banco.py
```

---

## Reprodutibilidade

O script [`coleta/coletar_dados.py`](coleta/coletar_dados.py) documenta e reproduz a
coleta inteira. Ele **não** é executado pelos notebooks — foi rodado uma vez para gerar
os arquivos acima e fica versionado para dois fins:

1. registrar exatamente de onde veio cada número;
2. permitir atualizar a base em semestres futuros.

```bash
cd data/coleta
python coletar_dados.py
```

Atualizar a base **muda os resultados** de todos os notebooks. Se fizer isso, execute o
material inteiro e revise os textos que citam números específicos.

---

## Uso e licença dos dados

Os dados de mercado e os indicadores macroeconômicos são de acesso público e estão aqui
**exclusivamente para fins educacionais**. A base de clientes é fictícia.

> **Atenção:** Nada neste repositório é recomendação de investimento.
