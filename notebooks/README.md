# notebooks/

Os notebooks seguem uma ordem numérica obrigatória e representam o fluxo completo de análise e modelagem do Tech Challenge - Fase 2.

| Arquivo | Escopo | Rúbrica |
|---|---|---|
| `01_eda.ipynb` | Distribuições, correlações, outliers e balanceamento | Dim. 3 - 20 pts |
| `02_preprocessamento.ipynb` | Nulos, definição do alvo, normalização e feature engineering | Dim. 4 - 15 pts |
| `03_modelagem.ipynb` | Split/CV, treino de pelo menos dois modelos e comparação | Dim. 5 - 20 pts |
| `04_avaliacao.ipynb` | Métricas, feature importance e implicações de negócio | Dim. 6 - 20 pts |

## Regras

- A execução deve ocorrer de cima para baixo em ambiente limpo (`Kernel -> Restart & Run All`).
- As células devem permanecer em ordem crescente.
- As saídas dos gráficos e tabelas relevantes permanecem salvas nos notebooks.
- Todo gráfico é acompanhado imediatamente por interpretação em Markdown.
- A primeira célula de cada notebook define `RANDOM_STATE = 42` e os caminhos do projeto.
- O mesmo `RANDOM_STATE = 42` é utilizado em todos os pontos aleatórios.
