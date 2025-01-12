import streamlit as st
from dotenv import load_dotenv
from src.auth import show_auth_page
from src.dashboard import show_dashboard
from src.styles import load_css
from src.database import initialize_session_state

def initialize_app_state():
    """Initialize all app-related session state variables"""
    if 'theme' not in st.session_state:
        st.session_state.theme = 'light'
    if 'current_user' not in st.session_state:
        st.session_state.current_user = None

def main():
    load_dotenv()  # Load environment variables
    
    # Initialize all session states
    initialize_app_state()
    initialize_session_state()
    
    st.set_page_config(
        page_title="SuvidhaAI",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    st.markdown(load_css(), unsafe_allow_html=True)

    # Theme toggle and sidebar
    with st.sidebar:
        st.image("./assets/image.png", width=100)
        st.title("SuvidhaAI")
        
        if st.button("🌓 Toggle Theme", key="theme_toggle"):
            st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
            st.rerun()
        
        # Use an f-string for the theme attribute
        st.markdown(f"""
            <script>
                document.documentElement.setAttribute('data-theme', '{st.session_state.theme}');
            </script>
            """, unsafe_allow_html=True)

    if not st.session_state.current_user:
        show_auth_page()
    else:
        show_dashboard()

if __name__ == "__main__":
    main()