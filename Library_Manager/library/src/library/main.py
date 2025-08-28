import streamlit as st
import json
import os

LIBRARY_FILE = "library.txt"

st.markdown(
    """
    <style>
    /* Background for the main app */
    .stApp {
        background: linear-gradient(to right, rgb(2, 30, 109), rgb(99, 5, 5), rgb(122, 108, 0), rgb(26, 131, 7), #005F69);
    }
    
    /* Background for the sidebar */
    .stSidebar {
        background: linear-gradient(to bottom, rgb(6, 74, 109), rgb(4, 106, 124));
    }

    /* Ensuring sidebar elements follow the new background */
    section[data-testid="stSidebar"] {
        background: linear-gradient(to bottom, rgb(6, 74, 109), rgb(4, 106, 124));
    }

    /* Styling input fields in Streamlit */
    div[data-baseweb="input"] {
        background-color: #222 !important;  /* Dark gray background */
        border-radius: 10px !important;
    }

    div[data-baseweb="input"] > div {
        background-color: #333 !important;  /* Slightly lighter gray */
        color: #ffffff !important;  /* White text */
        border: 2px solid #f39c12 !important;  /* Orange border */
        border-radius: 10px !important;
        padding: 10px !important;
    }

    /* Styling select dropdowns */
    div[data-baseweb="select"] > div {
        background-color: #333 !important;
        color: #fff !important;
        border: 2px solid #f39c12 !important;
    }

    /* Styling text area */
    textarea {
        background-color: #333 !important;
        color: white !important;
        border: 2px solid #f39c12 !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }

    /* Styling number input (for publication year) */
    input[type="number"] {
        background-color: #333 !important;
        color: white !important;
        border: 2px solid #f39c12 !important;
        border-radius: 10px !important;
        padding: 10px !important;
    }

    /* Styling buttons */
    button {
        background-color: #f39c12 !important;  /* Orange background */
        color: white !important;
        border-radius: 10px !important;
        padding: 12px !important;
        font-weight: bold !important;
        border: none !important;
    }

    /* Change button hover effect */
    button:hover {
        background-color: #e67e22 !important;  /* Lighter orange */
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# Functions to handle file I/O
def load_library():
    if os.path.exists(LIBRARY_FILE):
        try:
            with open(LIBRARY_FILE, "r") as f:
                data = f.read()
                if data:
                    return json.loads(data)
        except Exception as e:
            st.error(f"Error loading library: {e}")
    return []

def save_library(library):
    try:
        with open(LIBRARY_FILE, "w") as f:
            json.dump(library, f, indent=4)
    except Exception as e:
        st.error(f"Error saving library: {e}")

# Initialize session state for library if not already set
if "library" not in st.session_state:
    st.session_state.library = load_library()

# Sidebar menu
st.sidebar.title("Personal Library Manager")
menu = st.sidebar.radio("Go to", ("Add a Book", "Remove a Book", "Search for a Book", "Display All Books", "Display Statistics"))

# Function to display all books in a formatted table
def display_books(library):
    if not library:
        st.info("Your library is empty.")
        return
    for idx, book in enumerate(library, start=1):
        status = "Read" if book["read"] else "Unread"
        st.write(f"**{idx}. {book['title']}** by {book['author']} ({book['publication_year']}) - *{book['genre']}* - {status}")

# Add a Book
if menu == "Add a Book":
    st.header("Add a New Book")
    title = st.text_input("Enter the book title:")
    author = st.text_input("Enter the author:")
    pub_year = st.number_input("Enter the publication year:", step=1, format="%i")
    genre = st.text_input("Enter the genre:")
    read_input = st.radio("Have you read this book?", ("Yes", "No"))
    if st.button("Add Book"):
        if title and author and genre and pub_year:
            book = {
                "title": title,
                "author": author,
                "publication_year": int(pub_year),
                "genre": genre,
                "read": True if read_input.lower() == "yes" else False
            }
            st.session_state.library.append(book)
            save_library(st.session_state.library)
            st.success("Book added successfully!")
        else:
            st.warning("Please fill out all fields.")

# Remove a Book
elif menu == "Remove a Book":
    st.header("Remove a Book")
    title_to_remove = st.text_input("Enter the title of the book to remove:")
    if st.button("Remove Book"):
        removed = False
        for book in st.session_state.library[:]:
            if book["title"].lower() == title_to_remove.lower():
                st.session_state.library.remove(book)
                removed = True
                save_library(st.session_state.library)
                st.success("Book removed successfully!")
                break
        if not removed:
            st.error("Book not found.")

# Search for a Book
elif menu == "Search for a Book":
    st.header("Search for a Book")
    search_by = st.radio("Search by:", ("Title", "Author"))
    query = st.text_input(f"Enter the {search_by.lower()}:")
    if st.button("Search"):
        if query:
            if search_by == "Title":
                matching = [book for book in st.session_state.library if query.lower() in book["title"].lower()]
            else:
                matching = [book for book in st.session_state.library if query.lower() in book["author"].lower()]
            if matching:
                st.write("**Matching Books:**")
                display_books(matching)
            else:
                st.info("No matching books found.")
        else:
            st.warning("Please enter a search query.")

# Display All Books
elif menu == "Display All Books":
    st.header("Your Library")
    display_books(st.session_state.library)

# Display Statistics
elif menu == "Display Statistics":
    st.header("Library Statistics")
    total_books = len(st.session_state.library)
    if total_books == 0:
        st.info("No books in the library to display statistics.")
    else:
        read_count = sum(1 for book in st.session_state.library if book["read"])
        percentage_read = (read_count / total_books) * 100
        st.write(f"**Total books:** {total_books}")
        st.write(f"**Percentage read:** {percentage_read:.1f}%")

# Option to manually save library (if needed)
if st.sidebar.button("Save Library Now"):
    save_library(st.session_state.library)
    st.sidebar.success("Library saved!")
