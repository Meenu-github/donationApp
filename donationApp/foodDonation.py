import streamlit as st
from PIL import Image
import base64
import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
cur = conn.cursor()
def foodDonate() :
    main_bg = "bg.jpg"
    main_bg_ext = "jpg"
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
    
    
    st.markdown("<h1 style='text-align: left; color: peachpuff;'>Food Donation</h1>", unsafe_allow_html=True)
    
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
            addData(namefood,foodaddress,food_phone)
            
        else:
            st.info("Please submit the form.")

def addData(a,b,c):
    conn = sqlite3.connect('data.db',check_same_thread=False)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS food(NAME TEXT(50), ADDRESS TEXT(50), PHONE_NO  TEXT(15)); """) 
    cur.execute("INSERT INTO food VALUES (?,?,?)",(a,b,c))
    conn.commit()
    
    st.success("Successfully inserted")
    
    




        

