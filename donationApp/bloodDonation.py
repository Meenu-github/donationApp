import streamlit as st
from PIL import Image
import base64
import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
cur = conn.cursor()


def bloodDonate() :
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
    st.markdown("<h1 style='text-align: left; color: aquamarine;'>Blood Donation</h1>", unsafe_allow_html=True)
    
    
    img = Image.open("_bloodDonation.jpg")
    st.image(img, caption='Blood Donation', width=500)
    st.write("This is the blood donation page.")
    st.write("Here if you are willing to donate blood\n you have to register yourself.")
    
    with st.form(key="Registration for Blood Donation"):
        bloodname = st.text_input("Enter your name : ")
        bgrp = st.text_input("Enter your blood group : ")
        age = st.slider(label="Enter your age ", min_value=18, max_value=45)
        blood_phone =  st.text_input("Enter your Phone number : ")
        date = st.date_input(label="Date")
        
        submissionblood = st.form_submit_button(label="Submit")
        if submissionblood==True:
            addData(bloodname,bgrp,age,blood_phone,date)

            

def addData(a,b,c,d,e):
    conn = sqlite3.connect('data.db',check_same_thread=False)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS blood(NAME TEXT(50),BLOOD_GROUP TEXT(5), AGE TEXT(3), PHONE_NO  TEXT(15), DAT_E TEXT(10)); """) 
    cur.execute("INSERT INTO blood VALUES (?,?,?,?,?)",(a,b,c,d,e))
    conn.commit()
    
    st.success("Successfully inserted")

    


    

