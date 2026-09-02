# Resultados consolidados — análise em português

## Base
1.143 registros, 13 colunas, 11 variáveis preditoras, 0 missing, 0 duplicados.

## Target
984 Baixa/Média (86,09%) e 159 Alta Qualidade (13,91%).

## Validação cruzada no conjunto de treino (Cross-Validation)

| Modelo              |   Accuracy |   Precision |   Recall |     F1 |   ROC-AUC |
|:--------------------|-----------:|------------:|---------:|-------:|----------:|
| Regressão Logística |     0.7845 |      0.3719 |   0.7975 | 0.5054 |    0.8694 |
| Random Forest       |     0.9026 |      0.7734 |   0.4492 | 0.5609 |    0.9227 |
| Gradient Boosting   |     0.8884 |      0.6345 |   0.4738 | 0.5401 |    0.9052 |

## Avaliação final no conjunto de teste

| Modelo              |   Accuracy |   Precision |   Recall |     F1 |   ROC-AUC |
|:--------------------|-----------:|------------:|---------:|-------:|----------:|
| Regressão Logística |     0.7991 |      0.3793 |   0.6875 | 0.4889 |    0.8504 |
| Random Forest       |     0.9083 |      0.7619 |   0.5000 | 0.6038 |    0.9124 |
| Gradient Boosting   |     0.8996 |      0.6667 |   0.5625 | 0.6102 |    0.8775 |

## Modelo escolhido e justificativa
**Random Forest**, por melhor desempenho global na validação cruzada.

## Teste do modelo final
Matriz de confusão (Confusion Matrix):
```text
[[192,   5],
 [ 16,  16]]
```

Recall Alta Qualidade = 50%. Isso mostra que ainda há falsos negativos.

## Variáveis relevantes (Feature Importance)
Permutation importance: **alcohol** é o maior sinal preditivo, seguido por `volatile acidity`, `citric acid`, `sulphates` e `total sulfur dioxide`.
