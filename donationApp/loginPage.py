import streamlit as st
import openpyxl as pxl
import pandas as pd
#proj = pd.read_excel('proj.xlsx')
exp = pxl.load_workbook('proj.xlsx')
sheet = exp.active
maxrow= sheet.max_row+1
#sheet = exp['Sheet1']
def loginPages():
    page_name = ['Register', 'Login']
    page = st.radio('Choose Register/Login', page_name)
    if page =='Register':
        with st.form(key="Sign up"):
            userName = st.text_input("Username")
            email = st.text_input("E-mail Id")
            password = st.text_input("Password")
            conf_password = st.text_input('Confirm your password')
        
            sheet.cell(row=maxrow,column=1).value = userName
            sheet.cell(row=maxrow,column=2).value = email
            sheet.cell(row=maxrow,column=3).value = password
            

            submissionButton = st.form_submit_button(label="Sign up")
            if submissionButton==True:
                exp.save('proj.xlsx')
                st.success("Successfully sign up")


    if page=='Login':
        with st.form(key="Login"):

            userName = st.text_input("Username")
            password = st.text_input("Password")
            submissionButton = st.form_submit_button(label="Login")
            if submissionButton==True:
                proj = pd.read_excel('proj.xlsx',index_col=1)
                if userName in proj:
                    pas = pd.read_excel('proj.xlsx',index_col=2)
                    if password in pas:
                        st.success('Data found')

                st.success("Successfully login")

