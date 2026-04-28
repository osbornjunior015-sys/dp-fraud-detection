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
  x = df.drop('amount', axis=1)
  x

  st.write('**y**')
  y = df.amount
  y

with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x='oldbalanceOrg', y='newbalanceOrig', color='amount')

#Data preparation
with st.sidebar:
  st.header('Input features')
  Transaction_type= st.selectbox('Transaction_type', ('type_TRANSFER', 'type_PAYMENT', 'type_DEBIT', 'type_CASH_OUT'))
Amount= st.selectbox('Amount', ('old_sender_balance', 'New_sender_balance', 'Old_receiver_balance', 'New_receiver_balance'))
