import requests
from bs4 import BeautifulSoup
import streamlit as st
import pyperclip
# Making a GET request



hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

form = st.form("my_form")
input = form.text_input("Enter Movie Url from shahed4u.land")


# Now add a submit button to the form:
submit =   form.form_submit_button("Submit")

if submit:


    try:
        r = requests.get(input)
        soup = BeautifulSoup(r.content, 'html.parser')
        vidhd = str(soup)
        vidhd_1 = vidhd.find('https://vidhd.fun')
        vidhd = vidhd[vidhd_1:]
        vidhd = vidhd[0: vidhd.index('"')]
        pyperclip.copy(vidhd)
        st.code(vidhd)


    except:
        st.error('Cant Find Vidhd Link')

st.caption('Made By [Flix](http://flix.pythonanywhere.com/)')