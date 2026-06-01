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
    page_title="Mental Health Advisor",
    page_icon="🧠"
)

st.title("🧠 AI Mental Health Advisor")

st.write(
    "Talk about stress, anxiety, study pressure, motivation, productivity, and emotional wellness."
)

st.info(
    "⚠️ This AI is not a licensed therapist or doctor. "
    "For serious mental health concerns, contact a qualified professional."
)

# =========================
# USER INPUT
# =========================

user_input = st.text_area(
    "How are you feeling today?"
)

# =========================
# BUTTON
# =========================

if st.button("Get Support"):

    if user_input.strip() != "":

        with st.spinner("Thinking..."):

            prompt = f"""
            You are a supportive and calm mental wellness assistant.

            Your job:
            - Give supportive and positive responses
            - Suggest healthy coping techniques
            - Encourage balance, sleep, exercise, and communication
            - Keep responses gentle, beginner-friendly, and practical
            - Never give harmful advice
            - Do not pretend to be a doctor

            User Message:
            {user_input}
            """

            try:

                response = model.generate_content(prompt)

                st.subheader("💙 Supportive Response")

                st.write(response.text)

            except Exception as e:

                st.error(f"Error: {e}")

    else:

        st.warning("Please enter your thoughts or feelings.")