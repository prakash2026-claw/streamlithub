import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Streamlit App Portfolio", layout="wide")

# 🎨 LIGHT SIDEBAR TINT: Clean separation without distraction
# Choose one color below. Currently using a very soft, professional ice-blue/grey (#F0F4F8).
# Alternative ideas: Soft green (#F0FDFC) or warm cream (#FDFBF7)
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #F0F4F8 !important; 
        border-right: 1px solid #E2E8F0 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Main Page Headers
st.title("🚀 My Streamlit App Portfolio")
st.write("Welcome! Use the navigation menu in the sidebar to filter through my projects.")
st.divider()

# 3. Sidebar Radio Setup (Back to clean, standard look)
st.sidebar.header("🎯 Navigation Menu")

selected_section = st.sidebar.radio(
    "Choose a domain to view:",
    options=[
        "✨ Show All Apps",
        "🔍 Clustering & Anomaly Detection",
        "💬 Natural Language Processing (NLP)",
        "🤖 Core Machine Learning Applications"
    ]
)

# ==========================================
# SECTION 1: Unsupervised Learning & Analytics
# ==========================================
if selected_section == "✨ Show All Apps" or selected_section == "🔍 Clustering & Anomaly Detection":
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
if selected_section == "✨ Show All Apps" or selected_section == "💬 Natural Language Processing (NLP)":
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
if selected_section == "✨ Show All Apps" or selected_section == "🤖 Core Machine Learning Applications":
    st.header("🤖 3. Core Machine Learning Applications")
    col6, col7, col8 = st.columns(3)

    with col6:
        st.subheader("🎯 Classification")
        st.write("Predict distinct categories and labels (e.g., Churn, Default prediction).")
        st.link_button("Open Classification App", "https://streamlit.app")

    with col7:
        st.subheader("📉 Regression")
        st.write("Bank Operational Cost per month.")
        st.link_button("Open Regression App", "https://kaggle-models-pjf6kck2czs57f2t5be2ah.streamlit.app/")

    with col8:
        st.subheader("⚡ Classification + Regression")
        st.write("Dual-purpose models executing multi-task predictions simultaneously.")
        st.link_button("Open Joint ML App", "https://streamlit.app")

    st.divider()
