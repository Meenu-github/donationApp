import streamlit as st
import calendar
from tkinter import *
from tkcalendar import Calendar
yy = 2021
mm = 12
from openpyxl import Workbook,worksheet,load_workbook
wb = Workbook()
ws = wb.active
ws.title = "blooddonation"

def bloodDonate() :
    st.title("Blood Donation")
    st.write("This is the blood donation page.")
    st.write("Here if you are willing to donate blood\n you have to register yourself.")
    
    with st.form(key="Registration for Blood Donation"):
        bloodname = st.text_input("Enter your name : ")
        bgrp = st.text_input("Enter your blood group : ")
        age = st.slider(label="Enter your age ", min_value=18, max_value=45)
        bloodidProof =  st.text_input("Enter your Id Proof Number : ")
        
        submissionblood = st.form_submit_button(label="Submit")
        if submissionblood==True:
            root = Tk()
            root.geometry("400x400")
            cal = Calendar(root, selectmode = 'day',
                        year = 2021, month = 7,
                        day = 31)
            cal.pack(pady = 20)
            
            def grad_date():
                date.config(text = "Selected Date is: " + cal.get_date())
            Button(root, text = "Get Date",
                command = grad_date).pack(pady = 20)
            date = Label(root, text = "")
            date.pack(pady = 20)
            root.mainloop()

            ws.append([bloodname,bgrp,age,bloodidProof,cal.get_date()])
            wb.save('BloodDonation.xlsx')
            
            st.success("Successfully submitted your data.")
    st.info("Select a date to donate blood in your nearby blood donation center : ")
    
    st.write(calendar.month(yy, mm))



    #adding date picker..

