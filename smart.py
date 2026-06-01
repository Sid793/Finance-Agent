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
    page_title="Smart Product Recommendation Agent",
    page_icon="🛍️"
)

st.title("🛍️ Smart Product Recommendation Agent")

st.write(
    "Get AI-powered recommendations for smartphones, laptops, headphones, smartwatches, and more."
)

# =========================
# USER INPUTS
# =========================

product_type = st.selectbox(
    "Select Product Category",
    [
        "Smartphone",
        "Laptop",
        "Headphones",
        "Smartwatch",
        "Tablet",
        "Camera",
        "Gaming Laptop"
    ]
)

budget = st.text_input("Enter Your Budget")

purpose = st.text_input(
    "Purpose (gaming, coding, study, photography, office work, etc.)"
)

brand_preference = st.text_input(
    "Preferred Brand (Optional)"
)

# =========================
# BUTTON
# =========================

if st.button("Recommend Products"):

    if budget and purpose:

        with st.spinner("Finding best products for you..."):

            prompt = f"""
            You are an expert smart product recommendation AI.

            Recommend the best products based on user needs.

            Product Category:
            {product_type}

            Budget:
            {budget}

            Purpose:
            {purpose}

            Preferred Brand:
            {brand_preference}

            Give:
            - Top 3 product recommendations
            - Key features
            - Pros and cons
            - Estimated price
            - Best overall recommendation

            Keep answers beginner-friendly and easy to understand.
            """

            try:

                response = model.generate_content(prompt)

                st.subheader("📌 Recommended Products")

                st.write(response.text)

            except Exception as e:

                st.error(f"Error: {e}")

    else:

        st.warning("Please fill all required fields.")