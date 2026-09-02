import pandas as pd


def load_dataset(path):
    df = pd.read_csv(path)
    df.columns = [str(col).strip() for col in df.columns]
    return df


def save_dataset(df, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False)
