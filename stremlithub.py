import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Streamlit App Portfolio", layout="wide")

st.title("🚀 My Streamlit App Portfolio")
st.write("Welcome! Use the sidebar to switch between categories instantly.")
st.divider()

# 2. Sidebar Exclusive Filter (Radio Menu)
st.sidebar.header("🎯 Navigation Menu")
st.sidebar.write("Choose a single domain to view:")

# Radio selection forces exactly ONE active view at a time
selected_section = st.sidebar.radio(
    "Select Domain:",
    options=[
        "Show All Apps",  # Default landing view
        "Clustering & Anomaly Detection",
        "Natural Language Processing (NLP)",
        "Core Machine Learning Applications"
    ]
)

# ==========================================
# SECTION 1: Unsupervised Learning & Analytics
# ==========================================
if selected_section == "Show All Apps" or selected_section == "Clustering & Anomaly Detection":
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
if selected_section == "Show All Apps" or selected_section == "Natural Language Processing (NLP)":
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
if selected_section == "Show All Apps" or selected_section == "Core Machine Learning Applications":
    st.header("🤖 3. Core Machine Learning Applications")
    col6, col7, col8 = st.columns(3)

    with col6:
        st.subheader("🎯 Classification")
        st.write("Predict distinct categories and labels (e.g., Churn, Default prediction).")
        st.link_button("Open Classification App", "https://streamlit.app")

    with col7:
        st.subheader("📉 Regression")
        st.write("Predict numbers and continuous trends (e.g., Sales, Pricing forecast).")
        st.link_button("Open Regression App", "https://streamlit.app")

    with col8:
        st.subheader("⚡ Classification + Regression")
        st.write("Dual-purpose models executing multi-task predictions simultaneously.")
        st.link_button("Open Joint ML App", "https://streamlit.app")

    st.divider()
