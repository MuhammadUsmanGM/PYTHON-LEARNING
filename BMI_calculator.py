import streamlit as st
import pandas as pd

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right,rgb(2, 30, 109),rgb(99, 5, 5),rgb(122, 108, 0),rgb(26, 131, 7), #005F69);
    }
    
    .css-1d391kg { /* Sidebar background */
        background: linear-gradient(to bottom,rgb(6, 74, 109),rgb(4, 106, 124));
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.write('Welcome to BMI Calculator')
height=st.slider('Enter your height(in cm): ',20,250,175)
height=float(height)
weight=st.slider('Enter your weight(in kg): ',20,200,70)
weight=float(weight)
bmi=weight/((height/100)**2)

st.subheader(f'Your BMI is {bmi}')

st.write('### BMI Categories ###')
st.info("-->Underweight: BMI less than 18.5")
st.success("*-->Normal Weight: BMI between 18.5 and 24.9*")
st.warning("*-->Overweight: BMI between 25 and 29.9*")
st.error("*-->Obesity: BMI 30 or Greater*")