import streamlit as st
import openpyxl as pxl
import pandas as pd

#import gspread
#from gspread_dataframe import get_as_dataframe 
#proj = pd.read_excel('proj.xlsx')
#exp = pxl.load_workbook('proj.xlsx')

projDemo = pd.read_excel('../donationApp/proj.xlsx')
exp = pxl.load_workbook('../donationApp/proj.xlsx')
sheet = exp.active
maxrow = sheet.max_row+1
#sheet = exp['Sheet2']

def type(selectRole):
    if selectRole == 'Hospital':
        exp = pd.read_excel('../donationApp/BloodDonation.xlsx')
        new = pxl.load_workbook('../donationApp/BloodDonation.xlsx')
        newsheet = new.active
        #sheet = exp.active
        #maxrow = sheet.max_row+1
        
        blooddata = ['Yes, I want Blood Donor data', 'No, I want Blood Donor data']
        b = st.selectbox('Do you want data of blood donor :', blooddata, key='1')
        if b == 'Yes, I want Blood Donor data':
            st.table(exp)
        if b == 'No, I want Blood Donor data':
            st.info('YOU SELECTED NO.')

    if selectRole == 'Food Distributor':
        exp1 = pd.read_excel('../donationApp/FoodDonation.xlsx')
        new = pxl.load_workbook('../donationApp/FoodDonation.xlsx')
        newsheet = new.active
        #sheet = exp1.active
        #maxrow = sheet.max_row+1
        
        fooddata = ['Yes, I want Food Donor data', 'No, I don\'t Want Food Donor data']
        b1 = st.selectbox('Do you want data of food donor :', fooddata, key='2')
        if b1 == 'Yes, I want Food Donor data':
            st.table(exp1)
        if b1 == 'No, I don\'t Want Food Donor data':
            st.info('YOU SELECTED NO.')

    if selectRole == 'Orphanage':
        exp2 = pd.read_excel('../donationApp/BookDonation.xlsx')
        new = pxl.load_workbook('../donationApp/BookDonation.xlsx')
        newsheet = new.active
        #sheet = exp2.active
        #maxrow = sheet.max_row+1
        
        bookdata = ['Yes, I want book donor data', 'No, I dont want book donor data']
        b2 = st.selectbox('Do you want data of book donor :', bookdata, key= '3' )
        if b2 == 'Yes, I want book donor data':
            st.table(exp2)
        if b2 == 'No, I dont want book donor data':
            st.info('YOU SELECTED NO.')


def loginPages():
    page_name = ['Register', 'Login']
    page = st.radio('Choose Register/Login', page_name)
    if page == 'Register':
        with st.form(key="Sign up"):
            userName = st.text_input("Username")
            email = st.text_input("E-mail Id")
            password = st.text_input("Password", type="password")
            conf_password = st.text_input('Confirm your password', type="password")
            role = ['Hospital', 'Food Distributor', 'Orphanage']
            selectRole = st.selectbox("Role", role)
            if password == conf_password:
                pass
            else:
                st.warning("password do not match with confirm password")
               

            sheet.cell(row=maxrow, column=1).value = userName
            sheet.cell(row=maxrow, column=2).value = email
            sheet.cell(row=maxrow, column=3).value = password
            sheet.cell(row=maxrow, column=4).value = selectRole

            submissionButton = st.form_submit_button(label="Sign up")
            if submissionButton == True:
                exp.save('../donationApp/proj.xlsx')
                st.success("Successfully sign up")
                type(selectRole)

    if page == 'Login' :
        with st.form(key="Login"):

            userName = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submissionButton = st.form_submit_button(label="Login")
            if submissionButton == True:

                for i in range(2, sheet.max_row):
                    if((sheet.cell(row=i, column=2).value == userName)):
                        if((sheet.cell(row=i, column=3).value == password)):
                            y = sheet.cell(row=i, column=4).value
                            st.success('Successfully Login')
                            
                            type(y)

                        else:
                            st.error(
                                "either username or password is incorrect")




#st.table(projDemo)

# for i in range(1, sheet.max_row+1):
#     for j in range(1, sheet.max_column+1):
#         st.write(sheet.cell(row=i, column=j).value, end="  ")
