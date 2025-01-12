# 📱 Suvidha App

Welcome to **Suvidha App**! 🚀

Suvidha App is a Streamlit-based application designed for seamless and efficient user interaction with features like authentication, profile management, document handling, and an integrated chatbot. Built with simplicity, style, and scalability in mind. 🌟

---

## ✨ Features

- **Authentication Module**: Secure user login and session management.
- **Dashboard**: Overview of user activities and quick access to features.
- **Document Management**: Easy upload, view, and organization of files.
- **Chatbot Integration**: Instant assistance with an AI-powered chatbot.
- **Profile Management**: User-friendly profile customization.
- **Configurable Settings**: Simplified configuration using `.env`.

---

## 📂 Project Structure

```
📁 suvidha_app/
├── 📁 assets/
│   └── image.png             # Static images and assets
├── 📁 src/
│   ├── 📄 auth.py             # Authentication logic
│   ├── 📄 dashboard.py        # Dashboard implementation
│   ├── 📄 documents.py        # Document handling logic
│   ├── 📄 chatbot.py          # Chatbot integration
│   ├── 📄 profile.py          # Profile management
│   ├── 📄 database.py         # Database interaction
│   ├── 📄 styles.py           # Custom styles and themes
│   └── 📄 config.py           # Configuration settings
├── 📄 app.py                  # Main application entry point
├── 📄 requirements.txt        # Python dependencies
└── 📄 .env                    # Environment variables
```

---

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository

```bash
# Clone the repository
https://github.com/shibbu04/suvidha_app.git
cd suvidha_app
```

OR

### 2️⃣ Create a New Project Directory

```bash
# Create a new directory
mkdir suvidha_app
cd suvidha_app
```

### 3️⃣ Set Up a Virtual Environment

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

1. Create a `.env` file in the root directory:

   ```plaintext
   GOOGLE_API_KEY=your_google_api_key_here
   ```

2. Replace `your_google_api_key_here` with your actual Google API Key.

---

## 🚀 Run the Application

Start the Streamlit application by running:

```bash
streamlit run app.py
```

---

## 📋 Requirements

- **Python**: 3.8+
- **Dependencies**: Installed via `requirements.txt`:

  ```plaintext
  streamlit==1.31.0
  google-generativeai==0.3.1
  Pillow==10.0.0
  python-dotenv==1.0.0
  pandas==2.1.0
  ```

---

## 🖼️ Screenshots

 📸
![image](https://github.com/user-attachments/assets/46f210ae-aaa8-462d-8ce6-1b84be5185fb)

![image](https://github.com/user-attachments/assets/5d085599-251e-488f-b4a7-d77035d2dae9)

![image](https://github.com/user-attachments/assets/2fd6c17e-ef24-437d-94e7-04a92585837f)


---

## 🤝 Contribution

Contributions are welcome! Follow these steps:

1. Fork the repository
2. Create a new branch (`feature/your-feature-name`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature-name`)
5. Open a Pull Request

---

## 📧 Contact

Developed by [Shivam Singh](https://github.com/shibbu04) 🌟

Feel free to reach out for any queries or feedback!
