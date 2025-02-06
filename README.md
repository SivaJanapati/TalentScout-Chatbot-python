## TalentScout-Chatbot-python
#TalentScout - Hiring Assistant Chatbot

#Project Overview

TalentScout is an AI-powered chatbot designed to assist recruiters in evaluating job candidates. It collects candidate information, stores it in a database, and generates technical questions tailored to the candidate’s skillset using OpenAI's GPT-4o model. The chatbot is built using Streamlit for an interactive UI, OpenAI’s API for AI-driven responses, and SQLite for data storage.

#Installation & Setup Guide

#Prerequisites

Ensure you have the following installed:

Python 3.8+

pip (Python package manager)

Git (for deployment via GitHub)

Steps to Set Up Locally

#Clone the Repository:

git clone https://github.com/yourusername/talentscout-chatbot.git
cd talentscout-chatbot

#Create a Virtual Environment (Recommended):

python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows

#Install Dependencies:

pip install -r requirements.txt

#Set Up Environment Variables:

Create a .env file in the root directory and add:

OPENAI_API_KEY=your_openai_api_key

Alternatively, set it in your system environment variables.

Run the Application:

streamlit run app.py

#How the Chatbot Works

Users enter candidate details (Name, Email, Experience, Tech Stack, etc.).

The chatbot stores the data in an SQLite database.

The chatbot generates technical questions based on the candidate’s tech stack using OpenAI’s GPT-4o model.

The generated questions are displayed to the user.

#API & Database Details

OpenAI API Usage

Model Used: gpt-4o-mini

Purpose: Generates relevant technical questions based on the candidate’s tech stack.

Example API Call:

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a recruitment assistant."},
        {"role": "user", "content": prompt}
    ]
)

#Database (SQLite)

Database Name: candidates.db

Table Structure:

CREATE TABLE IF NOT EXISTS candidates (
    name TEXT,
    email TEXT,
    phone TEXT,
    experience TEXT,
    position TEXT,
    location TEXT,
    tech_stack TEXT
);

Data Insertion:

cursor.execute("INSERT INTO candidates VALUES (?, ?, ?, ?, ?, ?, ?)",
              (name, email, phone, experience, position, location, tech_stack))
conn.commit()

#Deployment

Deploying to Streamlit Cloud

Push your project to GitHub:

git add .
git commit -m "Initial commit"
git push origin main

Log in to Streamlit Cloud.

Create a new app and connect your GitHub repository.

Set environment variables (OPENAI_API_KEY) in Streamlit's secrets manager.

Deploy and test your chatbot.
