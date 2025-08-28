import random

import streamlit as st

st.title("Adventure Game")
st.header("Welcome to the Adventure Game")
st.subheader("Enjoy the Endless Adventure")

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right,rgb(0, 68, 255), #FF4B4B, #FFE306, #2EF309);
    }
    
    .css-1d391kg { /* Sidebar background */
        background: linear-gradient(to bottom, #0284C7,rgb(13, 219, 255));
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "inventory" not in st.session_state:
    st.session_state.inventory = []
if "health" not in st.session_state:
    st.session_state.health = 100
if "location" not in st.session_state:
    st.session_state.location = "Choose"
if "game_over" not in st.session_state:
    st.session_state.game_over = False

col1, col2 = st.columns(2)
with col1:
    st.metric("Health", st.session_state.health)
with col2:
    st.write(
        "Inventory:",
        (
            ", ".join(st.session_state.inventory)
            if st.session_state.inventory
            else "Empty"
        ),
    )

# Game over handling
if st.session_state.game_over:
    if st.button("Restart Game"):
        st.session_state.health = 100
        st.session_state.inventory = []
        st.session_state.location = "Choose"
        st.session_state.game_over = False
        st.experimental_rerun()

user = st.selectbox(
    "Choose a Location",
    ["Choose", "Forest", "River", "Cave", "Quit"],
    key="location_radio",
    disabled=st.session_state.game_over,
)


def check_health():
    if st.session_state.health <= 0:
        st.session_state.game_over = True
        st.error("You Died...")
        st.error("You lost your inventory...")
        st.session_state.inventory = []
        return True
    return False


if user == "Forest":
    st.write("You are in a Forest.")
    st.write("You are in front of a lion.")

    lion = st.radio(
        "You wanna fight the lion",
        ["Choose", "Yes", "No"],
        key="lion_radio",
    )

    if lion == "Yes":
        st.write("You are having a great fight.")
        damage = random.randint(0, 40)
        st.session_state.health -= damage

        if not check_health():
            st.write(f"You got a damage of {damage}")
            st.write(f"Your Health: {st.session_state.health}")
            st.write("After defeating lion, You found a Glowing Crystal")

            crystal = st.radio(
                "You wanna collect Glowing Crystal?",
                ["Choose", "Yes", "No"],
                key="crystal_radio",
            )

            if crystal == "Yes":
                if "Glowing Crystal" not in st.session_state.inventory:
                    st.session_state.inventory.append("Glowing Crystal")
                    st.success("Glowing Crystal added to your inventory!")
            elif crystal == "No":
                st.write("You missed the treasure of your fate.")

    elif lion == "No":
        st.write("You escaped from your fate.")

elif user == "Cave":
    st.write("You entered in a Cave.")
    st.write("A bear is ready to have you for dinner.")

    bear = st.radio(
        "You wanna fight with bear?",
        ["Choose", "Yes", "No"],
        key="bear_radio",
    )

    if bear == "Yes":
        st.write("You are having a fight with bear.")
        damage = random.randint(0, 40)
        st.session_state.health -= damage

        if not check_health():
            st.write(f"You got a damage of {damage}")
            st.write(f"Your Health: {st.session_state.health}")
            st.write("You found a Piece of valuable gold!")

            gold = st.radio(
                "You wanna collect the gold?",
                ["Choose", "Yes", "No"],
                key="gold_radio",
            )

            if gold == "Yes":
                if "Piece of valuable gold" not in st.session_state.inventory:
                    st.session_state.inventory.append("Piece of valuable gold")
                    st.success("Gold added to your inventory!")
            elif gold == "No":
                st.write("You missed a valuable item.")

    elif bear == "No":
        st.write("You escaped from your fate.")

elif user == "River":
    st.write("You arrived at a rushing River.")
    st.write("A giant crocodile emerges from the water!")

    crocodile = st.radio(
        "Do you want to face the crocodile?",
        ["Choose", "Yes", "No"],
        key="crocodile_radio",
    )

    if crocodile == "Yes":
        st.write("You engage in a fierce battle with the crocodile.")
        damage = random.randint(0, 35)
        st.session_state.health -= damage

        if not check_health():
            st.write(f"You took {damage} damage")
            st.write(f"Your Health: {st.session_state.health}")
            st.write("You found a Magical Pearl in the river bed!")

            pearl = st.radio(
                "Do you want to take the Magical Pearl?",
                ["Choose", "Yes", "No"],
                key="pearl_radio",
            )

            if pearl == "Yes":
                if "Magical Pearl" not in st.session_state.inventory:
                    st.session_state.inventory.append("Magical Pearl")
                    st.success("Magical Pearl added to your inventory!")
            elif pearl == "No":
                st.write("You left the mysterious pearl behind.")

    elif crocodile == "No":
        st.write("You carefully backed away from the river.")

elif user == "Quit":
    st.write("You are quitting the game...")
    st.write("Thanks for playing")
    st.stop()

elif user == "Choose":
    st.info("Please select a location...")
