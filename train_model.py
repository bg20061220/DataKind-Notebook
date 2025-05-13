import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
from sklearn.model_selection  import GridSearchCV
import joblib

# Load data
df = pd.read_csv("cars24data.csv")

# Custom transformer to bin imperfections
class ImperfectionBinner(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        X = X.copy()
        def bin_imperfections(val):
            if val == 0:
                return "None"
            elif val <= 5:
                return "Low"
            elif val <= 15:
                return "Medium"
            else:
                return "High"
        X["Imperfection_Level"] = X["Imperfections"].apply(bin_imperfections)
        return X.drop("Imperfections", axis=1)
    

# Feature Engineering: Create Car Age and KM per Year
current_year = 2025  # You can dynamically get the current year if needed
df['Car_Age'] = current_year - df['Manufacturing_year']  # Calculate Car Age
df['KM_per_Year'] = df['KM driven'] / df['Car_Age']  # Calculate KM per Year


# Drop the 'Manufacturing Year' column as we now have 'Car Age'
df.drop(columns=["Manufacturing_year"], inplace=True)


# Feature columns and target
X = df[[
    "Engine capacity", "Spare key", "Transmission", "KM driven", 
    "Ownership", "Fuel type", "Imperfections", "Repainted Parts", 
    "Car_Age", "KM_per_Year"
]]
y = df["Price"]

# Updated feature list (after binning)
categorical_features = ["Spare key", "Transmission", "Fuel type", "Imperfection_Level"]
numerical_features = [
    "Manufacturing_year", "Engine capacity", "KM driven",
    "Ownership", "Repainted Parts"
]

# Preprocessor
preprocessor = ColumnTransformer([
    ("cat", OneHotEncoder(handle_unknown='ignore'), categorical_features)
], remainder='passthrough')

# Final pipeline
model = Pipeline(steps=[
    ("bin_imperfections", ImperfectionBinner()),
    ("preprocessor", preprocessor),
   ("regressor", RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    min_samples_split=10,
    random_state=42
))

])


# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model.fit(X_train, y_train)

# Initial results 
# R² Score: 0.8292
# Mean Absolute Error (MAE): 53962.1107
# Mean Squared Error (MSE): 5691486187.1972
# Root Mean Squared Error (RMSE): 75441.9392

# # Check 2 
# R² Score: 0.8345
# Mean Absolute Error (MAE): 54008.6417
# Mean Squared Error (MSE): 5514299203.9640
# Root Mean Squared Error (RMSE): 74258.3275
# Save model
joblib.dump(model, "model.pkl")
