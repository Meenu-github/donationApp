import streamlit as st
import openpyxl as pxl
import pandas as pd
import gspread
from gspread_dataframe import get_as_dataframe 
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
            role = ['Hospital','Food Distributor','Orphanage']
            selectRole = st.selectbox("Role",role)
            if password== conf_password:
                pass
            else:
                st.info("password do not match with confirm password")
            
        
            sheet.cell(row=maxrow,column=1).value = userName
            sheet.cell(row=maxrow,column=2).value = email
            sheet.cell(row=maxrow,column=3).value = password
            sheet.cell(row=maxrow, column=4).value = selectRole
            

            submissionButton = st.form_submit_button(label="Sign up")
            if submissionButton==True:
                exp.save('proj.xlsx')
                st.success("Successfully sign up")
                type(selectRole)


    if page=='Login':
        with st.form(key="Login"):

            userName = st.text_input("Username")
            password = st.text_input("Password")
            submissionButton = st.form_submit_button(label="Login")
            if submissionButton==True:
                
                for i in range(2, sheet.max_row):
                    if((sheet.cell(row=i, column=2).value == userName)):
                        if((sheet.cell(row=i, column=3).value == password)):
                            y = sheet.cell(row=i,column=4).value
                            st.success('Successfully Login')
                            type(y)
                 
                        else:
                            st.error("either username or password is incorrect")
def type(selectRole):
    if selectRole=='Hospital':
        exp = pxl.load_workbook('BloodDonation.xlsx')
        sheet = exp.active
        maxrow= sheet.max_row+1
        a2 = ['Yes','No']
        b2 = st.radio('Do you want data of blood donor :',a2)
        if b2=='Yes':
            for i in range(1,sheet.max_row+1):
                for j in range(1,sheet.max_column+1):
                    st.text(print(sheet.cell(row=i,column=j).value, end="  "))
                st.text(print("\n"))
        if b2=='No':
            st.info('YOU SELECTED NO.')

    if selectRole=='Food Distributor':
        exp = pxl.load_workbook('FoodDonation.xlsx')
        sheet = exp.active
        maxrow= sheet.max_row+1
        a = ['Yes','No']
        b = st.radio('Do you want data of food donor :',a)
        if b=='Yes':
            for i in range(1,sheet.max_row+1):
                for j in range(1,sheet.max_column+1):
                    st.text(print(sheet.cell(row=i,column=j).value, end="  "))
                st.text(print("\n"))
        if b=='No':
            st.info('YOU SELECTED NO.')

    if selectRole=='Orphanage':
        exp = pxl.load_workbook('BookDonation.xlsx')
        sheet = exp.active
        maxrow= sheet.max_row+1
        a1 = ['Yes','No']
        b1 = st.radio('Do you want data of food donor :',a1)
        if b1=='Yes':
            for i in range(1,sheet.max_row+1):
                for j in range(1,sheet.max_column+1):
                    st.write(sheet.cell(row=i,column=j).value, end="  ")
                st.write("\n")
        if b1=='No':
            st.info('YOU SELECTED NO.')

                    
df = get_as_dataframe(sheet)
st.write(df)
st.table(df)
                            

                

