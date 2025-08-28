import os 
import sys

from streamlit.web import cli

def app():

    sys.argv=("streamlit","run","src\streamlit_app\main.py")
    cli.main()