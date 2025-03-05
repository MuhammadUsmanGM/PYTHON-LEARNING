import streamlit as st
import pandas as pd
print('Welcome to BMI Calculator')
height=st.slider('Enter your height(in cm): ',20,250,175)
height=float(height)
weight=st.slider('Enter your weight(in kg): ',20,200,70)
weight=float(weight)
bmi=weight/((height/100)**2)

st.write(f'YOur BMI is {bmi}')

st.write('### BMI Categories ###')
st.info("-->Underweight: BMI less than 18.5")
st.success("-->Normal Weight: BMI between 18.5 and 24.9")
st.warning("-->Overweight: BMI between 25 and 29.9")
st.error("-->Obesity: BMI 30 or Greater")