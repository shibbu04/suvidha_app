import streamlit as st
from datetime import datetime
import time
from src.database import save_document, get_user_documents

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

def show_documents():
    st.markdown('<div class="main-header"><h2>📄 Document Management</h2></div>', 
                unsafe_allow_html=True)
    
    # Document upload form
    with st.form("document_upload"):
        col1, col2 = st.columns(2)
        with col1:
            doc_type = st.selectbox("Document Type", 
                ["Aadhar Card", "PAN Card", "Income Certificate", "Address Proof"])
        with col2:
            file = st.file_uploader("Choose file", type=['pdf', 'jpg', 'png'])
        
        doc_number = st.text_input("Document Number (for verification)")
        submit_button = st.form_submit_button("Upload & Verify")
        
        if submit_button and file and doc_number:
            with st.spinner("Uploading and verifying document..."):
                # Verify document
                verifier = DocumentVerifier()
                result = verifier.verify_document(doc_type, doc_number, 
                                               st.session_state.current_user.get('state'))
                
                if result["valid"]:
                    doc_data = {
                        "user_email": st.session_state.current_user['email'],
                        "type": doc_type,
                        "filename": file.name,
                        "number": doc_number,
                        "upload_date": str(datetime.now().date()),
                        "status": "Verified"
                    }
                    save_document(doc_data)
                    if doc_type not in st.session_state.verified_documents:
                        st.session_state.verified_documents.append(doc_type)
                    st.success("Document verified and uploaded successfully!")
                else:
                    st.error(result["message"])

    # Display uploaded documents
    st.subheader("My Documents")
    docs = get_user_documents(st.session_state.current_user['email'])
    
    if not docs:
        st.info("No documents uploaded yet.")
    else:
        for doc in docs:
            with st.expander(f"{doc['type']} - {doc['status']}"):
                st.markdown(f"""
                    <div class="card">
                        <p><strong>Document Type:</strong> {doc['type']}</p>
                        <p><strong>Status:</strong> {doc['status']}</p>
                        <p><strong>Upload Date:</strong> {doc['upload_date']}</p>
                        <p><strong>Document Number:</strong> {doc.get('number', 'N/A')}</p>
                    </div>
                """, unsafe_allow_html=True)