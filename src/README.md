# src/

Esta pasta concentra as funções reutilizadas por mais de um notebook. A separação dos componentes compartilhados reduz duplicação de código e mantém consistência entre as etapas do projeto.

| Arquivo | Responsabilidade |
|---|---|
| `config.py` | caminhos, `RANDOM_STATE` e constantes |
| `data.py` | carregamento e salvamento de datasets |
| `preprocessing.py` | definição do alvo, preparação e feature engineering |
| `models.py` | definição dos modelos de classificação |
| `evaluation.py` | métricas e interpretação do desempenho |

Os notebooks importam esses componentes diretamente com, por exemplo:

```python
from src.config import RANDOM_STATE
```
