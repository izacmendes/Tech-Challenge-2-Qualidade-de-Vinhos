# results/

Os resultados analíticos são organizados em três grupos.

| Pasta | Conteúdo | Versionado? |
|---|---|---|
| `figures/` | gráficos exportados (`.png`) | sim |
| `metrics/` | tabelas e relatórios (`.csv` / `.txt`) | sim |
| `models/` | modelos serializados (`.pkl` / `.joblib`) | não |

Figuras e métricas ficam versionadas para permitir que o avaliador consulte os resultados sem executar novamente os notebooks. Os modelos podem ser regenerados pela etapa de modelagem/avaliação.
