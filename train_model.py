import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import joblib

# Load data
df = pd.read_csv("cars24data.csv")

# Feature columns and target
X = df[[
    "Manufacturing_year", "Engine capacity", "Spare key",
    "Transmission", "KM driven", "Ownership", "Fuel type",
    "Imperfections", "Repainted Parts"
]]
y = df["Price"]

# Preprocessing
categorical_features = ["Spare key", "Transmission", "Fuel type"]
numerical_features = [
    "Manufacturing_year", "Engine capacity", "KM driven",
    "Ownership", "Imperfections", "Repainted Parts"
]

preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown='ignore'), categorical_features)
], remainder='passthrough')

# Create pipeline
model = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("regressor", RandomForestRegressor(random_state=42))
])

# Train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model.pkl")
