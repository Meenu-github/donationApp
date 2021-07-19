import streamlit as st
import openpyxl
def loginPages():
    def login():
        with st.form("Login"):
            username = st.text_input("Username")
            passwd = st.text_input("Password")
            st.form_submit_button("Login")
            if st.form_submit_button==True:
                st.success("Successfully login")
    def sign_up():
        with st.form("Sign up"):
            username = st.text_input("Username")
            email = st.text_input("E-mail Id")
            passwd = st.text_input("Password")
            st.form_submit_button("Sign up")
            if st.form_submit_button==True:
                st.success("Successfully sign up")
    st.title("Welcome and login to the page if not registered sign up now")
    col1,col2 = st.beta_columns(2)
    col1 = st.button("Login", on_click=login)
    col2 = st.button("Sign up", on_click=sign_up)
