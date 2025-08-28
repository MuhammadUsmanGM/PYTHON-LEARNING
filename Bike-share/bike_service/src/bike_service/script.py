import os
import sys
from streamlit.web import cli

def app():
    sys.argv=("streamlit","run","src/bike_service/app.py")
    cli.main()