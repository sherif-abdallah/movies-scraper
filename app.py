from selenium import webdriver
from bs4 import BeautifulSoup
import streamlit as st


hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

form = st.form("my_form")
input = form.text_input("Enter Movie Url from mycima.ws")
# Now add a submit button to the form:
submit =   form.form_submit_button("Submit")
if submit:
    try:
        driver = webdriver.ChromeOptions()
        driver.add_argument('headless')
        driver = webdriver.Chrome(options=driver)
        r = driver.get(input)
        source = driver.page_source
        soup = BeautifulSoup(source, "html.parser")
        soup = str(soup)
        # Get Links
    except:
        st.error('Write a Valid Url')

    try:
        govid_1 = soup.find('https://govid.cyou')
        govid = soup[govid_1:]
        govid = govid[0: govid.index('?')]
        govid = govid.strip(' ')
    except:
        govid = 'N/A'

    try:
        vidbom_1 = soup.find('https://vedbom.org')
        vidbom = soup[vidbom_1:]
        vidbom = vidbom[0: vidbom.index('?')]
        vidbom = vidbom.strip(' ')
    except:
        vidbom = 'N/A'

    try:
        vedshare_1 = soup.find('https://vedshare.com')
        vedshare = soup[vedshare_1:]
        vedshare = vedshare[0: vedshare.index('?')]
        vedshare = vedshare.strip(' ')
    except:
        vedshare = 'N/A'

    try:
        myviid_1 = soup.find('https://myviid.net')
        myviid = soup[myviid_1:]
        myviid = myviid[0: myviid.index('"')]
        myviid = myviid.strip(' ')
    except:
        myviid = 'N/A'

    try:
        uqload_1 = soup.find('https://uqload.com')
        uqload = soup[uqload_1:]
        uqload = uqload[0: uqload.index('?')]
        uqload = uqload.strip(' ')
    except:
        uqload = 'N/A'

    try:
        uptostream_1 = soup.find('https://uptostream.com')
        uptostream = soup[uptostream_1:]
        uptostream = uptostream[0: uptostream.index('?')]
        uptostream = uptostream.strip(' ')
    except:
        uptostream = 'N/A'

    # st.json({'Govid' : govid, 'Vidbom' : vidbom, 'Vedshare' : vedshare, 'myviid' : myviid, 'uqload':uqload, 'uptostream':uptostream})
    st.table([['Govid' , govid], [ 'Vidbom' , vidbom], [ 'Vedshare' , vedshare], [ 'myviid' , myviid], [ 'uqload',uqload], [ 'uptostream',uptostream]])
