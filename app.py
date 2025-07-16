# app.py

import streamlit as st
from model_utils import simplify_homework_question

st.set_page_config(page_title="AI Homework Helper", page_icon="📚")
st.title("📚 AI Homework Helper for Busy Parents")
st.write("Ask any CBC homework question and get a simple, child-friendly explanation.")

# Input box
user_input = st.text_area("✍️ Enter Homework Question", placeholder="e.g., Explain what energy transformation happens when a bulb lights up.")

# When 'Explain' button is clicked
if st.button("🧠 Explain"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            explanation = simplify_homework_question(user_input)
        st.success("Here’s a simple explanation:")
        st.markdown(f"🗣️ **{explanation}**")
    else:
        st.warning("Please enter a question before clicking Explain.")
