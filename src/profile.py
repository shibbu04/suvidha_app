import streamlit as st
import time
from datetime import datetime
from src.database import update_user
from src.config import STATES, CATEGORIES, OCCUPATIONS

class ProfileValidator:
    @staticmethod
    def validate_phone(phone):
        """Validate phone number"""
        return len(phone) == 10 and phone.isdigit()

    @staticmethod
    def validate_aadhar(aadhar):
        """Validate Aadhar number"""
        cleaned_aadhar = aadhar.replace("-", "").replace(" ", "")
        return len(cleaned_aadhar) == 12 and cleaned_aadhar.isdigit()

    @staticmethod
    def validate_pin_code(pin_code):
        """Validate PIN code"""
        return len(pin_code) == 6 and pin_code.isdigit()

    @staticmethod
    def validate_email(email):
        """Basic email validation"""
        return "@" in email and "." in email.split("@")[1]

class ProfileManager:
    def __init__(self, user_data):
        self.user_data = user_data
        self.validator = ProfileValidator()

    def update_profile(self, updated_data):
        """Update profile with validation"""
        validation_errors = []

        # Validate phone
        if not self.validator.validate_phone(updated_data.get('phone', '')):
            validation_errors.append("Invalid phone number. Please enter 10 digits.")

        # Validate Aadhar
        if not self.validator.validate_aadhar(updated_data.get('aadhar', '')):
            validation_errors.append("Invalid Aadhar number. Please enter 12 digits.")

        # Validate PIN code
        if updated_data.get('pin_code') and not self.validator.validate_pin_code(updated_data.get('pin_code')):
            validation_errors.append("Invalid PIN code. Please enter 6 digits.")

        if validation_errors:
            return False, validation_errors

        return True, None

def show_profile():
    st.markdown('<div class="main-header"><h2>👤 My Profile</h2></div>', 
                unsafe_allow_html=True)
    
    user = st.session_state.current_user
    profile_manager = ProfileManager(user)
    
    # Create tabs for different sections
    tabs = st.tabs(["Personal Information", "Contact Details", "Documents & Verification", "Preferences"])
    
    with tabs[0]:  # Personal Information
        show_personal_info(user, profile_manager)
    
    with tabs[1]:  # Contact Details
        show_contact_details(user, profile_manager)
    
    with tabs[2]:  # Documents & Verification
        show_documents_verification(user)
    
    with tabs[3]:  # Preferences
        show_preferences(user)

def show_personal_info(user, profile_manager):
    st.subheader("Personal Information")
    
    with st.form("personal_info_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("First Name", value=user.get('first_name', ''))
            last_name = st.text_input("Last Name", value=user.get('last_name', ''))
            dob = st.date_input("Date of Birth", 
                              value=datetime.strptime(user.get('dob', '2000-01-01'), '%Y-%m-%d').date() 
                              if user.get('dob') else datetime.now().date())
            gender = st.selectbox("Gender", 
                                ["Male", "Female", "Other", "Prefer not to say"],
                                index=["Male", "Female", "Other", "Prefer not to say"].index(
                                    user.get('gender', 'Prefer not to say')))
        
        with col2:
            category = st.selectbox("Category", CATEGORIES,
                                  index=CATEGORIES.index(user.get('category', 'General')))
            occupation = st.selectbox("Occupation", OCCUPATIONS,
                                    index=OCCUPATIONS.index(user.get('occupation', 'Other')))
            annual_income = st.number_input("Annual Income (in ₹)", 
                                         value=float(user.get('annual_income', 0)),
                                         min_value=0.0)
            
        submit = st.form_submit_button("Update Personal Information")
        
        if submit:
            with st.spinner("Updating personal information..."):
                updated_data = {
                    'first_name': first_name,
                    'last_name': last_name,
                    'dob': str(dob),
                    'gender': gender,
                    'category': category,
                    'occupation': occupation,
                    'annual_income': annual_income
                }
                
                if update_user(user['email'], updated_data):
                    st.success("Personal information updated successfully!")
                else:
                    st.error("Failed to update personal information")

def show_contact_details(user, profile_manager):
    st.subheader("Contact Details")
    
    with st.form("contact_details_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            email = st.text_input("Email", value=user.get('email', ''), disabled=True)
            phone = st.text_input("Phone Number", value=user.get('phone', ''))
            alternate_phone = st.text_input("Alternate Phone Number", 
                                          value=user.get('alternate_phone', ''))
        
        with col2:
            address = st.text_area("Address", value=user.get('address', ''))
            state = st.selectbox("State", STATES,
                               index=STATES.index(user.get('state', 'Maharashtra')))
            city = st.text_input("City", value=user.get('city', ''))
            pin_code = st.text_input("PIN Code", value=user.get('pin_code', ''))
        
        submit = st.form_submit_button("Update Contact Details")
        
        if submit:
            with st.spinner("Updating contact details..."):
                updated_data = {
                    'phone': phone,
                    'alternate_phone': alternate_phone,
                    'address': address,
                    'state': state,
                    'city': city,
                    'pin_code': pin_code
                }
                
                success, errors = profile_manager.update_profile(updated_data)
                if success:
                    if update_user(user['email'], updated_data):
                        st.success("Contact details updated successfully!")
                    else:
                        st.error("Failed to update contact details")
                else:
                    for error in errors:
                        st.error(error)

def show_documents_verification(user):
    st.subheader("Documents & Verification")
    
    # Display verification status
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
            <div class="card">
                <h4>📱 Phone Verification</h4>
                <p style="color: green">✓ Verified</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="card">
                <h4>📧 Email Verification</h4>
                <p style="color: green">✓ Verified</p>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="card">
                <h4>🆔 Aadhar Verification</h4>
                <p style="color: green">✓ Verified</p>
            </div>
        """, unsafe_allow_html=True)
    
    # KYC Status
    st.subheader("KYC Status")
    kyc_status = user.get('kyc_status', 'Pending')
    st.progress(75 if kyc_status == 'Pending' else 100)
    st.write(f"KYC Status: {kyc_status}")
    
    if kyc_status == 'Pending':
        st.info("Your KYC is under review. This usually takes 24-48 hours.")
        if st.button("Check KYC Status"):
            with st.spinner("Checking KYC status..."):
                time.sleep(1)
                st.write("KYC is still under review.")

def show_preferences(user):
    st.subheader("Preferences")
    
    # Language Preferences
    st.subheader("Language Preferences")
    primary_language = st.selectbox(
        "Primary Language",
        ["English", "Hindi", "Marathi", "Kannada"],
        index=["English", "Hindi", "Marathi", "Kannada"].index(
            user.get('primary_language', 'English'))
    )
    
    # Notification Preferences
    st.subheader("Notification Preferences")
    col1, col2 = st.columns(2)
    
    with col1:
        email_notifications = st.checkbox("Email Notifications", 
                                       value=user.get('email_notifications', True))
        scheme_alerts = st.checkbox("New Scheme Alerts", 
                                  value=user.get('scheme_alerts', True))
    
    with col2:
        sms_notifications = st.checkbox("SMS Notifications", 
                                      value=user.get('sms_notifications', True))
        status_updates = st.checkbox("Application Status Updates", 
                                   value=user.get('status_updates', True))
    
    # Save preferences
    if st.button("Save Preferences"):
        with st.spinner("Saving preferences..."):
            updated_data = {
                'primary_language': primary_language,
                'email_notifications': email_notifications,
                'sms_notifications': sms_notifications,
                'scheme_alerts': scheme_alerts,
                'status_updates': status_updates
            }
            
            if update_user(user['email'], updated_data):
                st.success("Preferences saved successfully!")
            else:
                st.error("Failed to save preferences")
                