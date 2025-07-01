import streamlit as st
import requests

st.set_page_config(page_title="SmartSDLC")
st.title("SmartSDLC Dashboard 🚀")

st.write("Welcome to the AI-powered Software Development Lifecycle Assistant!")

with st.form("chat_form"):
    message = st.text_input("Ask the Assistant:")
    if st.form_submit_button("Send"):
        res = requests.post("http://localhost:8000/chat/chat", json=message)
        st.success(res.json()['reply'])
