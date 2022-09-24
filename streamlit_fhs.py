import streamlit as st
import joblib
import pandas as pd


st.write("House Price Prediction")

col1, col2 = st.columns(2)
sqft_living = col1.number_input("Enter house living area in sqft", min_value=100.0)
sqft_lot = col2.number_input("Enter house lot area in sqft", min_value=100.0)
bedroom = col1.number_input("Enter number of bedrooms", max_value=15, step=1)
bathroom = col2.number_input("Enter number of bathrooms", min_value=1.0, max_value=10.0, step=0.25)
floor = col1.number_input("Enter number of floors", min_value=1.0, max_value=7.0, step=0.5)
waterfront = col2.selectbox("Does the house has waterfront view?", ['Yes', 'No'])
condition_index = col1.number_input("Enter house condition score", min_value=1, max_value=5, step=1)
condition_index = col2.number_input("Enter house grade score", min_value=1, max_value=13, step=1)

st.button('Predict')

