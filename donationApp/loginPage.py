from donationApp.bloodDonation import addData
import streamlit as st
import pandas as pd
import base64
import sys
import pyodbc as odbc

DRIVER = "SQL Server"
SERVER_NAME = "MEENU\SQLEXPRESS"
DATABASE_NAME="StreamLit"
cnxn = f"""
    Driver={{{DRIVER}}};
    Server={SERVER_NAME};
    Database={DATABASE_NAME};
    Trusted_Connection=yes;
"""

records = []

def type(selectRole):
    st.title("Blood Donation")
    main_bg = "black-and-white-gif-background-8.gif"
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
    if selectRole == 'Hospital':

        tabl = pd.read_sql_query('SELECT * From Blood_Donation',DRIVER)
        st.write(tabl)
    
    if selectRole == 'Food Distributor':
        
        tabl = pd.read_sql_query('SELECT * From Food_Donation',DRIVER)
        st.write(tabl)
        

    if selectRole == 'Orphanage':
      
        tabl = pd.read_sql_query('SELECT * From Book_Donation',DRIVER)
        st.table(tabl)
        


def loginPages():
    st.title("Blood Donation")
    main_bg = "black-and-white-gif-background-8.gif"
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
                      
            submissionButton = st.form_submit_button(label="Sign up")
            if submissionButton == True:
              
                records.append([userName,email,password,selectRole])
                st.success("Successfully sign up")

                addData()
                
                st.info('Giving data of donor')

                type(selectRole)
                
                

    if page == 'Login' :
        with st.form(key="Login") :

            userName = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submissionButton = st.form_submit_button(label="Login")
            if submissionButton == True:
                match = """
                    SELECT Orole FROM Organization WHERE email==userName AND pass==password
                    """

                if match==True:
                    type(match)
                            
                            
                            

            else:
                st.error(
                    "either username or password is incorrect")

def addData():
    try:
        conn = odbc.connect(cnxn)
    except Exception as e:
        print(e)
        print("task is terminated")
        sys.exit()
    else:
        cursor = conn.cursor()
    insert_statement = """
        INSERT INTO Organization
        VALUES (?, ?, ?, ?)
    """
    try:
        for record in records:
            print(record)
            cursor.execute(insert_statement, record)
    except Exception as e:
        cursor.rollback()
        print(e)

    else:
        print("Successfully inserted")
        cursor.commit()
        cursor.close()

    



