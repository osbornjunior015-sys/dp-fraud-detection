import streamlit as st
import pandas as pd
import joblib


model = joblib.load("/content/fraud_detection_pipelie.pkl")
