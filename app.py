import streamlit as st
import numpy as np
import pandas as pd
import joblib

#load the joblib
model = joblib.load("co2_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("🌍 Agri-Food CO₂ Emissions Predictor")
st.write("""
Enter values for the top 5 features below (in kilotones).  
All emissions in this dataset are recorded in kilotones: 1 kt = 1,000 kg.
""")

all_features = scaler.feature_names_in_
default_values = np.zeros(len(all_features))

top_features = [
    'Agrifood Systems Waste Disposal',
    'Manure left on Pasture',
    'Urban population',
    'IPPU',
    'Food Household Consumption'
]

user_input = default_values.copy()


with st.form(key='input_form'):
    input_values = []
    
    for f in top_features:
        val_str = st.text_input(f"Enter value for {f} (kt):", value="0")
        input_values.append(val_str)

    submit_button = st.form_submit_button(label='Predict Emissions')

if submit_button:
    for i, f in enumerate(top_features):
        idx = list(all_features).index(f)
        try:
            val = float(input_values[i])
        except ValueError:
            val = 0.0 
        user_input[idx] = val

    user_array = np.array(user_input).reshape(1, -1)
    scaled_input = scaler.transform(user_array)

    user_df = pd.DataFrame(scaled_input, columns=scaler.feature_names_in_)

    # Predict CO2 emissions
    prediction = model.predict(user_df)[0]

    st.success(f"Predicted CO₂ Emissions: {prediction:.2f} kt")
