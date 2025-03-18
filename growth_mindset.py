import streamlit as st
import random

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

def get_growth_mindset_challenge():
    challenges = [
        "🌱 Learn a new skill for 10 minutes today.",
        "💡 Embrace failure: Reflect on a past mistake and what you learned from it.",
        "📚 Read an inspiring article or book on personal growth.",
        "📝 Write down three things you're grateful for today.",
        "🎯 Set a small goal and take the first step towards it.",
        "🤔 Step out of your comfort zone: Try something new today.",
        "👂 Ask for feedback and use it as a tool for improvement.",
        "🌟 Encourage someone else to adopt a growth mindset."
    ]
    return random.choice(challenges)

# Streamlit UI
st.title("🚀 Growth Mindset Challenge")
st.write("Click the button below to get a challenge that will help you develop a growth mindset!")

if st.button("Give Me a Challenge!"):
    challenge = get_growth_mindset_challenge()
    st.subheader(challenge)

st.write("Remember: Growth comes from persistence, effort, and learning from challenges! 💪")
