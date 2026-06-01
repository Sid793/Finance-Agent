import streamlit as st
import google.generativeai as genai
from crewai import Agent,task,Crew
from langchain_google_genai import
ChatGoogleGenerativeAI
# =========================

# GEMINI API KEY
# =========================
genai.configure(api_key="AIzaSyBUghPPndVJFZpcH2cACBDFAgMcwtP10-E")

# Load Gemini Model
model = genai.GenerativeModel("gemini-2.5-flash")

# =========================
# STREAMLIT UI
# =========================

st.title("💰 Financial Advisor Chatbot")

st.write("Ask me anything about savings, budgeting, investing, and money management.")

# User Input
user_input = st.text_input("Enter your question:")

if st.button("Ask"):

    if user_input:

        prompt = f"""
        You are a professional financial advisor chatbot.

        Give simple and beginner-friendly financial advice.

        User Question:
        {user_input}
        """

        response = model.generate_content(prompt)

        st.subheader("Advisor Response:")
        st.write(response.text)

    else:
        st.warning("Please enter a question.")