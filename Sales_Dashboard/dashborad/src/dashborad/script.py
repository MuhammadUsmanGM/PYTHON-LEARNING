import os 
import sys

from streamlit.web import cli

def app():
    sys.argv=("streamlit","run","src/dashborad/app.py")
    cli.main()