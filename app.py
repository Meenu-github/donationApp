import streamlit as st
from donationApp import bookDonation, bloodDonation, foodDonation, firstpage

st.markdown("## Welcome to the Donation page.")
st.title("Donation")
st.header("Let us come together and donate something for the needy.")
menu = ["Book Donation", "Blood Donation","Food Donation", "None"]
"""
choice = st.radio("Navigation",["Book Donation", "Blood Donation","Food Donation", "None"])
"""
choice = st.sidebar.selectbox("Menu", menu)
if choice=="Book Donation":
    bookDonation.bookdonate()
if choice=="Blood Donation" :
    bloodDonation.bloodDonate()
if choice=="Food Donation" :
    foodDonation.foodDonate()
if choice == "None" :
    st.text("DO YOU KNOW ?")
    st.text("HOW OLD THIS WEB PAGE IS ?")
    st.text("THIS WEB PAGE IS MADE ON 14 JULY 2021")
    st.text("The contributors to this code are : Meenu, Kaviya, Rebecca, Raghul, Aditya")
