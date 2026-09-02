# Tech Challenge - Fase 2 | POSTECH Data Analytics

## 1. Identificação

| Campo | Valor |
|---|---|
| Turma | Pós Tech - Data Analytics |
| Grupo | 14 |
| Data de entrega | 01/09/2026 |

### Integrantes

| Nome completo | RM | E-mail |
|---|---|---|
| Izabella Costa Mendes | rm375012 | rm375012@fiap.com.br |

## 2. Links da entrega

| Item | Link |
|---|---|
| Repositório | https://github.com/izacmendes/Tech-Challenge-2-Qualidade-de-Vinhos.git |
| Vídeo executivo (<= 5 min) | https://drive.google.com/file/d/1WaAwaF46T9etUlQgIO9Ks6kkKFQiD4HA/view?usp=sharing |
| Apresentação | https://drive.google.com/file/d/1w-uMfAHdgdHIWz3YADIgztKj4kE-P7-L/view?usp=sharing |

## 3. O problema

A avaliação da qualidade do vinho tradicionalmente depende de análise sensorial. Este projeto investiga se características físico-químicas podem apoiar a identificação de vinhos classificados como High Quality e atuar como uma camada adicional de suporte ao monitoramento da qualidade.

### Variável alvo

A variável original `quality` foi transformada em classificação binária:

- `quality >= 7` -> High Quality (`1`)
- `quality < 7` -> Low/Medium Quality (`0`)

O limiar de 7 segue a definição do Tech Challenge e concentra a previsão na categoria de maior qualidade.

### Dataset

| Campo | Valor |
|---|---|
| Fonte | Wine Quality Dataset, conforme indicado no enunciado |
| Linhas x colunas | 1.143 x 13 |
| Período / versão | Não especificado no material fornecido |
| Licença de uso | Não especificada no material fornecido |

### Descrição das variáveis

| Variável | Tipo | Descrição |
|---|---|---|
| `fixed acidity` | Numérica | Acidez fixa |
| `volatile acidity` | Numérica | Acidez volátil |
| `citric acid` | Numérica | Concentração de ácido cítrico |
| `residual sugar` | Numérica | Açúcar residual |
| `chlorides` | Numérica | Concentração de cloretos |
| `free sulfur dioxide` | Numérica | Dióxido de enxofre livre |
| `total sulfur dioxide` | Numérica | Dióxido de enxofre total |
| `density` | Numérica | Densidade |
| `pH` | Numérica | Medida de pH |
| `sulphates` | Numérica | Sulfatos |
| `alcohol` | Numérica | Teor alcoólico |
| `quality` | Inteira | Nota original de qualidade |
| `Id` | Inteira | Identificador; não utilizado como preditor |

## 4. Como reproduzir

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
jupyter notebook
```

O dataset bruto é mantido em `data/raw/` e não é versionado. Execute os notebooks na ordem abaixo:

| # | Notebook | O que faz |
|---|---|---|
| 1 | `notebooks/01_eda.ipynb` | Análise exploratória |
| 2 | `notebooks/02_preprocessamento.ipynb` | Limpeza, escala e feature engineering |
| 3 | `notebooks/03_modelagem.ipynb` | Treino e comparação dos modelos |
| 4 | `notebooks/04_avaliacao.ipynb` | Métricas, importância de variáveis e implicações de negócio |

Semente fixa: `RANDOM_STATE = 42`, declarada na primeira célula de cada notebook.

## 5. Resultados

### Validação cruzada

| Model               |   Accuracy |   Precision |   Recall |     F1 |   ROC-AUC |
|:--------------------|-----------:|------------:|---------:|-------:|----------:|
| Random Forest       |     0.9026 |      0.7734 |   0.4492 | 0.5609 |    0.9227 |
| Gradient Boosting   |     0.8884 |      0.6345 |   0.4738 | 0.5401 |    0.9052 |
| Logistic Regression |     0.7845 |      0.3719 |   0.7975 | 0.5054 |    0.8694 |

### Teste final - Random Forest

| Model         |   Accuracy |   Precision |   Recall |     F1 |   ROC-AUC |
|:--------------|-----------:|------------:|---------:|-------:|----------:|
| Random Forest |     0.9083 |      0.7619 |   0.5000 | 0.6038 |    0.9124 |

**Modelo escolhido:** Random Forest

**Métricas priorizadas:** F1-score, Recall, Precision e ROC-AUC, complementadas por Accuracy. A classe High Quality representa 13,91% da base, de modo que Accuracy isolada não representa adequadamente a capacidade de identificar a classe minoritária.

### Principais sinais preditivos

A permutation importance destaca `alcohol`, `volatile acidity`, `citric acid`, `sulphates` e `total sulfur dioxide` entre os principais sinais preditivos.

## 6. Principais conclusões

- A base apresenta forte desbalanceamento entre as classes.
- Não foram encontrados valores ausentes nem registros duplicados.
- `alcohol` apresenta a associação linear mais forte com a qualidade e aparece como principal sinal preditivo.
- `residual sugar` e `chlorides` concentram as maiores taxas de outliers pelo critério IQR; os valores foram preservados.
- Features derivadas foram testadas e não apresentaram ganho de F1 sobre as variáveis originais; a versão final mantém o conjunto original.
- Random Forest apresentou o melhor perfil global na validação cruzada e foi selecionado como modelo final.
- No teste final, o Random Forest apresentou Accuracy de 0.9083, Precision de 0.7619, Recall de 0.5000, F1 de 0.6038 e ROC-AUC de 0.9124.

### Limitações e próximos passos

A classe High Quality é minoritária e parte dos casos positivos ainda não é identificada pelo modelo. A importância das variáveis representa contribuição preditiva, não causalidade. Antes de uso operacional, recomenda-se validação em novos dados de produção e avaliação do limiar de decisão de acordo com o custo de falsos positivos e falsos negativos.

## 7. Estrutura do repositório

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

## 8. Tecnologias

Python, Pandas, NumPy, Matplotlib, Scikit-learn, Joblib e Jupyter Notebook.
