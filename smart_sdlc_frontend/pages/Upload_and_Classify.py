import streamlit as st
import requests

st.set_page_config(page_title="Requirement Classifier", layout="centered")
st.title("📂 Upload and Classify Requirements")

st.markdown("Upload a plain text file of software requirements. The backend will classify them.")

uploaded_file = st.file_uploader("📎 Upload a .txt file", type=["txt"])

if uploaded_file:
    content = uploaded_file.read().decode("utf-8")
    with st.spinner("Sending to backend..."):
        try:
            res = requests.post("http://localhost:8000/ai/analyze-requirements", json={"text": content})
            if res.status_code == 200:
                st.success("✅ Classification successful!")
                st.markdown(res.text)
            else:
                st.error(f"❌ Backend error: {res.text}")
        except Exception as e:
            st.error(f"❌ Request failed: {e}")