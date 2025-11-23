from joblib import load
import numpy as np
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "model.pkl"

def predict_delay(priority: int, est_days: int, hist_rate: float = 0.7):
    if not MODEL_PATH.exists():
        return {"error": "Model not found. Run train.py first."}

    model = load(MODEL_PATH)

    X = np.array([[priority, est_days, hist_rate]])
    pred = model.predict(X)[0]
    prob = model.predict_proba(X)[0][1]

    return {
        "delayed": bool(pred),
        "probability": round(float(prob) * 100, 2),
    }
