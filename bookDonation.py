import streamlit as st
def bookdonate() :
    st.markdown("BOOK DONATION")
    st.title("Welcome to the book donation page, your old book can bring light in someones future.\nCome let us donate books for needy one.\nYou don't have to walk and donate it you just have to register yourself and we will pick the book from your house address that will be provided.")
    st.write("Here if you are willing to donate book\n you have to register yourself.")
    with st.form(key="Registration for Blood Donation"):
        bookname = st.text_input("Enter your name : ")
        address = st.text_input("Enter your address please : ")
        bookidProof = st.text_input("Enter your Id Proof Number : ")
        if (bookname and address and bookidProof) == True:
            submissionbook = st.form_submit_button()
            if submissionbook==True:
                st.info("Successfully submitted the form.")
            else:
                st.info("Please submit the form.")

