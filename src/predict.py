import joblib
import pandas as pd


model = joblib.load(
    "models/random_forest_model.pkl"
)


def predict_churn(data):

    prediction = model.predict(data)

    if prediction[0] == 1:
        return "Customer will Churn"

    else:
        return "Customer will Stay"


print("Prediction system ready ✅")