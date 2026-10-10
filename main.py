
import streamlit as st
import pandas as pd
import pickle

with open("parkinsons_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Parkinson's Disease Prediction")
st.write("Enter the voice measurement features below.")

feature_names = [
    "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)",
    "MDVP:Jitter(%)", "MDVP:Jitter(Abs)", "MDVP:RAP",
    "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer",
    "MDVP:Shimmer(dB)", "Shimmer:APQ3", "Shimmer:APQ5",
    "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR",
    "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
]

with st.form("prediction_form"):
    values = []

    for feature in feature_names:
        value = st.number_input(feature, value=0.0, format="%.6f")
        values.append(value)

    submitted = st.form_submit_button("Predict")

if submitted:
    input_data = pd.DataFrame([values], columns=feature_names)
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.warning("Prediction: Parkinson's group pattern")
    else:
        st.success("Prediction: Healthy control group pattern")

    st.caption("Educational demonstration only. This result is not a medical diagnosis.")
