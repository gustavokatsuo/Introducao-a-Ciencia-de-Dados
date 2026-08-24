# Módulo 04 · SQL

**Capacitação Introdutória de Ciência de Dados · FEA.dev**

---

## Contexto

Nos módulos anteriores, todo dado chegou como arquivo: um `.csv`, um `.xlsx`, e a análise
começava no `read_csv`. Fora daqui quase nunca é assim. Os dados de uma empresa moram em
um **banco de dados**, e alguém precisou escrever uma consulta para que aquele arquivo
existisse.

Este módulo ensina a escrever essa consulta. É a habilidade que mais aparece em descrição
de vaga júnior de dados, e a única do tripé — Python, SQL, estatística — que a capacitação
ainda não cobria.

A boa notícia é que ele é curto em conceito novo. Quem terminou o módulo 02 já sabe
filtrar, agrupar e cruzar tabelas; aqui essas mesmas operações ganham outra sintaxe e
passam a rodar **dentro do banco**, o que muda tudo quando a tabela tem bilhões de linhas e
não cabe na memória. Cada aula fecha com a mesma pergunta respondida nas duas linguagens, e
a conferência de que os números batem.

A última aula trata do que separa quem escreve SQL de quem escreve SQL em produção:
parâmetros e injeção de SQL, onde traçar a linha entre banco e pandas, e o que muda ao
migrar para PostgreSQL ou BigQuery.

Usamos **SQLite**, que já vem com o Python e cabe em um arquivo — sem servidor, sem
instalação, funcionando igual no Colab e no VS Code. O SQL que você escreve aqui é o mesmo
de um banco de produção.

## Notebooks

| # | Notebook | Conteúdo | Tempo |
|---|---|---|---|
| 1 | [`01_introducao_e_select.ipynb`](01_introducao_e_select.ipynb) | Modelo relacional, chaves, conexão pelo Python, `SELECT`, `WHERE`, operadores, `NULL`, `ORDER BY`, `LIMIT`, `DISTINCT`, ordem de execução | 75 min |
| 2 | [`02_agregacoes_e_grupos.ipynb`](02_agregacoes_e_grupos.ipynb) | `COUNT`/`SUM`/`AVG`/`MIN`/`MAX`, `COUNT(*)` × `COUNT(col)`, `GROUP BY`, **`HAVING`**, `CASE WHEN`, agregação condicional, `strftime` | 75 min |
| 3 | [`03_joins.ipynb`](03_joins.ipynb) | Normalização, `INNER` × `LEFT JOIN`, `NULL` em junção, **conferência de junção**, granularidades diferentes, self-join | 80 min |
| 4 | [`04_subconsultas_e_janelas.ipynb`](04_subconsultas_e_janelas.ipynb) | Subconsultas, **CTEs (`WITH`)**, funções de janela, `LAG`/`LEAD`, `ROW_NUMBER`, `ROWS BETWEEN`, média móvel, drawdown | 90 min |
| 5 | [`05_sql_e_pandas.ipynb`](05_sql_e_pandas.ipynb) | Parâmetros e **injeção de SQL**, o que fazer no banco × no pandas, pipeline completo, `to_sql`, limpeza em SQL, dialetos | 60 min |

**Tempo total estimado:** 6h20

## Exercícios

[`05_Exercicios/lista_04_sql.ipynb`](../05_Exercicios/lista_04_sql.ipynb)
— 14 exercícios, cerca de 2h30, terminando em um ciclo completo de análise a partir do
banco. Gabarito em arquivo separado.

## O banco

O arquivo [`data/capacitacao.db`](../data/capacitacao.db) tem quatro tabelas, construídas a
partir dos **mesmos CSVs** dos módulos 02 e 03:

| Tabela | Linhas | Uma linha é |
|---|---|---|
| `empresas` | 8 | uma empresa listada (chave primária `ticker`) |
| `cotacoes` | 9.968 | um pregão de um papel (chave `data` + `ticker`) |
| `indicadores` | 60 | um mês de IPCA, Selic e dólar |
| `clientes` | 400 | um cliente da corretora fictícia — **suja de propósito** |

Isso é deliberado: a mesma pergunta, respondida em pandas e em SQL, tem que dar o mesmo
número. É assim que o trainee confere se entendeu.

O banco é reproduzível — veja
[`data/coleta/gerar_banco.py`](../data/coleta/gerar_banco.py).

## Ao final deste módulo você deve conseguir

- ler o esquema de um banco que você nunca viu e descrever o que há nele;
- responder perguntas de negócio com `WHERE`, `GROUP BY`, `HAVING` e `JOIN`;
- **conferir** se uma junção perdeu ou multiplicou linhas — e saber por que isso importa;
- calcular retorno, média móvel e ranking com funções de janela;
- quebrar uma consulta longa em CTEs que outra pessoa consiga ler;
- passar parâmetros com `?` e explicar por que `f-string` em SQL é um problema de
  segurança;
- decidir o que fazer no banco e o que trazer para o pandas.

## Conceitos que costumam travar

| Ponto | Onde está tratado |
|---|---|
| `=` compara; texto vai entre aspas **simples** | Aula 1, seção 7 |
| `NULL` não é igual a nada — use `IS NULL`, nunca `= NULL` | Aula 1, seção 8 |
| `<>` exclui os vazios em silêncio | Aula 1, seção 8 |
| O banco executa `FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY` | Aula 1, seção 11 |
| `COUNT(*)` conta linhas; `COUNT(coluna)` ignora vazios | Aula 2, seção 2 |
| `WHERE` filtra linhas; `HAVING` filtra grupos | Aula 2, seção 4 |
| Em `CASE WHEN`, a ordem das condições muda o resultado | Aula 2, seção 5 |
| Com `SUM(CASE ...)` use `ELSE 0`; com `AVG(CASE ...)`, nunca | Aula 2, seção 6 |
| Todo `JOIN` precisa de conferência: conte antes, conte depois | Aula 3, seção 6 |
| Chave repetida do lado direito **multiplica** as linhas | Aula 3, seção 6 |
| Para juntar granularidades diferentes, agregue primeiro | Aula 3, seção 8 |
| Depois de um `JOIN`, pergunte: *uma linha disto é o quê?* | Aula 3, seção 7 |
| Esquecer `PARTITION BY` em `LAG` mistura papéis diferentes | Aula 4, seção 4 |
| **`WHERE` amputa a janela** — janela na CTE, filtro por fora | Aula 4, seção 6 |
| Com `ORDER BY` na janela e sem quadro, o padrão é acumulado | Aula 4, seção 6 |
| Funções de janela não podem ser usadas no `WHERE` | Aula 4, seção 5 |
| Valores vão em `?`; nunca monte SQL com `f-string` | Aula 5, seção 1 |
| `CAST` inconversível vira `0.0` no SQLite, sem erro | Aula 5, seção 5 |

### O SQLite perdoa o que os outros bancos recusam

Três diferenças que o módulo mostra explicitamente, porque viram bug na migração:

| O que o SQLite aceita | O que o PostgreSQL faz |
|---|---|
| apelido do `SELECT` usado no `WHERE` | erro |
| coluna fora do `GROUP BY` e fora de agregação | erro (o SQLite devolve valor arbitrário) |
| `CAST` de texto inconversível | erro (o SQLite devolve `0.0` ou um pedaço do número) |

Escreva como se ele fosse estrito, e trocar de banco será um detalhe.

## Bibliografia e leituras

- [SQLBolt](https://sqlbolt.com/) — exercícios interativos no navegador, o melhor primeiro complemento
- [Select Star SQL](https://selectstarsql.com/) — livro livre online, com exercícios sobre dados reais
- [Documentação do SQLite](https://www.sqlite.org/lang.html) — a referência da sintaxe usada aqui
- [Modern SQL — window functions](https://modern-sql.com/feature/over) — a melhor explicação de funções de janela que existe
- [PostgreSQL Tutorial](https://www.postgresqltutorial.com/) — para quando você encostar no primeiro banco de produção
- [Use The Index, Luke](https://use-the-index-luke.com/) — por que uma consulta é lenta, e o que fazer

## Palavras-chave

`banco relacional` · `tabela` · `chave primária` · `chave estrangeira` · `normalização`
· `SQLite` · `SELECT` · `FROM` · `WHERE` · `NULL` · `IS NULL` · `ORDER BY` · `LIMIT`
· `DISTINCT` · `COUNT` · `SUM` · `AVG` · `GROUP BY` · `HAVING` · `CASE WHEN`
· `agregação condicional` · `strftime` · `JOIN` · `INNER JOIN` · `LEFT JOIN`
· `granularidade` · `subconsulta` · `CTE` · `WITH` · `função de janela` · `OVER`
· `PARTITION BY` · `LAG` · `ROW_NUMBER` · `ROWS BETWEEN` · `média móvel` · `drawdown`
· `parâmetro` · `injeção de SQL` · `read_sql_query` · `to_sql` · `dialeto`
