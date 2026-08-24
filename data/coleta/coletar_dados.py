"""
Coleta e vendorização dos dados usados na Capacitação Introdutória FEA.dev.

Este script foi executado UMA VEZ para gerar os arquivos da pasta `data/`.
Ele NÃO é executado pelos notebooks: todo o material lê apenas os arquivos
já salvos em `data/`, sem qualquer download em tempo de execução.

Ele fica versionado por dois motivos:
  1. documentar exatamente de onde veio cada número;
  2. permitir atualizar a base em anos futuros (basta rodar de novo).

Fontes
------
* Preços de ações e Ibovespa : Yahoo Finance (endpoint público de chart)
* Indicadores macroeconômicos: Banco Central do Brasil, API do SGS
  (https://dadosabertos.bcb.gov.br/) - séries 433 (IPCA), 4390 (Selic
  acumulada no mês) e 1 (dólar comercial, venda).
* Cadastro de clientes     : FICTÍCIO, gerado aleatoriamente neste script.

Uso:
    python coletar_dados.py
"""

from __future__ import annotations

import io
import json
import time
import unicodedata
import urllib.request
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

PASTA_DADOS = Path(__file__).resolve().parents[1]
DATA_INICIO = "2021-01-01"
DATA_FIM = "2025-12-31"

CABECALHO = {"User-Agent": "Mozilla/5.0 (compatible; FEAdev-material/1.0)"}

TICKERS = {
    "PETR4.SA": "PETR4",
    "VALE3.SA": "VALE3",
    "ITUB4.SA": "ITUB4",
    "BBDC4.SA": "BBDC4",
    "ABEV3.SA": "ABEV3",
    "WEGE3.SA": "WEGE3",
    "MGLU3.SA": "MGLU3",
    "B3SA3.SA": "B3SA3",
}


def _baixar_json(url: str) -> dict:
    requisicao = urllib.request.Request(url, headers=CABECALHO)
    with urllib.request.urlopen(requisicao, timeout=60) as resposta:
        return json.loads(resposta.read().decode("utf-8"))


def _para_epoch(data_iso: str) -> int:
    return int(datetime.strptime(data_iso, "%Y-%m-%d").timestamp())


def baixar_serie_yahoo(simbolo: str) -> pd.DataFrame:
    """Baixa o histórico diário de um ativo no Yahoo Finance."""
    url = (
        "https://query1.finance.yahoo.com/v8/finance/chart/"
        f"{simbolo}?period1={_para_epoch(DATA_INICIO)}"
        f"&period2={_para_epoch(DATA_FIM)}&interval=1d&events=div%2Csplit"
    )
    bruto = _baixar_json(url)
    resultado = bruto["chart"]["result"][0]
    cotacoes = resultado["indicators"]["quote"][0]
    ajustado = resultado["indicators"]["adjclose"][0]["adjclose"]

    tabela = pd.DataFrame(
        {
            "data": pd.to_datetime(resultado["timestamp"], unit="s", utc=True)
            .tz_convert("America/Sao_Paulo")
            .date,
            "abertura": cotacoes["open"],
            "maxima": cotacoes["high"],
            "minima": cotacoes["low"],
            "fechamento": cotacoes["close"],
            "fechamento_ajustado": ajustado,
            "volume": cotacoes["volume"],
        }
    )
    return tabela.dropna(subset=["fechamento"]).reset_index(drop=True)


def baixar_serie_bcb(codigo: int) -> pd.DataFrame:
    """Baixa uma série temporal do SGS do Banco Central."""
    inicio = datetime.strptime(DATA_INICIO, "%Y-%m-%d").strftime("%d/%m/%Y")
    fim = datetime.strptime(DATA_FIM, "%Y-%m-%d").strftime("%d/%m/%Y")
    url = (
        f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados"
        f"?formato=json&dataInicial={inicio}&dataFinal={fim}"
    )
    tabela = pd.DataFrame(_baixar_json(url))
    tabela["data"] = pd.to_datetime(tabela["data"], format="%d/%m/%Y")
    tabela["valor"] = pd.to_numeric(tabela["valor"])
    return tabela


def gerar_acoes() -> pd.DataFrame:
    partes = []
    for simbolo, ticker in TICKERS.items():
        print(f"  baixando {ticker} ...")
        parte = baixar_serie_yahoo(simbolo)
        parte.insert(1, "ticker", ticker)
        partes.append(parte)
        time.sleep(1.5)
    acoes = pd.concat(partes, ignore_index=True)
    acoes = acoes.sort_values(["data", "ticker"]).reset_index(drop=True)
    for coluna in ["abertura", "maxima", "minima", "fechamento", "fechamento_ajustado"]:
        acoes[coluna] = acoes[coluna].round(2)
    acoes["volume"] = acoes["volume"].astype("Int64")
    return acoes


def gerar_ibovespa() -> pd.DataFrame:
    print("  baixando ^BVSP ...")
    ibov = baixar_serie_yahoo("%5EBVSP")
    ibov = ibov[["data", "abertura", "maxima", "minima", "fechamento", "volume"]]
    for coluna in ["abertura", "maxima", "minima", "fechamento"]:
        ibov[coluna] = ibov[coluna].round(0)
    ibov["volume"] = ibov["volume"].astype("Int64")
    return ibov


def gerar_indicadores() -> pd.DataFrame:
    print("  baixando séries do Banco Central ...")
    ipca = baixar_serie_bcb(433).rename(columns={"valor": "ipca_mes_pct"})
    selic = baixar_serie_bcb(4390).rename(columns={"valor": "selic_mes_pct"})
    dolar = baixar_serie_bcb(1).rename(columns={"valor": "dolar"})

    ipca["mes"] = ipca["data"].dt.to_period("M")
    selic["mes"] = selic["data"].dt.to_period("M")
    dolar["mes"] = dolar["data"].dt.to_period("M")

    dolar_mensal = dolar.groupby("mes").agg(
        dolar_medio=("dolar", "mean"), dolar_fim_mes=("dolar", "last")
    )

    indicadores = (
        ipca[["mes", "ipca_mes_pct"]]
        .merge(selic[["mes", "selic_mes_pct"]], on="mes", how="outer")
        .merge(dolar_mensal, on="mes", how="outer")
        .sort_values("mes")
    )
    indicadores.insert(0, "data", indicadores["mes"].dt.to_timestamp().dt.date)
    indicadores = indicadores.drop(columns="mes")
    indicadores["dolar_medio"] = indicadores["dolar_medio"].round(4)
    indicadores["dolar_fim_mes"] = indicadores["dolar_fim_mes"].round(4)
    return indicadores.reset_index(drop=True)


def gerar_empresas() -> pd.DataFrame:
    """Tabela cadastral escrita à mão (informação pública das empresas)."""
    return pd.DataFrame(
        [
            ("PETR4", "Petróleo Brasileiro S.A. - Petrobras", "Petróleo e Gás", "Estatal", 1953),
            ("VALE3", "Vale S.A.", "Mineração", "Privada", 1942),
            ("ITUB4", "Itaú Unibanco Holding S.A.", "Financeiro", "Privada", 1945),
            ("BBDC4", "Banco Bradesco S.A.", "Financeiro", "Privada", 1943),
            ("ABEV3", "Ambev S.A.", "Consumo não cíclico", "Privada", 1999),
            ("WEGE3", "WEG S.A.", "Bens industriais", "Privada", 1961),
            ("MGLU3", "Magazine Luiza S.A.", "Consumo cíclico", "Privada", 1957),
            ("B3SA3", "B3 S.A. - Brasil, Bolsa, Balcão", "Financeiro", "Privada", 2008),
        ],
        columns=["ticker", "empresa", "setor", "controle", "ano_fundacao"],
    )


def gerar_clientes(semente: int = 42) -> pd.DataFrame:
    """
    Base FICTÍCIA de clientes de uma corretora, propositalmente "suja".

    Os defeitos são intencionais e servem de matéria-prima para a aula de
    limpeza de dados: valores faltantes, linhas duplicadas, números salvos
    como texto, datas em formatos diferentes e categorias inconsistentes.
    """
    rng = np.random.default_rng(semente)
    n = 380

    primeiros = ["Ana", "Bruno", "Carla", "Diego", "Elisa", "Felipe", "Gabriela",
                 "Henrique", "Isabela", "João", "Karina", "Lucas", "Mariana",
                 "Nicolas", "Olívia", "Pedro", "Rafaela", "Sofia", "Thiago", "Vitor"]
    sobrenomes = ["Almeida", "Barbosa", "Carvalho", "Dias", "Esteves", "Ferreira",
                  "Gomes", "Higashi", "Ibrahim", "Junior", "Klein",
                  "Lima", "Moraes", "Nunes", "Oliveira", "Pereira", "Queiroz",
                  "Ribeiro", "Santos", "Tanaka"]
    cidades = ["São Paulo", "Campinas", "Ribeirão Preto", "Santos", "Sorocaba",
               "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre", "Recife"]
    estados = {"São Paulo": "SP", "Campinas": "SP", "Ribeirão Preto": "SP",
               "Santos": "SP", "Sorocaba": "SP", "Rio de Janeiro": "RJ",
               "Belo Horizonte": "MG", "Curitiba": "PR", "Porto Alegre": "RS",
               "Recife": "PE"}
    perfis = ["Conservador", "Moderado", "Arrojado"]

    linhas = []
    for i in range(n):
        cidade = str(rng.choice(cidades))
        idade = int(rng.integers(18, 76))
        perfil = str(rng.choice(perfis, p=[0.45, 0.35, 0.20]))
        base_patrimonio = {"Conservador": 40_000, "Moderado": 110_000, "Arrojado": 260_000}[perfil]
        patrimonio = float(rng.lognormal(np.log(base_patrimonio), 0.55))
        aporte = patrimonio * float(rng.uniform(0.005, 0.03))
        dia = int(rng.integers(1, 29))
        mes = int(rng.integers(1, 13))
        ano = int(rng.integers(2019, 2026))
        linhas.append(
            {
                "id_cliente": 1000 + i,
                "nome": f"{rng.choice(primeiros)} {rng.choice(sobrenomes)}",
                "idade": idade,
                "cidade": cidade,
                "estado": estados[cidade],
                "perfil_investidor": perfil,
                "data_cadastro": f"{ano:04d}-{mes:02d}-{dia:02d}",
                "patrimonio_investido": round(patrimonio, 2),
                "aporte_mensal": round(aporte, 2),
                "ativo": bool(rng.random() > 0.18),
            }
        )

    clientes = pd.DataFrame(linhas)

    # --- sujeira proposital -------------------------------------------------
    # 1) valores faltantes
    for coluna, fracao in [("idade", 0.06), ("perfil_investidor", 0.05),
                           ("patrimonio_investido", 0.04), ("cidade", 0.03)]:
        alvo = rng.choice(clientes.index, size=int(len(clientes) * fracao), replace=False)
        clientes.loc[alvo, coluna] = np.nan

    # 2) idades impossíveis
    alvo = rng.choice(clientes.index, size=5, replace=False)
    clientes.loc[alvo, "idade"] = rng.choice([-3, 0, 199, 250], size=5)

    # 3) dinheiro salvo como texto no formato brasileiro (ponto de milhar e
    #    vírgula decimal), como sai de uma exportação de Excel em pt-BR.
    #    Parte das linhas ainda carrega o prefixo "R$".
    com_cifrao = set(rng.choice(clientes.index, size=90, replace=False))
    clientes["patrimonio_investido"] = clientes["patrimonio_investido"].astype(object)
    for indice in clientes.index:
        valor = clientes.at[indice, "patrimonio_investido"]
        if pd.isna(valor):
            continue
        texto = f"{valor:,.2f}".replace(",", "@").replace(".", ",").replace("@", ".")
        clientes.at[indice, "patrimonio_investido"] = (
            f"R$ {texto}" if indice in com_cifrao else texto
        )

    # 4) datas em formato brasileiro em parte das linhas
    alvo = rng.choice(clientes.index, size=90, replace=False)
    clientes["data_cadastro"] = clientes["data_cadastro"].astype(object)
    for indice in alvo:
        ano, mes, dia = clientes.at[indice, "data_cadastro"].split("-")
        clientes.at[indice, "data_cadastro"] = f"{dia}/{mes}/{ano}"

    # 5) categorias inconsistentes (caixa e espaços)
    alvo = rng.choice(clientes.index, size=60, replace=False)
    clientes["perfil_investidor"] = clientes["perfil_investidor"].astype(object)
    for indice in alvo:
        valor = clientes.at[indice, "perfil_investidor"]
        if isinstance(valor, str):
            escolha = rng.integers(0, 3)
            if escolha == 0:
                valor = valor.upper()
            elif escolha == 1:
                valor = valor.lower()
            else:
                valor = f"  {valor} "
            clientes.at[indice, "perfil_investidor"] = valor

    # 6) cidades com acentuação e caixa inconsistentes
    clientes["cidade"] = clientes["cidade"].astype(object)
    sem_acento = set(rng.choice(clientes.index, size=70, replace=False))
    caixa_alta = set(rng.choice(clientes.index, size=45, replace=False))
    caixa_baixa = set(rng.choice(clientes.index, size=45, replace=False))
    for indice in clientes.index:
        valor = clientes.at[indice, "cidade"]
        if not isinstance(valor, str):
            continue
        if indice in sem_acento:
            valor = unicodedata.normalize("NFKD", valor).encode("ascii", "ignore").decode()
        if indice in caixa_alta:
            valor = valor.upper()
        elif indice in caixa_baixa:
            valor = valor.lower()
        clientes.at[indice, "cidade"] = valor

    # 7) "ativo" gravado de três jeitos diferentes
    clientes["ativo"] = clientes["ativo"].map({True: "sim", False: "nao"})
    alvo = rng.choice(clientes.index, size=80, replace=False)
    clientes.loc[alvo, "ativo"] = clientes.loc[alvo, "ativo"].map({"sim": "1", "nao": "0"})

    # 8) linhas duplicadas
    duplicadas = clientes.sample(20, random_state=semente)
    clientes = pd.concat([clientes, duplicadas], ignore_index=True)
    clientes = clientes.sample(frac=1, random_state=semente).reset_index(drop=True)

    return clientes


def gerar_excel(acoes: pd.DataFrame, empresas: pd.DataFrame) -> None:
    """Versão em Excel de um recorte, para a aula de leitura de planilhas."""
    recorte = acoes[
        (acoes["ticker"].isin(["PETR4", "VALE3", "ITUB4"]))
        & (pd.to_datetime(acoes["data"]).dt.year == 2025)
    ].copy()
    caminho = PASTA_DADOS / "acoes_2025.xlsx"
    with pd.ExcelWriter(caminho, engine="openpyxl") as escritor:
        recorte.to_excel(escritor, sheet_name="cotacoes", index=False)
        empresas.to_excel(escritor, sheet_name="cadastro", index=False)
    print(f"  data/acoes_2025.xlsx  ({len(recorte)} linhas, 2 abas)")


def main() -> None:
    print("Coletando dados...")
    acoes = gerar_acoes()
    ibovespa = gerar_ibovespa()
    indicadores = gerar_indicadores()
    empresas = gerar_empresas()
    clientes = gerar_clientes()

    arquivos = {
        "acoes_b3.csv": acoes,
        "ibovespa.csv": ibovespa,
        "indicadores_macro.csv": indicadores,
        "empresas_b3.csv": empresas,
        "clientes_corretora.csv": clientes,
    }
    for nome, tabela in arquivos.items():
        caminho = PASTA_DADOS / nome
        tabela.to_csv(caminho, index=False)
        print(f"  data/{nome}  ({len(tabela)} linhas, {tabela.shape[1]} colunas)")

    gerar_excel(acoes, empresas)
    print("Pronto.")


if __name__ == "__main__":
    main()
