import streamlit as st
import openpyxl
def login():
    with st.form(key="Login"):

        userName = st.text_input("Username")
        password = st.text_input("Password")
        submissionButton = st.form_submit_button(label="Login")
        if submissionButton==True:
            st.success("Successfully login")
def sign_up():
    with st.form(key="Sign up"):
        userName = st.text_input("Username")
        email = st.text_input("E-mail Id")
        password = st.text_input("Password")
        submissionButton = st.form_submit_button(label="Sign up")
        if submissionButton==True:
            st.success("Successfully sign up")
def loginPages():
    st.title("Welcome and login to the page if not registered sign up now")
    col1,col2 = st.beta_columns(2)
    col1 = st.button("Login", on_click=login)
    col2 = st.button("Sign up", on_click=sign_up)
