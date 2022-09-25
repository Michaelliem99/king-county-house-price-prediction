import streamlit as st
import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import xgboost as xgb

st.write("House Price Prediction")

st.number_input("Enter the age of the house:", step=1)
col1, col2 = st.columns(2)
sqft_living = col1.number_input("Enter house living area in sqft", min_value=100.0)
sqft_lot = col2.number_input("Enter house lot area in sqft", min_value=100.0)
bedrooms = col1.number_input("Enter number of bedrooms", max_value=15, step=1)
bathrooms = col2.number_input("Enter number of bathrooms", min_value=1.0, max_value=10.0, step=0.25)
floor = col1.number_input("Enter number of floors", min_value=1.0, max_value=7.0, step=0.5)
waterfront = col2.selectbox("Does the house has waterfront view?", ['Yes', 'No'])
condition = col1.number_input("Enter house condition score", min_value=1, max_value=5, step=1)
grade = col2.number_input("Enter house grade score", min_value=1, max_value=13, step=1)

df_pred = pd.DataFrame({
    'sqft_living15':sqft_living, 'sqft_lot15':sqft_lot, 
    'bedrooms':bedrooms, 'bathrooms':bathrooms, 
    'floor':floor, 'waterfront':waterfront,
    'condition':condition, 'grade':grade
}, index=[0])

waterfront_mapping = {'Yes':1, 'No':0}
df_pred['waterfront'] = df_pred['waterfront'].replace(waterfront_mapping)
    
model = joblib.load('xgb_pipe.sav')
prediction = model.predict(df_pred)

if st.button('Predict'):
    st.write('Your predicted house price is {}'.format(prediction[0]))