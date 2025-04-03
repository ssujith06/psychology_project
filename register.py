import streamlit as st
import sqlite3

def register_student():
    st.subheader("Student Registration")
    name = st.text_input("Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    
    if st.button("Register"):
        conn = sqlite3.connect("hostel.db")
        c = conn.cursor()
        c.execute("INSERT INTO students (name, email, password) VALUES (?, ?, ?)", 
                  (name, email, password))
        conn.commit()
        conn.close()
        st.success("Registration successful! You can now apply for an outpass.")
