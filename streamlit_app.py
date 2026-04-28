import streamlit as st
import pandas as pd
import  joblib


st.title('🚩 Fraud Detection Preadiction App')
st.write("Enter transaction details to check if it's fraudulent.")
with st.expander('Data'):
  st.write('**Raw Data**')
  st.info('This App builds a Fraud Detection')
  df = pd.read_csv('https://raw.githubusercontent.com/osbornjunior015-sys/cleaned-fruad.data/refs/heads/main/cleaned_fraud_data.csv')
  df

  st.write('**X**')
  x = st.drop('step', axis=1)
  x

  st.write('**y**')
  y = df.step
  y




