import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Application configuration
APP_CONFIG = {
    "title": "SuvidhaAI",
    "description": "Your Gateway to Government Schemes",
    "version": "1.0.0",
    "theme": {
        "primary_color": "#2E7D32",
        "secondary_color": "#FF4081",
    }
}

# API configuration
API_CONFIG = {
    "google_api_key": os.getenv("GOOGLE_API_KEY"),
    "model_name": "gemini-pro"
}

# Document settings
DOCUMENT_CONFIG = {
    "allowed_types": ['pdf', 'jpg', 'png'],
    "max_size_mb": 5,
    "supported_docs": [
        "Aadhar Card",
        "PAN Card",
        "Income Certificate",
        "Address Proof"
    ]
}

# State list
STATES = [
    "Maharashtra",
    "Delhi",
    "Karnataka"
]

# Categories
CATEGORIES = [
    "General",
    "OBC",
    "SC",
    "ST"
]

# Occupations
OCCUPATIONS = [
    "Farmer",
    "Student",
    "Self-employed",
    "Employed",
    "Other"
]