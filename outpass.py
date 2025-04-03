import streamlit as st
import sqlite3
from datetime import datetime

def apply_outpass():
    st.subheader("Apply for Outpass")
    student_id = st.text_input("Enter your Student ID")
    reason = st.text_area("Reason for Outpass")
    date = st.date_input("Select Date")
    
    if st.button("Submit Request"):
        today = datetime.today().date()
        if date < today:
            st.error("Invalid Date! Outpass date must be in the future.")
            return
        
        conn = sqlite3.connect("hostel.db")
        c = conn.cursor()
        c.execute("INSERT INTO outpass (student_id, reason, date, status) VALUES (?, ?, ?, ?)", 
                  (student_id, reason, date, "Pending"))
        conn.commit()
        conn.close()
        st.success("Outpass request submitted successfully! Await approval.")
