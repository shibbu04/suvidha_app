import streamlit as st

def initialize_session_state():
    """Initialize all session state variables"""
    if 'users' not in st.session_state:
        st.session_state.users = [
            {
                "email": "demo@example.com",
                "password": "demo123",
                "first_name": "Demo",
                "last_name": "User",
                "phone": "1234567890",
                "aadhar": "1234-5678-9012",
                "state": "Maharashtra"
            }
        ]
    
    if 'documents' not in st.session_state:
        st.session_state.documents = [
            {
                "user_email": "demo@example.com",
                "type": "Aadhar Card",
                "filename": "aadhar.pdf",
                "upload_date": "2024-01-09",
                "status": "Verified"
            }
        ]
    
    if 'verified_documents' not in st.session_state:
        st.session_state.verified_documents = []

def save_user(user_data):
    """Save user data to session state"""
    st.session_state.users.append(user_data)

def get_user(email, password):
    """Get user by email and password"""
    return next((user for user in st.session_state.users 
                 if user['email'] == email and user['password'] == password), None)

def save_document(document_data):
    """Save document data to session state"""
    st.session_state.documents.append(document_data)

def get_user_documents(user_email):
    """Get documents for a specific user"""
    return [doc for doc in st.session_state.documents if doc['user_email'] == user_email]

def update_user(email, updated_data):
    """Update user data in session state"""
    for user in st.session_state.users:
        if user['email'] == email:
            user.update(updated_data)
            if st.session_state.current_user['email'] == email:
                st.session_state.current_user.update(updated_data)
            return True
    return False