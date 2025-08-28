import os 
import sys

from streamlit.web import cli

def app1():

    sys.argv=("streamlit","run","src\streamlit_app\main1.py")
    cli.main()