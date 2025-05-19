import streamlit as st
import numpy as np
import joblib
import tensorflow as tf

# Load model and scaler
model = tf.keras.models.load_model("fraud_model.h5")
scaler = joblib.load("scaler.pkl")

st.title("💳 Credit Card Fraud Detection (CNN + LSTM)")
st.markdown("Enter transaction details to predict fraud:")

# Define inputs (match the final features you used)
v1 = st.number_input("V1", -30.0, 30.0, 0.0)
v2 = st.number_input("V2", -30.0, 30.0, 0.0)
v3 = st.number_input("V3", -30.0, 30.0, 0.0)
v4 = st.number_input("V4", -30.0, 30.0, 0.0)
v5 = st.number_input("V5", -30.0, 30.0, 0.0)
amount = st.number_input("Amount", 0.0, 10000.0, 100.0)

# Collect and scale input
input_data = np.array([[v1, v2, v3, v4, v5, amount]])
input_scaled = scaler.transform(input_data)
input_reshaped = input_scaled.reshape((input_scaled.shape[0], input_scaled.shape[1], 1))

# Predict
if st.button("Check Transaction"):
    prediction = model.predict(input_reshaped)
    predicted_label = (prediction > 0.5).astype("int32")[0][0]

    if predicted_label == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ This transaction seems Safe.")
