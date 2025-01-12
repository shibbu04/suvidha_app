import streamlit as st
import os
import google.generativeai as genai

# Configure the Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def initialize_chat():
    """Initialize chat if not already in session state"""
    if 'chat' not in st.session_state:
        model = genai.GenerativeModel('gemini-pro')
        st.session_state.chat = model.start_chat(history=[])
    if 'messages' not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant",
            "content": "Hello! I'm your SuvidhaAI assistant. How may I help you today?"
        }]

def get_scheme_response(question, verified_documents):
    """Get AI response for scheme-related questions"""
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

def show_chatbot():
    initialize_chat()
    
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