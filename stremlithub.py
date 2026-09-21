import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Streamlit App Portfolio", layout="wide")

st.title("🚀 My Streamlit App Portfolio")
st.write("Welcome! Use the sidebar to filter categories, or click any link below to open an app instantly.")
st.divider()

# 2. Sidebar Filter Configuration
st.sidebar.header("🎯 Portfolio Filters")
st.sidebar.write("Select the domains you want to view:")

# Available categories mapped to their sections
available_sections = [
    "Clustering & Anomaly Detection",
    "Natural Language Processing (NLP)",
    "Core Machine Learning Applications"
]

# Multi-select widget in sidebar
selected_sections = st.sidebar.multiselect(
    "Filter by Domain:",
    options=available_sections,
    default=available_sections # Displays all by default
)

# Fallback in case the user clears all checkboxes
if not selected_sections:
    st.info("💡 Please select at least one domain in the sidebar to view apps.")

# ==========================================
# SECTION 1: Unsupervised Learning & Analytics
# ==========================================
if "Clustering & Anomaly Detection" in selected_sections:
    st.header("🔍 1. Clustering & Anomaly Detection")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Clustering Models")
        st.write("Group data points based on feature similarities.")
        st.link_button("Open Clustering App", "https://streamlit.app")

    with col2:
        st.subheader("⚠️ Anomaly Detection")
        st.write("Identify outliers, fraud, and unusual patterns in your datasets.")
        st.link_button("Open Anomaly App", "https://streamlit.app")

    st.divider()

# ==========================================
# SECTION 2: Natural Language Processing (NLP)
# ==========================================
if "Natural Language Processing (NLP)" in selected_sections:
    st.header("💬 2. Natural Language Processing (NLP)")
    col3, col4, col5 = st.columns(3)

    with col3:
        st.subheader("🏷️ NLP (Classification)")
        st.write("Text analysis tasks like sentiment detection or spam filtering.")
        st.link_button("Open NLP Classification", "https://streamlit.app")

    with col4:
        st.subheader("📈 NLP (Regression)")
        st.write("Predict continuous values from text (e.g., essay grading scores).")
        st.link_button("Open NLP Regression", "https://streamlit.app")

    with col5:
        st.subheader("🧠 NLP (Classification + Regression)")
        st.write("Combined pipeline generating both labels and numeric scores from text inputs.")
        st.link_button("Open Hybrid NLP App", "https://streamlit.app")

    st.divider()

# ==========================================
# SECTION 3: Standard Machine Learning
# ==========================================
if "Core Machine Learning Applications" in selected_sections:
    st.header("🤖 3. Core Machine Learning Applications")
    col6, col7, col8 = st.columns(3)

    with col6:
        st.subheader("🎯 Classification")
        st.write("Predict distinct categories and labels (e.g., Churn, Default prediction).")
        st.link_button("Open Classification App", "https://streamlit.app")

    with col7:
        st.subheader("📉 Regression")
        st.write("Predict numbers and continuous trends (e.g., Sales, Pricing forecast).")
        st.link_button("Open Regression App", "https://kaggle-models-a3vmespwdbjyhqxxoavuvb.streamlit.app/")

    with col8:
        st.subheader("⚡ Classification + Regression")
        st.write("Dual-purpose models executing multi-task predictions simultaneously.")
        st.link_button("Open Joint ML App", "https://streamlit.app")

    st.divider()
