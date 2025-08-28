import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right,rgb(114, 2, 81),rgb(5, 136, 123));
    }
    
    .css-1d391kg { /* Sidebar background */
        background: linear-gradient(to bottom,rgb(9, 108, 158),rgb(9, 130, 151));
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Conversion factors
conversion_factors = {
    "Length": {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701,
    },
    "Weight": {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1000000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    },
    "Temperature": {
        "Celsius": "celsius",
        "Fahrenheit": "fahrenheit",
        "Kelvin": "kelvin",
    }
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return value * 9/5 + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
    return value

def convert(value, from_unit, to_unit, category):
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    else:
        return value * (conversion_factors[category][to_unit] / conversion_factors[category][from_unit])

st.title("Google-Like Unit Converter")

# Select conversion category
category = st.selectbox("Select category", list(conversion_factors.keys()))

# Select units
from_unit = st.selectbox("From", list(conversion_factors[category].keys()))
to_unit = st.selectbox("To", list(conversion_factors[category].keys()))

# Input value
value = st.number_input("Enter value", format="%.5f")

# Convert and display
if st.button("Convert"):
    result = convert(value, from_unit, to_unit, category)
    st.success(f"{value} {from_unit} = {result:.5f} {to_unit}")
