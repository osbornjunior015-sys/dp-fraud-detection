import streamlit as st
import pandas as pd

st.title('🚩 Fraud Detection App')

st.info('This App builds a Fraud Detection')
df = pd.read_csv('https://github.com/osbornjunior015-sys/cleaned-fruad.data')
df
