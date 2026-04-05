import streamlit as st
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Setup OpenAI only
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("Interview Story Builder - OpenAI")

# User input
resume_bullet = st.text_area("Paste your resume bullet or project description:")
question_type = st.selectbox("Select question type:", 
                           ["Tell me about a time you...", "Achievement", "Challenge", "Teamwork"])

if st.button("Generate STAR Story (OpenAI)"):
    if resume_bullet:
        # STAR prompt template
        prompt = f"""
        Convert this resume bullet into a STAR interview story for: {question_type}
        
        Resume: {resume_bullet}
        
        Return ONLY in this format:
        **Situation:** [text]
        **Task:** [text]
        **Action:** [text]
        **Result:** [text]
        """
        
        # OpenAI only
        with st.container():
            st.subheader("OpenAI STAR Story")
            with st.spinner("Generating..."):
                openai_response = openai_client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                )
                st.markdown(openai_response.choices[0].message.content)
    else:
        st.warning("Please enter a resume bullet.")