import streamlit as st
from google import genai

st.title("Aqua AI Math Teacher 🌊")

# 1. Initialize Client - Ensure your Secret is named GEMINI_API_KEY
client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# 2. User Inputs
language = st.selectbox("Choose Language", ["English", "French", "Pidgin", "Spanish"])
question = st.text_input("Ask a math question:")

if st.button("Ask Aqua 🌊"):
    if question:
        try:
            # THE TRUTH: You MUST use 'models/' prefix and '1.5' to get past the 429 error
            response = client.models.generate_content(
                model ="geminni-3.0-flash",
                contents=f"You are Aqua, a friendly math teacher. Answer in {language}: {question}"
            )
            st.write(f"**Aqua:** {response.text}")
        except Exception as e:
            st.error(f"Technical Block: {e}")
    else:
        st.warning("Please enter a question first!")
