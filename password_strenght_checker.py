import re
import streamlit as st
import random
import string

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right,#830606,#0C8306,#52057D);
    }
    
    .css-1d391kg { /* Sidebar background */
        background: linear-gradient(to bottom,rgb(9, 108, 158),rgb(9, 130, 151));
    }
    </style>
    """,
    unsafe_allow_html=True,
)

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")
    
    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", feedback
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions above.", feedback

def generate_strong_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

# Streamlit UI
st.title("🔐 Password Strength Meter")
password = st.text_input("Enter your password:", type="password")
if password:
    strength, feedback = check_password_strength(password)
    st.subheader(strength)
    for suggestion in feedback:
        st.write(suggestion)

if st.button("Generate Strong Password"):
    st.write("Suggested Password: ", generate_strong_password())