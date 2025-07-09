import streamlit as st
import pandas as pd
import joblib
from train_model import ImperfectionBinner
# Load the model
model = joblib.load("model.pkl")

st.title("🚗 Second-hand Car Price Predictor (Only For Maruti Cars)")

# User input
year = st.number_input("Manufacturing Year", min_value=1990, max_value=2025)
engine = st.number_input("Engine Capacity (cc)", min_value=500, max_value=5000)
spare_key = st.selectbox("Spare Key", ["Yes", "No"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
km = st.number_input("KM Driven", min_value=0)
owners = st.selectbox("Number of Owners", [1, 2, 3])

fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
imperfections = st.slider("Imperfections (0 = None, 10 = Worst)", 0, 10)
repainted = st.slider("Repainted Parts (0 = None, 10 = All)", 0, 10)
Car_Age = 2025 - year  # Calculate Car Age
KM_per_Year = km / Car_Age # Calculate KM per Year

# Predict
if st.button("Predict Price"):
    input_df = pd.DataFrame([{
        "Manufacturing_year": year,
        "Engine capacity": engine,
        "Spare key": spare_key,
        "Transmission": transmission,
        "KM driven": km,
        "Ownership": owners,
        "Fuel type": fuel,
        "Imperfections": imperfections,
        "Repainted Parts": repainted,
        "KM_per_Year" : KM_per_Year,
        "Car_Age": Car_Age
    }])
    
    prediction = model.predict(input_df)[0]
    st.success(f"Estimated Selling Price: ₹{int(prediction):,}")
