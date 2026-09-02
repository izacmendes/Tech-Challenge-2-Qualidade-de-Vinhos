# Roteiro dos slides

1. **Problema** — apoiar a identificação de vinhos de Alta Qualidade usando dados físico-químicos.
2. **Base** — 1.143 amostras; 11 indicadores; target binário.
3. **Desbalanceamento** — 13,91% Alta Qualidade; por isso Accuracy sozinha não basta.
4. **EDA** — principais sinais: alcohol, volatile acidity, citric acid, sulphates.
5. **Qualidade dos dados** — 0 missing/duplicados; outliers identificados e mantidos.
6. **Modelos** — Regressão Logística, Random Forest e Gradient Boosting.
7. **Escolha** — Random Forest: melhor desempenho global na validação cruzada.
8. **Resultado** — teste: Accuracy 90,83%, Precision 76,19%, Recall 50,00%, F1 60,38%, ROC-AUC 91,24%.
9. **Variáveis-chave** — destaque para alcohol e outras recorrentes.
10. **Recomendação** — usar como apoio ao monitoramento e priorização do controle de qualidade, mantendo avaliação sensorial como referência.
