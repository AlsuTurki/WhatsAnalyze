"""Main module for the streamlit app"""
import streamlit as st
from multipage import MultiPage
from src.pages import home, about


st.set_page_config(
    page_title="تحليل محادثات الواتس اب")    


# Create an instance of the app 
app = MultiPage()

# Title of the main page
#st.title("لوحة معلومات نقاط البيع السعودية")

# Add all your applications (pages) here
app.add_page("الصفحة الرئيسة", home.app)
app.add_page("تقنيات المشروع", about.app)




# The main app
app.run()