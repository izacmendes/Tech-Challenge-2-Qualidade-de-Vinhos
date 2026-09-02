import pandas as pd


def create_target(df, threshold=7):
    result = df.copy()
    result["high_quality"] = (result["quality"] >= threshold).astype(int)
    return result


def get_features(df):
    excluded = {"quality", "high_quality", "Id"}
    return [col for col in df.columns if col not in excluded]


def add_engineered_features(X):
    result = X.copy()
    result["total_acidity"] = result["fixed acidity"] + result["volatile acidity"] + result["citric acid"]
    result["bound_sulfur_dioxide"] = (result["total sulfur dioxide"] - result["free sulfur dioxide"]).clip(lower=0)
    result["free_sulfur_ratio"] = result["free sulfur dioxide"] / (result["total sulfur dioxide"] + 1e-6)
    result["sulphates_chlorides_ratio"] = result["sulphates"] / (result["chlorides"] + 1e-6)
    return result


def outlier_report(df, features):
    rows = []
    for col in features:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        mask = (df[col] < lower) | (df[col] > upper)
        rows.append({
            "Feature": col,
            "Q1": q1,
            "Q3": q3,
            "IQR": iqr,
            "Lower bound": lower,
            "Upper bound": upper,
            "Outliers": int(mask.sum()),
            "Outlier percentage": round(mask.mean()*100, 2),
        })
    return pd.DataFrame(rows).sort_values("Outliers", ascending=False).reset_index(drop=True)
