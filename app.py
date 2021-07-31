import streamlit as st
from donationApp import bookDonation, bloodDonation, foodDonation, firstpage, loginPage
#import streamlit as st
import base64


main_bg = "round-sphere-moving-animated-gif-11.gif"
main_bg_ext = "gif"
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

st.title("Donation")
st.header(" Welcome to the Donation page.")

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
    
