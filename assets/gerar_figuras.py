"""
Gera as figuras didáticas usadas nos notebooks e READMEs.

Todas as imagens do repositório são produzidas aqui e salvas em `assets/`.
Nenhuma imagem é carregada de site de terceiros (hotlink), o que garante que o
material continue funcionando offline e daqui a alguns anos.

Uso:
    python gerar_figuras.py
"""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

PASTA = Path(__file__).resolve().parent

AZUL = "#1f4e79"
AZUL_CLARO = "#cfe2f3"
LARANJA = "#c55a11"
LARANJA_CLARO = "#fbe5d6"
VERDE = "#2e7d32"
CINZA = "#595959"
CINZA_CLARO = "#f2f2f2"

plt.rcParams["font.size"] = 11


def _caixa(ax, x, y, largura, altura, texto, cor_fundo, cor_borda, tamanho=11,
           negrito=False, cor_texto="black"):
    ax.add_patch(
        mpatches.FancyBboxPatch(
            (x, y), largura, altura,
            boxstyle="round,pad=0.02,rounding_size=0.06",
            facecolor=cor_fundo, edgecolor=cor_borda, linewidth=1.6,
        )
    )
    ax.text(
        x + largura / 2, y + altura / 2, texto,
        ha="center", va="center", fontsize=tamanho, color=cor_texto,
        fontweight="bold" if negrito else "normal",
    )


def figura_anatomia_dataframe():
    """As partes de um DataFrame."""
    fig, ax = plt.subplots(figsize=(9.5, 4.6))
    ax.set_xlim(0, 9.5)
    ax.set_ylim(0, 4.6)
    ax.axis("off")

    colunas = ["ticker", "preco", "setor"]
    dados = [
        ["PETR4", "32.50", "Petróleo"],
        ["VALE3", "61.20", "Mineração"],
        ["ITUB4", "28.75", "Financeiro"],
    ]
    indices = ["0", "1", "2"]

    x0, y0 = 2.2, 0.9
    larg_idx, larg_col, alt = 0.85, 1.75, 0.62

    _caixa(ax, x0, y0 + 3 * alt, larg_idx, alt, "", CINZA_CLARO, CINZA)
    for j, nome in enumerate(colunas):
        _caixa(ax, x0 + larg_idx + j * larg_col, y0 + 3 * alt, larg_col, alt,
               nome, AZUL_CLARO, AZUL, negrito=True)

    for i, linha in enumerate(dados):
        y = y0 + (2 - i) * alt
        _caixa(ax, x0, y, larg_idx, alt, indices[i], CINZA_CLARO, CINZA, negrito=True)
        for j, valor in enumerate(linha):
            _caixa(ax, x0 + larg_idx + j * larg_col, y, larg_col, alt, valor,
                   "white", "#bfbfbf", tamanho=10)

    ax.annotate("índice\n(rótulo das linhas)", xy=(x0 + 0.4, y0 + 1.6),
                xytext=(0.15, 3.35), fontsize=10.5, color=CINZA, ha="left",
                arrowprops=dict(arrowstyle="-|>", color=CINZA, linewidth=1.5,
                                connectionstyle="arc3,rad=-0.25"))
    ax.annotate("colunas\n(cada uma é uma Series)",
                xy=(x0 + larg_idx + 1.6 * larg_col, y0 + 3 * alt + alt),
                xytext=(4.1, 4.25), fontsize=10.5, color=AZUL, ha="left",
                arrowprops=dict(arrowstyle="-|>", color=AZUL, linewidth=1.5,
                                connectionstyle="arc3,rad=0.2"))
    ax.annotate("valores", xy=(x0 + larg_idx + 1.55 * larg_col, y0 + 0.02),
                xytext=(7.4, 0.22), fontsize=10.5, color=LARANJA, ha="left",
                arrowprops=dict(arrowstyle="-|>", color=LARANJA, linewidth=1.5,
                                connectionstyle="arc3,rad=0.25"))

    ax.text(0.15, 4.35, "Anatomia de um DataFrame", fontsize=13.5,
            fontweight="bold", color="black")

    fig.savefig(PASTA / "anatomia_dataframe.png", dpi=160, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


def figura_loc_iloc():
    """loc trabalha com rótulos; iloc, com posições."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.4))

    indices = ["2025-01-02", "2025-01-03", "2025-01-06"]
    colunas = ["abertura", "fechamento", "volume"]
    dados = [
        ["37.10", "37.85", "38,2M"],
        ["37.90", "37.20", "41,7M"],
        ["37.15", "38.40", "35,9M"],
    ]

    configuracoes = [
        (axes[0], ".loc  →  rótulos", AZUL, AZUL_CLARO,
         'df.loc["2025-01-03", "fechamento"]', indices, colunas),
        (axes[1], ".iloc  →  posições", LARANJA, LARANJA_CLARO,
         "df.iloc[1, 1]", ["0", "1", "2"], ["0", "1", "2"]),
    ]

    for ax, titulo, cor, cor_clara, chamada, rotulos_linha, rotulos_col in configuracoes:
        ax.set_xlim(0, 6.4)
        ax.set_ylim(0, 4.4)
        ax.axis("off")

        x0, y0 = 1.35, 0.95
        larg_idx, larg_col, alt = 1.45, 1.2, 0.6

        _caixa(ax, x0, y0 + 3 * alt, larg_idx, alt, "", CINZA_CLARO, CINZA)
        for j, nome in enumerate(rotulos_col):
            _caixa(ax, x0 + larg_idx + j * larg_col, y0 + 3 * alt, larg_col, alt,
                   nome, cor_clara, cor, tamanho=8.5, negrito=True)

        for i, linha in enumerate(dados):
            y = y0 + (2 - i) * alt
            _caixa(ax, x0, y, larg_idx, alt, rotulos_linha[i], cor_clara, cor,
                   tamanho=9, negrito=True)
            for j, valor in enumerate(linha):
                destaque = (i == 1 and j == 1)
                _caixa(ax, x0 + larg_idx + j * larg_col, y, larg_col, alt, valor,
                       "#ffe699" if destaque else "white",
                       "#bf9000" if destaque else "#bfbfbf", tamanho=9,
                       negrito=destaque)

        ax.text(0.15, 3.95, titulo, fontsize=13, fontweight="bold", color=cor)
        ax.text(3.2, 0.45, chamada, fontsize=11, ha="center", family="monospace",
                bbox=dict(boxstyle="round,pad=0.4", facecolor="#ffe699",
                          edgecolor="#bf9000"))

    fig.suptitle("Os dois seletores do pandas — mesma célula, dois endereços",
                 fontsize=13.5, fontweight="bold", y=1.0)
    fig.savefig(PASTA / "loc_vs_iloc.png", dpi=160, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


def figura_fluxo_eda():
    """O ciclo da Análise Exploratória de Dados."""
    fig, ax = plt.subplots(figsize=(11.5, 4.8))
    ax.set_xlim(0, 11.5)
    ax.set_ylim(0, 4.8)
    ax.axis("off")

    etapas = [
        ("1. PERGUNTA", "O que eu quero\ndescobrir?", AZUL, AZUL_CLARO),
        ("2. EXPLORAÇÃO", "Tabelas, resumos\ne gráficos", LARANJA, LARANJA_CLARO),
        ("3. DESCOBERTA", "O que os dados\nmostraram?", "#7030a0", "#e4d5f0"),
        ("4. HIPÓTESE", "Por que isso\nacontece?", VERDE, "#e2f0d9"),
    ]

    largura, altura = 2.35, 1.6
    y = 2.05
    for i, (titulo, texto, cor, cor_clara) in enumerate(etapas):
        x = 0.35 + i * (largura + 0.42)
        _caixa(ax, x, y, largura, altura, "", cor_clara, cor)
        ax.text(x + largura / 2, y + altura - 0.36, titulo, ha="center",
                va="center", fontsize=11, fontweight="bold", color=cor)
        ax.text(x + largura / 2, y + altura / 2 - 0.32, texto, ha="center",
                va="center", fontsize=9.8, color="black")
        if i < len(etapas) - 1:
            ax.annotate("", xy=(x + largura + 0.38, y + altura / 2),
                        xytext=(x + largura + 0.04, y + altura / 2),
                        arrowprops=dict(arrowstyle="-|>", color=CINZA, linewidth=2))

    ax.annotate(
        "", xy=(1.5, y - 0.10), xytext=(10.0, y - 0.10),
        arrowprops=dict(arrowstyle="-|>", color=CINZA, linewidth=1.8,
                        linestyle="--", connectionstyle="arc3,rad=-0.30"),
    )
    ax.text(5.75, 0.12, "a hipótese vira a próxima pergunta — o ciclo recomeça",
            ha="center", fontsize=10.5, color=CINZA, style="italic")
    ax.text(5.75, 4.45, "O ciclo da Análise Exploratória de Dados",
            ha="center", fontsize=13.5, fontweight="bold")

    fig.savefig(PASTA / "fluxo_eda.png", dpi=160, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


def figura_escolha_grafico():
    """Que gráfico usar para cada pergunta."""
    fig, ax = plt.subplots(figsize=(11, 5.2))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 5.2)
    ax.axis("off")

    itens = [
        ("Uma variável numérica\n— como se distribui?", "histograma · boxplot", AZUL),
        ("Duas numéricas\n— há relação?", "dispersão (scatter)", LARANJA),
        ("Numérica ao longo do tempo\n— como evoluiu?", "linha", VERDE),
        ("Numérica por categoria\n— quem é maior?", "barras", "#7030a0"),
        ("Muitas numéricas juntas\n— quem anda com quem?", "mapa de calor", "#c00000"),
    ]

    largura, altura = 10.3, 0.78
    for i, (pergunta, grafico, cor) in enumerate(itens):
        y = 4.05 - i * (altura + 0.16)
        _caixa(ax, 0.35, y, largura, altura, "", "white", cor)
        ax.text(0.65, y + altura / 2, pergunta, ha="left", va="center", fontsize=10.2)
        ax.text(10.35, y + altura / 2, grafico, ha="right", va="center",
                fontsize=11, fontweight="bold", color=cor)

    ax.text(5.5, 4.95, "Qual gráfico usar?", ha="center", fontsize=13.5,
            fontweight="bold")

    fig.savefig(PASTA / "escolha_do_grafico.png", dpi=160, bbox_inches="tight",
                facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    figura_anatomia_dataframe()
    figura_loc_iloc()
    figura_fluxo_eda()
    figura_escolha_grafico()
    for imagem in sorted(PASTA.glob("*.png")):
        print(f"  assets/{imagem.name}  ({imagem.stat().st_size/1024:.0f} KB)")
