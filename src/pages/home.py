"""Home page shown when the user enters the application"""
from numpy.lib.shape_base import expand_dims
import streamlit as st
from pathlib import Path
from analysis_functions import *
from functions import *
from PIL import Image
image = Image.open('./img/HowTo.jpg')




#about project

def read_markdown_file(markdown_file):
    return Path(markdown_file).read_text(encoding="utf8")
#intro_markdown = read_markdown_file(r"C:\Users\talsughayyir\Desktop\pos 0.4\ABOUT.md")

# pylint: disable=line-too-long
def app():
    """Used to write the page in the app.py file"""
    hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
    st.markdown(hide_menu_style, unsafe_allow_html=True)
    title = """
    <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans+Arabic&display=swap" rel="stylesheet" type="text/css"/>
    <style> bdi {font-family: 'IBM Plex Sans Arabic';}
    div { direction: LTR; text-align: center;
    .css-hi6a2p {padding-top: 0rem;}

    </style>
    <div><h2><bdi>تحليل محادثات الواتس اب</bdi></h2></div>
    """
    st.write(title , unsafe_allow_html=True, )
    with st.spinner("Loading Home ..."):
        intro_markdown = read_markdown_file('./ABOUT.md')
        st.markdown(intro_markdown, unsafe_allow_html=True)

    st.image(image, caption='How To Export A chat')

    uploaded_file = st.file_uploader("ارفع الملف النصي!", type=['txt'])
    if st.button("بدء التحليل"):
        ts = T.time()
        chat = str(uploaded_file.read(),"utf-8")

        df, df_extended = crawl_the_chat(chat)
        df_summary = chat_summary(df)


        media_per_contact(df,sort=True, plot=True)
        daily_msgs(df)
        average_words_per_message_per_contact(df_extended,sort=True, plot=True)
        msgs_per_weekday(df_extended, sort=True, plot=True)
        msgs_per_hour(df_extended, plot=True)
        msgs_per_month(df_extended, plot=True)
        msgs_per_year(df_extended, sort=False, plot=True)
        emojis_per_user(df, sort=True, plot=True)
        msgs_per_contact(df_extended, sort=True, plot=True)
        words_per_contact( df_extended, sort=True, plot=True)
        emojis_per_msg_per_contact( df_extended, sort=True, plot=True)


        st.write("Time spent: ", np.round(T.time() - ts, 2), "secs")