import streamlit as st
import google.generativeai as genai

# =========================
# GEMINI API KEY
# =========================

genai.configure(api_key="AIzaSyBUghPPndVJFZpcH2cACBDFAgMcwtP10-E")

# =========================
# LOAD GEMINI MODEL
# =========================

model = genai.GenerativeModel("gemini-2.5-flash")

# =========================
# STREAMLIT UI
# =========================

st.set_page_config(
    page_title="Study Planner Agent",
    page_icon="📚"
)

st.title("📚 AI Study Planner Agent")

st.write(
    "Create smart study plans for exams, coding, UPSC, college subjects, and daily learning."
)

# =========================
# USER INPUTS
# =========================

goal = st.text_input("What do you want to study?")

hours = st.slider(
    "How many hours can you study daily?",
    1,
    15,
    4
)

days = st.number_input(
    "How many days do you have?",
    min_value=1,
    max_value=365,
    value=30
)

# =========================
# BUTTON
# =========================

if st.button("Generate Study Plan"):

    if goal:

        with st.spinner("Creating your study plan..."):

            prompt = f"""
            You are an expert AI Study Planner.

            Create a simple, practical, and beginner-friendly study plan.

            Student Goal:
            {goal}

            Study Hours Per Day:
            {hours}

            Total Days Available:
            {days}

            Give:
            - Daily study routine
            - Topics to focus on
            - Revision strategy
            - Break suggestions
            - Motivation tips

            Keep the response clear and structured.
            """

            try:

                response = model.generate_content(prompt)

                st.subheader("📌 Your Study Plan")

                st.write(response.text)

            except Exception as e:

                st.error(f"Error: {e}")

    else:

        st.warning("Please enter a study goal.")