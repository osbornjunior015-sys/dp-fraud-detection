import streamlit as st
import pandas as pd
import  joblib

model = joblib.load("fraud_model.pkl")

st.title('🚩 Fraud Detection Preadiction App')
st.write("Enter transaction details to check if it's fraudulent.")
st.info('This App builds a Fraud Detection')
df = pd.read_csv('https://raw.githubusercontent.com/osbornjunior015-sys/cleaned-fruad.data/refs/heads/main/cleaned_fraud_data.csv')
df
