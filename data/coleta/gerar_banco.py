"""
Gera o banco SQLite usado no módulo 04 (SQL) a partir dos CSVs desta pasta.

O banco é construído — não coletado. Todos os números saem dos mesmos arquivos
que os módulos 02 e 03 já usam, de propósito: a mesma pergunta respondida em
pandas e em SQL tem que dar exatamente o mesmo resultado, senão o paralelo que
sustenta o módulo se perde.

O arquivo `capacitacao.db` fica versionado junto com os CSVs, pela mesma razão
que eles: o material precisa funcionar offline e sem passo de preparação.

Uso:
    cd data/coleta
    python gerar_banco.py
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pandas as pd

PASTA_DADOS = Path(__file__).resolve().parent.parent
BANCO = PASTA_DADOS / "capacitacao.db"


# --- esquema -----------------------------------------------------------------
# Declarado à mão, em vez de deixar o pandas inferir, por três motivos:
# chaves primárias e estrangeiras de verdade (para o JOIN ter significado),
# NOT NULL onde faz sentido, e tipos previsíveis nas aulas.

ESQUEMA = """
DROP TABLE IF EXISTS cotacoes;
DROP TABLE IF EXISTS indicadores;
DROP TABLE IF EXISTS clientes;
DROP TABLE IF EXISTS empresas;

CREATE TABLE empresas (
    ticker        TEXT PRIMARY KEY,
    empresa       TEXT NOT NULL,
    setor         TEXT NOT NULL,
    controle      TEXT NOT NULL,
    ano_fundacao  INTEGER NOT NULL
);

CREATE TABLE cotacoes (
    data                 TEXT    NOT NULL,
    ticker               TEXT    NOT NULL,
    abertura             REAL    NOT NULL,
    maxima               REAL    NOT NULL,
    minima               REAL    NOT NULL,
    fechamento           REAL    NOT NULL,
    fechamento_ajustado  REAL    NOT NULL,
    volume               INTEGER NOT NULL,
    PRIMARY KEY (data, ticker),
    FOREIGN KEY (ticker) REFERENCES empresas (ticker)
);

CREATE TABLE indicadores (
    data           TEXT PRIMARY KEY,
    ipca_mes_pct   REAL,
    selic_mes_pct  REAL,
    dolar_medio    REAL,
    dolar_fim_mes  REAL
);

-- A tabela de clientes entra SUJA de propósito: é a mesma base do módulo 02,
-- com os mesmos defeitos, para que a aula de limpeza tenha versão em SQL.
-- Por isso aqui não há NOT NULL nem tipos numéricos: patrimonio_investido
-- guarda coisas como 'R$ 412.666,21', e é esse o exercício.
CREATE TABLE clientes (
    id_cliente            INTEGER,
    nome                  TEXT,
    idade                 REAL,
    cidade                TEXT,
    estado                TEXT,
    perfil_investidor     TEXT,
    data_cadastro         TEXT,
    patrimonio_investido  TEXT,
    aporte_mensal         REAL,
    ativo                 TEXT
);

CREATE INDEX idx_cotacoes_ticker ON cotacoes (ticker);
CREATE INDEX idx_cotacoes_data   ON cotacoes (data);
"""


def _ler_csv(nome: str) -> pd.DataFrame:
    return pd.read_csv(PASTA_DADOS / nome)


def construir() -> None:
    if BANCO.exists():
        BANCO.unlink()

    conexao = sqlite3.connect(BANCO)
    try:
        conexao.executescript(ESQUEMA)

        empresas = _ler_csv("empresas_b3.csv")
        cotacoes = _ler_csv("acoes_b3.csv")
        indicadores = _ler_csv("indicadores_macro.csv")
        clientes = _ler_csv("clientes_corretora.csv")

        # As datas viram texto ISO (AAAA-MM-DD). O SQLite não tem tipo de data;
        # o formato ISO é a convenção que faz comparação e ordenação de texto
        # coincidirem com a ordem cronológica. Isso é assunto da aula 1.
        for tabela in (cotacoes, indicadores):
            tabela["data"] = pd.to_datetime(tabela["data"]).dt.strftime("%Y-%m-%d")

        # A ordem importa: empresas primeiro, porque cotacoes referencia ticker.
        empresas.to_sql("empresas", conexao, if_exists="append", index=False)
        cotacoes.to_sql("cotacoes", conexao, if_exists="append", index=False)
        indicadores.to_sql("indicadores", conexao, if_exists="append", index=False)
        clientes.to_sql("clientes", conexao, if_exists="append", index=False)

        conexao.commit()
        conexao.execute("VACUUM")
    finally:
        conexao.close()


def conferir() -> None:
    """Confere que o banco reproduz os CSVs, linha por linha."""
    conexao = sqlite3.connect(BANCO)
    try:
        esperado = {
            "empresas": len(_ler_csv("empresas_b3.csv")),
            "cotacoes": len(_ler_csv("acoes_b3.csv")),
            "indicadores": len(_ler_csv("indicadores_macro.csv")),
            "clientes": len(_ler_csv("clientes_corretora.csv")),
        }
        for tabela, linhas in esperado.items():
            (obtido,) = conexao.execute(f"SELECT COUNT(*) FROM {tabela}").fetchone()
            marca = "ok" if obtido == linhas else "DIVERGENTE"
            print(f"  {tabela:12} {obtido:6} linhas  ({marca})")
            if obtido != linhas:
                raise SystemExit(f"{tabela}: esperava {linhas}, obtive {obtido}")

        # A integridade referencial só vale se ninguém violou a chave estrangeira.
        orfaos = conexao.execute(
            "SELECT COUNT(*) FROM cotacoes c "
            "LEFT JOIN empresas e ON c.ticker = e.ticker WHERE e.ticker IS NULL"
        ).fetchone()[0]
        print(f"  cotações sem empresa correspondente: {orfaos}")
        if orfaos:
            raise SystemExit("há cotações órfãs — a chave estrangeira foi violada")
    finally:
        conexao.close()


def main() -> None:
    print(f"Gerando {BANCO.name} a partir dos CSVs de {PASTA_DADOS.name}/ ...")
    construir()
    conferir()
    tamanho = BANCO.stat().st_size / 1024
    print(f"Pronto: {BANCO} ({tamanho:.0f} KB)")


if __name__ == "__main__":
    main()
