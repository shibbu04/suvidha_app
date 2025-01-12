def load_css():
    return """
    <style>
     :root[data-theme="light"] {
        --primary-color: #2E7D32;
        --secondary-color: #FF4081;
        --background-color: #ffffff;
        --text-color: #333333;
        --card-bg: #f8f9fa;
        --sidebar-bg: #f0f2f6;
    }
    
    :root[data-theme="dark"] {
        --primary-color: #4CAF50;
        --secondary-color: #FF80AB;
        --background-color: #1a1a1a;
        --text-color: #ffffff;
        --card-bg: #2d2d2d;
        --sidebar-bg: #2d2d2d;
    }

    /* Rest of the CSS remains the same */
    .stApp {
        transition: all 0.3s ease;
        background-color: var(--background-color) !important;
        color: var(--text-color) !important;
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

    .card:hover {
        transform: translateY(-5px);
    }

    .css-1d391kg {
        background-color: var(--sidebar-bg);
        padding: 2rem 1rem;
    }

    .stButton>button {
        background: linear-gradient(45deg, var(--primary-color), var(--secondary-color));
        color: white;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        border: none;
        transition: all 0.3s ease;
        text-transform: uppercase;
        font-weight: bold;
        letter-spacing: 1px;
    }

    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .progress-container {
        width: 100%;
        background-color: rgba(0,0,0,0.1);
        border-radius: 10px;
        margin: 1rem 0;
        overflow: hidden;
    }

    .progress-bar {
        height: 20px;
        background: linear-gradient(90deg, var(--primary-color), var(--secondary-color));
        border-radius: 10px;
        transition: width 1s ease-in-out;
        animation: shimmer 2s infinite linear;
    }
    </style>
    
    <script>
        // Initialize theme on page load
        document.documentElement.setAttribute('data-theme', 
            window.sessionStorage.getItem('theme') || 'light');
    </script>
    """
    