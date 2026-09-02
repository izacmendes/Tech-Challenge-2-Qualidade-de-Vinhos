# Estrutura do repositório

```text
.
├── .gitignore
├── CHECKLIST.md
├── ESTRUTURA.md
├── README.md
├── requirements.txt
├── data
│   ├── README.md
│   ├── raw
│   └── processed
├── docs
│   ├── README.md
│   └── apresentacao_executiva.pdf
├── notebooks
│   ├── 01_eda.ipynb
│   ├── 02_preprocessamento.ipynb
│   ├── 03_modelagem.ipynb
│   ├── 04_avaliacao.ipynb
│   └── README.md
├── results
│   ├── README.md
│   ├── figures
│   ├── metrics
│   └── models
└── src
    ├── README.md
    ├── __init__.py
    ├── config.py
    ├── data.py
    ├── preprocessing.py
    ├── models.py
    └── evaluation.py
```

## Convenções

| Regra | Aplicação |
|---|---|
| Notebooks numerados | `01_` a `04_`, na ordem de execução |
| Dataset bruto | `data/raw/`, não versionado |
| Dados processados | `data/processed/`, gerados pelo notebook 02 e não versionados |
| Figuras | `results/figures/`, versionadas |
| Métricas | `results/metrics/`, versionadas |
| Modelos | `results/models/`, não versionados |
| Random State | `RANDOM_STATE = 42` nos notebooks e nos pontos aleatórios |
| Código compartilhado | funções reutilizadas em `src/` |
| Nomes | `snake_case`, sem acentos e sem espaços |
