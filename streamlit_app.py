import streamlit as st
import pandas as pd
import  joblib


st.title('🚩 Fraud Detection Preadiction App')
st.write("Enter transaction details to check if it's fraudulent.")

st.info('This App builds a Fraud Detection')
df = pd.read_csv('https://raw.githubusercontent.com/osbornjunior015-sys/cleaned-fruad.data/refs/heads/main/cleaned_fraud_data.csv')
df

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT"])
amount = st.number_input("Amount", min_value=0.0)
oldbalanceOrg = st.number_input("Old Sender Balance", min_value=0.0)
newbalanceOrg = st.number_input("New Sender Balance", min_value=0.0)
oldbalanceDest = st.number_input("Old Receiver Balance", min_value=0.0)
newbalanceDest = st.number_input("New Receiver Balance", min_value=0.0)

if st.button("Predict"):
    # Prepare input
    input_data = pd.DataFrame([[transaction_type, amount, oldbalanceOrg, newbalanceOrg, oldbalanceDest, newbalanceDest]],
                              columns=["type","amount","oldbalanceOrg","newbalanceOrg","oldbalanceDest","newbalanceDest"])
    
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ Fraudulent Transaction Detected!")
    else:
        st.success("✅ Transaction is Legitimate.")
