import streamlit as st
from database import init_db
from register import register_student
from outpass import apply_outpass
from chatbot import chatbot

def main():
    st.title("Hostel Management System")
    menu = ["Home", "Register", "Apply Outpass", "Chatbot"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        st.subheader("Welcome to the Hostel Management System!")
    elif choice == "Register":
        register_student()
    elif choice == "Apply Outpass":
        apply_outpass()
    elif choice == "Chatbot":
        chatbot()

if __name__ == "__main__":
    init_db()
    main()
