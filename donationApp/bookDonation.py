import streamlit as st
from PIL import Image
import sys
import pyodbc as odbc
import base64

records = []
DRIVER = "SQL Server"
SERVER_NAME = "MEENU\SQLEXPRESS"
DATABASE_NAME="StreamLit"
cnxn = f"""
    Driver={{{DRIVER}}};
    Server={SERVER_NAME};
    Database={DATABASE_NAME};
    Trusted_Connection=yes;
"""


def bookdonate():
    
    st.title("Book Donation")
    main_bg = "book1.gif"
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
    st.markdown("BOOK DONATION")
    img = Image.open("BookDonation.jpg")
    st.image(img, caption='Book Donation',width=700)
    st.title(" Welcome to the book donation page, your old book can bring light in someones future.\nCome let us donate books for needy one.\nYou don't have to walk and donate it you just have to register yourself and we will pick the book from your house address that will be provided.")
    st.markdown("## Here if you are willing to donate book\n you have to register yourself.")
    
    with st.form(key="Registration for Blood Donation"):
    

        bookname = st.text_input("Enter your name : ")
        address = st.text_input("Enter your address please : ")
        book_phone = st.text_input("Enter your phone Number : ")
        
        submissionbook = st.form_submit_button(label="Submit")
        if submissionbook==True:
            records.append([bookname,address,book_phone])
            
            addData()
            
            st.success("Successfully submitted the form.")
        else:
            st.info("Please submit the form.")
def addData():
    try:
        conn = odbc.connect(cnxn)
    except Exception as e:
        st.error(e)
        st.error("task is terminated")
        #sys.exit()
    else:
        cursor = conn.cursor()
    insert_statement = """
        INSERT INTO Book_Donation
        VALUES (?, ?, ?)
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

    