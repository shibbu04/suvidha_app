import streamlit as st
from src.chatbot import show_chatbot
from src.documents import show_documents
from src.profile import show_profile

def show_dashboard():
    st.markdown(f"""
        <div class="main-header">
            <h1>Welcome, {st.session_state.current_user['first_name']}! 👋</h1>
            <p>Manage your government scheme applications</p>
        </div>
    """, unsafe_allow_html=True)

    menu = ["Dashboard", "Scheme Assistant", "Documents", "Profile", "Logout"]
    choice = st.sidebar.selectbox("Navigation", menu)

    if choice == "Dashboard":
        show_dashboard_content()
    elif choice == "Scheme Assistant":
        show_chatbot()
    elif choice == "Documents":
        show_documents()
    elif choice == "Profile":
        show_profile()
    elif choice == "Logout":
        st.session_state.current_user = None
        st.rerun()

def show_dashboard_content():
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
            <div class="card">
                <h3>15</h3>
                <p>Eligible Schemes</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="card">
                <h3>3</h3>
                <p>Applications</p>
            </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
            <div class="card">
                <h3>2</h3>
                <p>Approved</p>
            </div>
        """, unsafe_allow_html=True)
    with col4:
        st.markdown("""
            <div class="card">
                <h3>1</h3>
                <p>Pending</p>
            </div>
        """, unsafe_allow_html=True)

    st.subheader("Application Progress")
    progress = 75
    st.markdown(f"""
        <div class="progress-container">
            <div class="progress-bar" style="width: {progress}%"></div>
        </div>
        <p>Overall completion: {progress}%</p>
    """, unsafe_allow_html=True)