import streamlit as st
import requests

st.set_page_config(page_title="AI Code Generator", layout="centered")
st.title("🧠 AI Code Generator")

st.markdown("Enter a prompt and get AI-generated code from the FastAPI backend.")

with st.form("code_gen_form"):
    prompt = st.text_area("💬 Describe what you want to build:", height=150)
    submitted = st.form_submit_button("🚀 Generate Code")

if submitted and prompt:
    with st.spinner("Sending prompt to backend..."):
        try:
            res = requests.post("http://localhost:8000/ai/generate-code", json={"prompt": prompt})
            if res.status_code == 200:
                st.success("✅ Code generated successfully!")
                st.code(res.text, language="python")
            else:
                st.error(f"❌ Error from backend: {res.text}")
        except Exception as e:
            st.error(f"❌ Request failed: {e}")
