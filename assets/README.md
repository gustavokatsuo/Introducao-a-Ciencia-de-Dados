# Assets

Figuras didáticas usadas nos notebooks e READMEs da capacitação.

**Todas as imagens do repositório ficam aqui.** Nenhuma é carregada de site de terceiros
(*hotlink*) — links externos quebram, mudam de conteúdo e deixam o material inutilizável
offline.

| Arquivo | Onde é usado |
|---|---|
| `banner.png` | README raiz — banner da FEA.dev |
| `anatomia_dataframe.png` | Módulo 02, aula 2 — as partes de um DataFrame |
| `loc_vs_iloc.png` | Módulo 02, aula 2 — rótulos × posições |
| `escolha_do_grafico.png` | Módulo 03, aula 2 — que gráfico usar para cada pergunta |
| `fluxo_eda.png` | Módulo 03, aula 4 — o ciclo da análise exploratória |

## Como as figuras são geradas

Todas são produzidas por [`gerar_figuras.py`](gerar_figuras.py), com Matplotlib:

```bash
cd assets
python gerar_figuras.py
```

Isso mantém as imagens versionáveis, reproduzíveis e editáveis — se um rótulo precisar
mudar, altera-se o código e regenera-se o arquivo, em vez de procurar o `.png` original
em algum lugar.

## Como usar em um notebook

Caminhos relativos em células de texto nem sempre são renderizados (o Colab, por exemplo,
não os exibe). Por isso, no material as figuras são exibidas por uma célula de código:

```python
from IPython.display import Image
Image("../assets/nome_da_figura.png", width=800)
```

Em arquivos `README.md`, o caminho relativo em Markdown funciona normalmente:

```markdown
![Descrição](assets/nome_da_figura.png)
```
