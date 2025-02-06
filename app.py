import streamlit as st
from openai import OpenAI
import sqlite3
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("⚠️ OpenAI API key not found. Set it in a `.env` file or environment variable.")
else:
    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

# Database Setup
conn = sqlite3.connect("candidates.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS candidates
                (name TEXT, email TEXT, phone TEXT, experience TEXT, 
                position TEXT, location TEXT, tech_stack TEXT)''')

# Chatbot Greeting
st.title("TalentScout - Hiring Assistant Chatbot")
st.write("Welcome! I'll assist you with the hiring process. Let's begin.")

# Candidate Information
name = st.text_input("Full Name")
email = st.text_input("Email Address")
phone = st.text_input("Phone Number")
experience = st.selectbox("Years of Experience", ["0-1", "2-4", "5-8", "9+"])
position = st.text_input("Desired Position")
location = st.text_input("Current Location")
tech_stack = st.text_area("Tech Stack (e.g., Python, React, AWS)")

if st.button("Submit Details"):
    if not api_key:
        st.error("⚠️ API key missing! Cannot generate technical questions.")
    else:
        # Save to database
        cursor.execute("INSERT INTO candidates VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (name, email, phone, experience, position, location, tech_stack))
        conn.commit()
        st.success("Information recorded! Generating technical questions...")
        
        # Generate Technical Questions
        prompt = f"Generate 3-5 technical questions for a candidate skilled in {tech_stack}. Keep them relevant and concise."
        
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a recruitment assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        questions = response.choices[0].message.content
        st.write("Here are your technical questions:")
        st.write(questions)
