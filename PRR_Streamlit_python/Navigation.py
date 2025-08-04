import streamlit as st
from PIL import Image 
pages = {"About us": [st.Page("Main.py", title="Main")],"Register": [st.Page("App.py", title="Book Now!")]}
X = st.navigation(pages)
X.run()
