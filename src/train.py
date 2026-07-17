import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

# Load dataset

df = pd.read_csv(
    "data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv"
)


# Cleaning

df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"],
    errors="coerce"
)

df = df.dropna()


# Drop ID

df = df.drop(
    "customerID",
    axis=1
)


# Target split

X = df.drop(
    "Churn",
    axis=1
)

y = df["Churn"].map(
    {
        "Yes":1,
        "No":0
    }
)


# Encoding

X = pd.get_dummies(
    X,
    drop_first=True
)


# Split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Model

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(
    X_train,
    y_train
)


# Save model

os.makedirs(
    "../models",
    exist_ok=True
)

joblib.dump(
    model,
    "models/random_forest_model.pkl"
)


print("Model training completed ✅")