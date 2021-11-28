import requests
from bs4 import BeautifulSoup
import streamlit as st
import re


hide_st_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
button[title="View fullscreen"] {
display: none;
}

button[title="View fullscreen"]:hover {
display: none;
}
</style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)



# form = st.form("my_form")
input = st.text_input("Enter Movie Url from arabseed.ws")
# submit = form.form_submit_button("Submit")

# INFO
r = requests.get(input)
soup = BeautifulSoup(r.content, 'html5lib')
title = soup.find('h1', attrs = {'class':'Title'}) 
descrip = soup.find('p', attrs = {'class':'descrip'}) 
RatingImdb = soup.find('div', attrs = {'class':'RatingImdb'}) 
rate = RatingImdb.find('em')
image = soup.find('div', class_="PosterShape")
image = image.attrs.get('data-style')
image = re.search("(?P<url>https?://[^\s]+)", image).group("url")
image = str(image).replace(')', '').replace(';', '')
image = '''
    <style>
    .image{
        width: 200px;
        height: 350px;
    }
    @media screen and (min-width: 800px) {
        .image{
            width: 320px;
            height: 450px;
        }
    }  
    </style>              
    <br><center><img class="image"  src="''' + image + '''" ></center><br>'''
st.markdown(image, unsafe_allow_html=True)
st.write('Title')
st.code(title.text)
st.write('Description')
st.code(descrip.text)
st.write('IMDB Rating')
st.code(rate.text)
MetaTermsInfo = soup.find('div', class_='MetaTermsInfo')
MetaTermsInfo = MetaTermsInfo.find_all('a')
st.table(MetaTermsInfo)



# Watch Servers
r = requests.get(input + '/watch/')
soup = BeautifulSoup(r.content, 'html5lib')
containerServers = soup.find('div', class_='containerServers')
allcontainerServers = containerServers.find_all('li')
option = st.selectbox('Choosse a Server',tuple( range(0, len(allcontainerServers))))


currentvideo = containerServers.find_all("li", {"data-server" : option})
currentvideo = str(currentvideo).replace('[', '').replace(']', '')
videosoup = BeautifulSoup(currentvideo, 'html5lib')

videotitle = videosoup.find('span')
videotitle = str(videotitle.text).replace('p', '').replace('ٍ', '')
st.write('## ' + videotitle)

videosrc = videosoup.find('iframe')
st.code(videosrc['src'])

iframe = '''
    <style>
    .video{
        width: 350px;
        height: 250px;
    }
    @media screen and (min-width: 800px) {
        .video{
            width: 700px;
            height: 400px;
        }
    }  
    </style>              
    <center><iframe class="video"  src="''' + videosrc['src'] + '''"  frameborder="0" ></iframe></center>'''
st.markdown(iframe, unsafe_allow_html=True)


# Download Servers
r = requests.get(input + '/download/')
soup = BeautifulSoup(r.content, 'html5lib')
DownloadArea = soup.find('div', class_='DownloadArea')
downloadserver = DownloadArea.find_all('a')
download_option = st.selectbox('Choosse a Download Server',tuple( range(0, len(downloadserver))))
st.write('Download ' + str(downloadserver[download_option].text).replace('p', '').strip())
st.code(downloadserver[download_option]['href'])


st.caption('Made By [Flix](http://flix.pythonanywhere.com/)')
