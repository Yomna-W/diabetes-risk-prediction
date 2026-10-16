import streamlit as st
import pickle
import pandas as pd

# Load the pickled pipeline
with open("diabetes_rf_pipeline.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Diabetes Risk Prediction")
st.write("Enter patient details to predict diabetes risk:")

# User inputs
gender = st.selectbox("Gender:", ["Male", "Female"])
age = st.number_input("Age (years):", min_value=0.0, max_value=120.0, value=30.0, step=0.5)
hypertension = st.radio("Hypertension?:", (0, 1), index=1)
heart_disease = st.radio("Heart disease?:", (0, 1), index=0)

smoking_options = ["never", "No Info", "current", "former", "ever", "not current"]
raw_smoke = st.selectbox("Smoking history:", smoking_options)
if raw_smoke in ["never", "No Info"]:
    smoking_history = "non-smoker"
elif raw_smoke == "current":
    smoking_history = "current"
else:
    smoking_history = "past_smoker"

bmi = st.number_input("BMI:", min_value=10.0, max_value=60.0, value=28.4, step=0.1)
hba1c = st.number_input("HbA1c level:", min_value=3.0, max_value=15.0, value=7.2, step=0.1)
blood_glucose = st.number_input("Blood glucose level:", min_value=0, max_value=500, value=140, step=1)

if st.button("Predict"):
    sample = pd.DataFrame([{
        "gender": gender,
        "age": age,
        "hypertension": hypertension,
        "heart_disease": heart_disease,
        "smoking_history": smoking_history,
        "bmi": bmi,
        "HbA1c_level": hba1c,
        "blood_glucose_level": blood_glucose
    }])
    
    pred_label = int(model.predict(sample)[0])
    pred_prob = float(model.predict_proba(sample)[0, 1])
    
    label_str = "Diabetic (1)" if pred_label == 1 else "Non-diabetic (0)"
    st.subheader(f"Prediction: {label_str}")
    st.write(f"Probability of diabetes: {pred_prob:.2f}")