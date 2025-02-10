# Importing Necessary Libraries
import numpy as np
import pandas as pd
import pickle as pkl
import streamlit as st

# Load the trained model
model = pkl.load(open('C:/Users/Administrator/My_Journey/Machine Learning Projects/MISPM.pkl', 'rb'))  # Ensure file name is correct

# Streamlit App Header
st.header("Medical Insurance Premium Predictor")

# User Inputs
gender = st.selectbox("Choose Gender", ['Female', 'Male'])
region = st.selectbox("Choose Region", ['SouthEast', 'SouthWest', 'NorthEast', 'NorthWest'])
smoker = st.selectbox("Are you a smoker?", ['Yes', 'No'])
age = st.slider("Enter Age", 5, 80)
bmi = st.slider("Enter BMI", 5, 100)
children = st.slider("Choose No of Children", 0, 8)  # Fixed range

# Convert categorical variables
smoker = 1 if smoker == 'Yes' else 0

region_dict = {'SouthEast': 0, 'SouthWest': 1, 'NorthEast': 2, 'NorthWest': 3}
region = region_dict[region]

gender = 1 if gender == 'Male' else 0  # Encoding gender

# Prepare input data
input_data = np.array([[age, gender, bmi, children, smoker, region]])

# Prediction
if st.button("Predict"):
    predicted_prem = model.predict(input_data)
    display_string = f"Insurance Premium will be {round(predicted_prem[0], 0)} USD"
    display_inr = f"Insurance Premium will be {round(predicted_prem[0]*87.45, 0)} INR"
    st.markdown(display_string)
    st.markdown(display_inr)
