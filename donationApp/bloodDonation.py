import streamlit as st
#import tkinter as tk
#from tkcalendar import Calendar
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
            #root = tk.Tk()
            #root.geometry("400x400")
            #cal = Calendar(root, selectmode = 'day',
            #            year = 2021, month = 7,
             #           day = 31)
           # cal.pack(pady = 20)
            
            #def grad_date():
             #   date.config(text = "Selected Date is: " + cal.get_date())
        #    tk.Button(root, text = "Set Date",
         #       command = grad_date).pack(pady = 20)
          #  date = tk.Label(root, text = "")
           # date.pack(pady = 20)
            #root.mainloop()

            ws.append([bloodname,bgrp,age,bloodidProof])
            wb.save('BloodDonation.xlsx')
            
            st.success("Successfully submitted your data.")
    st.info("Select a date to donate blood in your nearby blood donation center : ")
    
    



    #adding date picker..

