import streamlit as st
import requests

st.set_page_config(page_title="Bug Fixer", layout="centered")
st.title("🐞 Bug Fixer")

st.markdown("Paste buggy code and let the backend AI fix it.")

with st.form("bug_fix_form"):
    buggy_code = st.text_area("🐛 Buggy Code", height=200)
    submitted = st.form_submit_button("🛠️ Fix Bugs")

if submitted and buggy_code:
    with st.spinner("Sending buggy code to backend..."):
        try:
            res = requests.post("http://localhost:8000/ai/fix-bugs", json={"code": buggy_code})
            if res.status_code == 200:
                st.success("✅ Bug fixed successfully!")
                st.code(res.text, language="python")
            else:
                st.error(f"❌ Error from backend: {res.text}")
        except Exception as e:
            st.error(f"❌ Request failed: {e}")
