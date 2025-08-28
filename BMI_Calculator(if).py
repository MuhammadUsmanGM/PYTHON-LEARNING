import streamlit as st
import pandas as pd

st.title('Welcome to BMI Calculator')

height=st.slider('Enter your height(in cm): ',100,250,175)

weight=st.slider('Enter your weight(in kg): ',40,200,70)

bmi=weight/((height/100)**2)

st.write(f'Your BMI is {bmi}')

st.write('<-----BMI Conclusion----->')

if bmi<18.5 :
    st.write('Underweight.')
    st.write('You need to focus on your Diet Plan.')
elif bmi>=18.5 and bmi<=24.9:
    st.write('Normal')
    st.write('You BMI looks Perfect. So Stay Focused.')
elif bmi>=25 and bmi<=29.9:
    st.write('Overweight')
    st.write('You should do some workout and lose some Weight.')
elif bmi>=30:
    st.write('Obesity')
    st.write("It's necessary for you to do a lot of workout.")
    st.write('It will be Beneficial for you.')