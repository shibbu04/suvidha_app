import streamlit as st
import time
from datetime import datetime
from src.database import save_user, get_user

def show_auth_page():
    st.markdown('<div class="main-header"><h1>🏛️ Welcome to SuvidhaAI</h1>'
                '<p>Your Gateway to Government Schemes</p></div>', 
                unsafe_allow_html=True)

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        show_login()
    with tab2:
        show_registration()

def show_login():
    with st.form("login_form"):
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        submit_button = st.form_submit_button("Login")

        if submit_button:
            with st.spinner("Logging in..."):
                time.sleep(1)
                user = get_user(email, password)
                if user:
                    st.session_state.current_user = user
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid credentials")

def show_registration():
    with st.form("registration_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            first_name = st.text_input("First Name")
            email = st.text_input("Email")
            phone = st.text_input("Phone Number")
            dob = st.date_input("Date of Birth")
            income = st.number_input("Annual Income", min_value=0)

        with col2:
            last_name = st.text_input("Last Name")
            password = st.text_input("Password", type="password")
            aadhar = st.text_input("Aadhar Number")
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
            occupation = st.selectbox("Occupation", 
                ["Farmer", "Student", "Self-employed", "Employed", "Other"])

        with col3:
            address = st.text_area("Address")
            state = st.selectbox("State", ["Maharashtra", "Delhi", "Karnataka"])
            city = st.text_input("City")
            pin_code = st.text_input("PIN Code")
            category = st.selectbox("Category", 
                ["General", "OBC", "SC", "ST"])

        submit_button = st.form_submit_button("Register")
        
        if submit_button:
            if not all([first_name, last_name, email, password, phone, aadhar, state]):
                st.error("Please fill in all required fields.")
            else:
                with st.spinner("Processing registration..."):
                    time.sleep(1.5)
                    user_data = {
                        "first_name": first_name,
                        "last_name": last_name,
                        "email": email,
                        "password": password,
                        "phone": phone,
                        "aadhar": aadhar,
                        "dob": str(dob),
                        "gender": gender,
                        "occupation": occupation,
                        "address": address,
                        "state": state,
                        "city": city,
                        "pin_code": pin_code,
                        "category": category,
                        "income": income
                    }
                    save_user(user_data)
                    st.success("Registration successful! Please login.")