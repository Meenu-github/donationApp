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
    #st.title("Blood Donation")
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
        st.success("Data of blood donor")
        conn = odbc.connect(cnxn)
        cursor = conn.cursor()
        tabl = 'SELECT * From Blood_Donation'
        cursor.execute(tabl)
        output = cursor.fetchall()
        for x in output:
            st.write(x)
        cursor.close()
    
    if selectRole == 'Food Distributor':
        st.success("Data of food donor")
        conn = odbc.connect(cnxn)
        cursor = conn.cursor()
        tab2 = 'SELECT * From Food_Donation'
        cursor.execute(tab2)
        output = cursor.fetchall()
        for x in output:
            st.write(x)
        cursor.close()
        

    if selectRole == 'Orphanage':
        st.success("Data of book donor")
        conn = odbc.connect(cnxn)
        cursor = conn.cursor()
        tab3 = 'SELECT * From Book_Donation'
        cursor.execute(tab3)
        output = cursor.fetchall()
        for x in output:
            st.write(x)
        cursor.close()
        #tabl = pd.read_sql_query('SELECT * From Book_Donation',DRIVER)
        #st.table(tabl)
        


def loginPages():
    #st.title("Blood Donation")
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
            passw = st.text_input("Password", type="password")
            conf_password = st.text_input('Confirm your password', type="password")
            role = ['Hospital', 'Food Distributor', 'Orphanage']
            selectRole = st.selectbox("Role", role)
            if passw == conf_password:
                pass
            else:
                st.warning("password do not match with confirm password")
                      
            submissionButton = st.form_submit_button(label="Sign up")
            if submissionButton == True:
              
                records.append([userName,email,passw,selectRole])
                st.success("Successfully sign up")

                addData()
                
                st.info('Giving data of donor')

                type(selectRole)
                
                

    if page == 'Login' :
        with st.form(key="Login") :

            userName = st.text_input("Username")
            passw = st.text_input("Password", type="password")
            submissionButton = st.form_submit_button(label="Login")
            if submissionButton == True:
                match = 'SELECT Orole FROM Organization WHERE email='" + userName + "' AND password= '"+ passw+"''
                

                if match!=None:
                    type(match)
                            
                else:
                    st.error("either username or password is incorrect")

def addData():
    
    conn = odbc.connect(cnxn)
    cursor = conn.cursor()
    insert_statement = """
        INSERT INTO Organization
        VALUES (?, ?, ?, ?)
    """
    
    for record in records:
        print(record)
        cursor.execute(insert_statement, record)
    
    print("Successfully inserted")
    cursor.commit()
    cursor.close()

    



