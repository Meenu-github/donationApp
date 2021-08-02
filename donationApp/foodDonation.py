import streamlit as st
from PIL import Image
import base64
import sys
import pyodbc as odbc
records = []
DRIVER = "ODBC Driver 13 for SQL Server"
SERVER_NAME = "MEENU\SQLEXPRESS"
DATABASE_NAME="StreamLit"
cnxn = f"""
    Driver={{{DRIVER}}};
    Server={SERVER_NAME};
    Database={DATABASE_NAME};
    Trusted_Connection=yes;
"""

def foodDonate() :
    st.title("Food Donation")
    main_bg = "food.gif"
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
    st.markdown("FOOD DONATION")
    img = Image.open("FoodDonation.jpg")
    st.image(img, caption='Food Donation',width=500)
    st.title("Welcome to the food donation page, your donated food can bring hope in someones life of survival.\nCome let us donate food for needy one.\nYou don't have to walk and donate it you just have to register yourself and we will pick the food from your house address that will be provided.")
    st.write("Here if you are willing to donate food\n you have to register yourself.")
    with st.form(key="Register for food donation"):
        namefood = st.text_input("Enter your name : ")
        foodaddress = st.text_input("Enter your address please : ")
        food_phone = st.text_input("Enter your phone  Number : ")
        
        foodsubmission = st.form_submit_button(label="Submit")
        if foodsubmission==True:
            
            records.append([namefood,foodaddress,food_phone])
            addData()
            st.success("Successfully registered for food donation")
        else:
            st.info("Please submit the form.")

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
        INSERT INTO Food_Donation
        VALUES (?, ?, ?)
    """
    try:
        for record in records:
            print(record)
            cursor.execute(insert_statement, record)
    except Exception as e:
        cursor.rollback()
        print(e.value)

    else:
        print("Successfully inserted")
        cursor.commit()
        cursor.close()

    




        

