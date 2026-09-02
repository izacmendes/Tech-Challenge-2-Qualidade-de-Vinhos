from pathlib import Path

RANDOM_STATE = 42

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
RESULTS_DIR = BASE_DIR / "results"
FIGURES_DIR = RESULTS_DIR / "figures"
METRICS_DIR = RESULTS_DIR / "metrics"
MODELS_DIR = RESULTS_DIR / "models"
DATA_FILE = RAW_DATA_DIR / "winequality.csv"

for folder in [PROCESSED_DATA_DIR, RESULTS_DIR, FIGURES_DIR, METRICS_DIR, MODELS_DIR]:
    folder.mkdir(parents=True, exist_ok=True)
