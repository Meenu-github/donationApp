import streamlit as st
def bloodDonate() :
    st.title("Blood Donation")
    st.write("This is the blood donation page.")
    st.write("Here if you are willing to donate blood\n you have to register yourself.")
    with st.form(key="Registration for Blood Donation"):
        bloodname = st.text_input("Enter your name : ")
        bgrp = st.text_input("Enter your blood group : ")
        age = st.slider(label="Enter your age ", min_value=18, max_value=45)
        bloodidProof =  st.text_input("Enter your Id Proof Number : ")
        if (bloodname and bgrp and age and bloodidProof) == True:
            submissionblood = st.form_submit_button(label="Submit")
            if submissionblood==True:
                st.info("Successfully submitted your data.")
    st.info("Select a date to donate blood in your nearby blood donation center : ")
    
    #adding date picker..

