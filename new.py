import streamlit as st
import json
import time
from datetime import datetime
import os
import google.generativeai as genai
from PIL import Image

# Configure the Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

# Initialize session states
if 'users' not in st.session_state:
    st.session_state.users = [{
        "email": "demo@example.com",
        "password": "demo123",
        "first_name": "Demo",
        "last_name": "User",
        "phone": "1234567890",
        "aadhar": "1234-5678-9012",
        "state": "Maharashtra"
    }]
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'verified_documents' not in st.session_state:
    st.session_state.verified_documents = []
if 'chat' not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])
if 'messages' not in st.session_state:
    st.session_state.messages = [{
        "role": "assistant",
        "content": "Hello! I'm your SuvidhaAI assistant. How may I help you today?"
    }]
if 'theme' not in st.session_state:
    st.session_state.theme = 'light'

class DocumentVerifier:
    @staticmethod
    def verify_document(doc_type, doc_number, state=None):
        """Generic document verification method"""
        try:
            # Simulate verification process
            time.sleep(1)
            return {"valid": True, "message": f"{doc_type} verification successful"}
        except Exception as e:
            return {"valid": False, "message": f"Verification failed: {str(e)}"}

def get_scheme_response(question, verified_documents):
    try:
        docs_info = "Verified documents:\n" + "\n".join([f"- {doc}" for doc in verified_documents])
        response = st.session_state.chat.send_message(
            f"""As a government welfare expert, provide specific scheme recommendations based on:
            Verified Documents: {docs_info}
            User Question: {question}
            Focus on eligibility criteria and required documents."""
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

def load_css():
    return """
    <style>
    [data-theme="light"] {
        --primary-color: #2E7D32;
        --secondary-color: #FF4081;
        --background-color: #ffffff;
        --text-color: #333333;
        --card-bg: #f8f9fa;
        --chat-user-bg: #e3f2fd;
        --chat-assistant-bg: #f5f5f5;
    }
    
    [data-theme="dark"] {
        --primary-color: #4CAF50;
        --secondary-color: #FF80AB;
        --background-color: #1a1a1a;
        --text-color: #ffffff;
        --card-bg: #2d2d2d;
        --chat-user-bg: #2c3e50;
        --chat-assistant-bg: #34495e;
    }

    .stApp {
        background-color: var(--background-color);
        color: var(--text-color);
    }

    .main-header {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        animation: fadeIn 0.5s ease-in;
    }

    .card {
        background-color: var(--card-bg);
        padding: 1.5rem;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
    }

    .stChatMessage {
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        animation: slideIn 0.3s ease;
    }

    .stChatMessage[data-testid="chat-message-user"] {
        background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
        color: white;
        margin-left: 20%;
    }

    .stChatMessage[data-testid="chat-message-assistant"] {
        background-color: var(--chat-assistant-bg);
        margin-right: 20%;
    }

    @keyframes slideIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .stButton>button {
        background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
        color: white;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        border: none;
        transition: all 0.3s ease;
    }
    </style>
    """

def show_auth_page():
    st.markdown('<div class="main-header"><h1>🏛️ Welcome to SuvidhaAI</h1></div>', 
                unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["Login", "Register"])
    
    with tab1:
        with st.form("login_form"):
            email = st.text_input("Email")
            password = st.text_input("Password", type="password")
            if st.form_submit_button("Login"):
                user = next((u for u in st.session_state.users 
                           if u['email'] == email and u['password'] == password), None)
                if user:
                    st.session_state.current_user = user
                    st.success("Login successful!")
                    st.rerun()
                else:
                    st.error("Invalid credentials")

    with tab2:
        with st.form("registration_form"):
            col1, col2 = st.columns(2)
            with col1:
                first_name = st.text_input("First Name")
                email = st.text_input("Email", key="reg_email")
                phone = st.text_input("Phone")
            with col2:
                last_name = st.text_input("Last Name")
                password = st.text_input("Password", type="password", key="reg_password")
                state = st.selectbox("State", ["Maharashtra", "Delhi", "Karnataka"])
            
            if st.form_submit_button("Register"):
                if all([first_name, last_name, email, password, phone, state]):
                    user_data = {
                        "first_name": first_name,
                        "last_name": last_name,
                        "email": email,
                        "password": password,
                        "phone": phone,
                        "state": state
                    }
                    st.session_state.users.append(user_data)
                    st.success("Registration successful! Please login.")
                else:
                    st.error("Please fill all required fields")

def show_document_verification():
    st.markdown('<div class="main-header"><h2>📄 Document Verification</h2></div>', 
                unsafe_allow_html=True)
    
    verifier = DocumentVerifier()
    doc_type = st.selectbox("Select Document Type", [
        "Aadhaar Card",
        "PAN Card",
        "Income Certificate",
        "Caste Certificate",
        "Disability Certificate"
    ])
    
    col1, col2 = st.columns(2)
    with col1:
        doc_number = st.text_input(f"Enter {doc_type} Number")
        state = st.selectbox("State", ["Maharashtra", "Delhi", "Karnataka"]) if doc_type in [
            "Income Certificate", "Caste Certificate"
        ] else None
    
    with col2:
        doc_file = st.file_uploader(f"Upload {doc_type}", type=["pdf", "jpg", "png"])
    
    if st.button("Verify Document"):
        if doc_number and doc_file:
            with st.spinner("Verifying document..."):
                result = verifier.verify_document(doc_type, doc_number, state)
                if result["valid"]:
                    if doc_type not in st.session_state.verified_documents:
                        st.session_state.verified_documents.append(doc_type)
                    st.success(result["message"])
                else:
                    st.error(result["message"])
        else:
            st.warning("Please provide all required information")

def show_chatbot():
    st.markdown('<div class="main-header"><h2>💬 AI Scheme Assistant</h2></div>', 
                unsafe_allow_html=True)

    # Display verified documents
    if st.session_state.verified_documents:
        st.sidebar.subheader("Verified Documents")
        for doc in st.session_state.verified_documents:
            st.sidebar.success(f"✅ {doc}")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask about government schemes..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            with st.spinner("Finding relevant schemes..."):
                response = get_scheme_response(prompt, st.session_state.verified_documents)
                message = {"role": "assistant", "content": response}
                st.session_state.messages.append(message)
                st.write(response)

def show_dashboard():
    st.markdown(f"""
        <div class="main-header">
            <h1>Welcome, {st.session_state.current_user['first_name']}! 👋</h1>
        </div>
    """, unsafe_allow_html=True)

    menu = ["Documents", "Scheme Assistant", "Logout"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Documents":
        show_document_verification()
    elif choice == "Scheme Assistant":
        show_chatbot()
    elif choice == "Logout":
        st.session_state.current_user = None
        st.rerun()

def main():
    st.set_page_config(page_title="SuvidhaAI", layout="wide")
    st.markdown(load_css(), unsafe_allow_html=True)

    with st.sidebar:
        st.title("SuvidhaAI")
        if st.button("🌓 Toggle Theme"):
            st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
            st.rerun()

    if not st.session_state.current_user:
        show_auth_page()
    else:
        show_dashboard()

if __name__ == "__main__":
    main()