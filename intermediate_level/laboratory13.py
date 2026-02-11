# Módulo. Ciencia de datos
from pathlib import Path

import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

DATA_PATH = Path("intermediate_level/data.csv")
MODEL_PATH = Path("intermediate_level/model.joblib")


def create_sample_csv():
    """Create a simple CSV if it doesn't exist."""
    if DATA_PATH.exists():
        return

    data = [
        {"age": 22, "income": 15000, "buy": 0},
        {"age": 25, "income": 18000, "buy": 0},
        {"age": 28, "income": 22000, "buy": 0},
        {"age": 35, "income": 45000, "buy": 1},
        {"age": 40, "income": 52000, "buy": 1},
        {"age": 48, "income": 61000, "buy": 1},
        {"age": 52, "income": 68000, "buy": 1},
        {"age": 23, "income": 20000, "buy": 0},
        {"age": 30, "income": 32000, "buy": 0},
        {"age": 45, "income": 58000, "buy": 1},
    ]

    df = pd.DataFrame(data)
    df.to_csv(DATA_PATH, index=False)
    print("Sample CSV created")


def load_and_clean_data():
    """Load and clean the CSV."""
    df = pd.read_csv(DATA_PATH)
    df = df.dropna()
    return df


def train_model(df):
    """Train a simple classifier."""
    X = df[["age", "income"]]
    y = df["buy"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42
    )

    model = LogisticRegression()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(f"Accuracy: {acc:.2f}")
    return model


def save_model(model):
    joblib.dump(model, MODEL_PATH)
    print("Saved model in:", MODEL_PATH)


def load_model():
    return joblib.load(MODEL_PATH)


def run_inference(model):
    """Make a test prediction."""
    sample = [[33, 40000]]  # age, income
    prediction = model.predict(sample)[0]

    print("Prediction for [age=33, income=40000]:", prediction)


if __name__ == "__main__":
    create_sample_csv()
    df = load_and_clean_data()
    model = train_model(df)
    save_model(model)

    loaded_model = load_model()
    run_inference(loaded_model)
