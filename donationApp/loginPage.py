import streamlit as st
import base64
import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
cur = conn.cursor()

def type(selectRole):
    
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
        conn = sqlite3.connect('data.db',check_same_thread=False)
        cur = conn.cursor()
        tabl = 'SELECT * From blood'
        cur.execute(tabl)
        output = cur.fetchall()
        st.table(output)
        
        cur.close()
    
    if selectRole == 'Food Distributor':
        st.success("Data of food donor")
        conn = sqlite3.connect('data.db',check_same_thread=False)
        cur = conn.cursor()
        tab2 = 'SELECT * From food'
        cur.execute(tab2)
        output = cur.fetchall()
        st.table(output)
        
        cur.close()
        

    if selectRole == 'Orphanage':
        st.success("Data of book donor")
        conn = sqlite3.connect('data.db',check_same_thread=False)
        cursor = conn.cursor()
        tab3 = 'SELECT * From book'
        cursor.execute(tab3)
        output = cursor.fetchall()
        st.table(output)
        
        cursor.close()
             
def loginPages():
    
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
                addData(userName,email,passw,selectRole)
                
                st.info('Giving data of donor')

                type(selectRole)
                
                

    if page == 'Login' :
        with st.form(key="Login") :

            userName = st.text_input("Username")
            passw = st.text_input("Password", type="password")
            submissionButton = st.form_submit_button(label="Login")
            if submissionButton == True:
                 
                retrieved_data = cur.execute("SELECT * FROM organization ")
                for i in retrieved_data:
                    if i[1]==userName and i[2]==passw:
                        retrieved_role = i[3]
                        break

                
                if retrieved_role!=None:
                    type(retrieved_role)
                            
                else:
                    st.error("either username or password is incorrect")
        

def addData(a,b,c,d):
    cur.execute("""CREATE TABLE IF NOT EXISTS organization(NAME TEXT(50),
                    EMAIL TEXT(30), PASSW  TEXT(20), ROL_E TEXT(25)); """) 
    cur.execute("INSERT INTO organization VALUES (?,?,?,?)",(a,b,c,d))
    conn.commit()
    conn.close()
    st.success("Successfully registered")
    
    

    



