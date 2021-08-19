import streamlit as st
from donationApp import bookDonation, bloodDonation, foodDonation, firstpage, loginPage
import base64
from gtts import gTTS
import os    

tts = gTTS(text="Hi user, This is your guide of the donation app, you are now at the donation app home page, you can donate food, blood and books here and if you are a distributor of these things then you can register yourself and fetch the data of donor and get the donation and then distribute it.", lang='en')
tts.save("pcvoice.mp3")
# to start the file from python
os.system("start pcvoice.mp3")



main_bg = "bg.jpg"
main_bg_ext = "jpg"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
        
    }}
    </style>
    """,
    unsafe_allow_html=True
)

video_file = open('Quickstart to Donation App.webm', 'rb') #rb opens the file in binary format for reading
video_bytes = video_file.read()
st.markdown("<h1 style='text-align: left; color: greenyellow;'>Quickstart to the donation app 👇</h1>", unsafe_allow_html=True)

st.video(video_bytes, format="video/mp4", start_time=0)
st.markdown("<h1 style='text-align: left; color: greenyellow;'>Donation</h1>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: left; color: greenyellow;'>Welcome to the Donation page.</h1>", unsafe_allow_html=True)



st.subheader("Let us come together and donate something for the needy.")
menu = ["None", "Book Donation", "Blood Donation","Food Donation","Organization Login/Register"]

choice = st.selectbox("Navigation", menu)
if choice=="Book Donation" :
    bookDonation.bookdonate()
if choice=="Blood Donation" :
    bloodDonation.bloodDonate()
if choice=="Food Donation" :
    foodDonation.foodDonate()
if choice == "None" :
    firstpage.firstpage()
    st.text("DO YOU KNOW ?")
    st.text("HOW OLD THIS WEB PAGE IS ?")
    st.text("THIS WEB PAGE IS MADE ON 14 JULY 2021")
if choice== "Organization Login/Register":
    loginPage.loginPages()
    
