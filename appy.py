import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load('model.pkl')
st.title("HOUSE PRICE PREDICTION APP") 

st.divider() 

st.write("This app uses machine learning for predicting house price with given features of the house. for using the inputs from this UI and then use predict button. In this we can identify the house price related to our comfortability. There are various of thing that we are updgrading to our choice. ")

st.divider() 
bedrooms = st.number_input("Number of bedrooms", min_value = 0, value = 0) 
bathrooms = st.number_input("Number of bathrooms", min_value= 0, value = 0) 
condition = st.number_input("Condition", min_value= 0, value = 3) 
st.divider() 
X = [[bedrooms, bathrooms, condition]] 
predictbutton = st.button("Predict!") 

if predictbutton:
       st.balloons()
       X_array = np.array(X)
       prediction = model.predict(X_array)[0]
       st.write(f"Price prediction is {prediction:,.2f} ")

else: 
    st.write("Enter submit after selecting the price that you want in it. ")