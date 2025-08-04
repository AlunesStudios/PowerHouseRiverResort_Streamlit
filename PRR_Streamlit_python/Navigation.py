import streamlit as st
from PIL import Image
Main_Image = Image.open("PRR_Main_Image.png")
st.set_page_config(page_icon=Main_Image, page_title="PowerHouse River Resort", layout="centered")
st.logo(Main_Image)
pages = {"About us": [st.Page("Main.py", title="Main")],"Register": [st.Page("App.py", title="Book Now!")]}
X = st.navigation(pages)
X.run()