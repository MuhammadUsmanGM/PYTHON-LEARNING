import streamlit as st
import random
import time
def toss():
  st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right,rgb(114, 2, 81),rgb(5, 136, 123),#390452);
    }
    
    .css-1d391kg { /* Sidebar background */
        background: linear-gradient(to bottom,rgb(9, 108, 158),rgb(9, 130, 151));
    }
    </style>
    """,
    unsafe_allow_html=True,
)
  st.title("Flip a Coin")
  st.subheader("You can toss and choose weather to win or loose.")
  coin = st.button("Flip a Coin")
  if coin:
        time.sleep(2)
        choice = random.choice(['Head','Tail'])
        st.subheader(choice)
if __name__ == "__main__":
    toss()
