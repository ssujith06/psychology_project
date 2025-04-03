import streamlit as st
from database import register_student, apply_outpass, student_exists
from chatbot import get_response

st.title("🏠 Hostel Management System")

menu = ["Home", "Student Register", "Apply for Outpass", "Chatbot"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Welcome to the Hostel Management System")
    st.write("Use the sidebar to navigate.")

elif choice == "Student Register":
    st.subheader("📌 Student Registration")
    name = st.text_input("Full Name")
    roll_no = st.text_input("Roll Number")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if student_exists(roll_no):
            st.error("Student already registered!")
        else:
            msg = register_student(name, roll_no, email, password)
            st.success(msg)

elif choice == "Apply for Outpass":
    st.subheader("📜 Outpass Application")
    roll_no = st.text_input("Enter Roll Number")
    reason = st.text_area("Reason for Outpass")
    out_date = st.date_input("Outpass Date")
    return_date = st.date_input("Return Date")

    if st.button("Apply"):
        if student_exists(roll_no):
            msg = apply_outpass(roll_no, reason, out_date, return_date)
            st.success(msg)
        else:
            st.error("Student not registered!")

elif choice == "Chatbot":
    st.subheader("🤖 Hostel Chatbot (Humorous)")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask me anything!"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        response = get_response(prompt)
        st.session_state.messages.append({"role": "assistant", "content": response})
