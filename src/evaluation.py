import pandas as pd
from sklearn.inspection import permutation_importance
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score


def evaluate_predictions(name, y_true, y_pred, y_prob):
    return {
        "Model": name,
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred, zero_division=0),
        "Recall": recall_score(y_true, y_pred, zero_division=0),
        "F1": f1_score(y_true, y_pred, zero_division=0),
        "ROC-AUC": roc_auc_score(y_true, y_prob),
    }


def permutation_importance_table(model, X_test, y_test, random_state=42):
    result = permutation_importance(model, X_test, y_test, scoring="f1", n_repeats=20, random_state=random_state, n_jobs=1)
    return pd.DataFrame({
        "Feature": X_test.columns,
        "Mean importance": result.importances_mean,
        "Std importance": result.importances_std,
    }).sort_values("Mean importance", ascending=False).reset_index(drop=True)
