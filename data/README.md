# data/

Esta pasta separa os dados brutos dos conjuntos derivados utilizados durante o fluxo analítico.

- `raw/`: arquivo bruto do Wine Quality Dataset; não versionado no Git.
- `processed/`: arquivos derivados gerados pelo notebook `02_preprocessamento.ipynb`; não versionados no Git.

O dataset é a base pública indicada no enunciado do Tech Challenge. A variável alvo é derivada de `quality`: `quality >= 7` corresponde a High Quality e `quality < 7` a Low/Medium Quality.
