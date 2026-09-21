import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Streamlit App Portfolio", layout="wide")

# ⚡ CSS TRICK TO INJECT CUSTOM STYLES (Turns radio buttons into prominent clickable rows)
st.markdown("""
    <style>
    /* Make the container look organized and readable */
    div[data-testid="stRadio"] > label {
        font-size: 1.15rem !important;
        font-weight: bold !important;
        color: #1F2937 !important;
        margin-bottom: 12px !important;
    }
    
    /* Transform each option row into a highlighted interactive strip */
    div[data-testid="stRadio"] div[role="radiogroup"] > label {
        background-color: #F3F4F6 !important; /* Soft grey background */
        border: 2px solid #E5E7EB !important; /* Discrete border */
        border-radius: 8px !important;        /* Rounded corners */
        padding: 12px 16px !important;         /* Breathing room inside card */
        margin-bottom: 10px !important;        /* Gap between choices */
        width: 100% !important;                /* Full sidebar width */
        cursor: pointer !important;
        transition: all 0.2s ease-in-out !important;
    }
    
    /* Hover effect: Subtle elevation shift */
    div[data-testid="stRadio"] div[role="radiogroup"] > label:hover {
        background-color: #EEF2F6 !important;
        border-color: #3B82F6 !important;      /* Changes to bright blue border */
        transform: translateY(-1px);
    }
    
    /* Active selection styling: Pops out to show exactly where the user is */
    div[data-testid="stRadio"] div[role="radiogroup"] > label[data-checked="true"] {
        background-color: #EFF6FF !important;  /* Light blue tint */
        border-color: #2563EB !important;      /* Deep premium blue boundary */
        font-weight: 600 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Main Page Headers
st.title("🚀 My Streamlit App Portfolio")
st.write("Welcome! Use the interactive navigation blocks in the sidebar to jump between categories instantly.")
st.divider()

# 3. Sidebar Exclusive Filter (Styled Radio Menu)
st.sidebar.header("🎯 Navigation Menu")

# The CSS block above will automatically redesign this widget into beautiful cards
selected_section = st.sidebar.radio(
    "Choose a domain to explore:",
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
        st.write("Predict numbers and continuous trends (e.g., Sales, Pricing forecast).")
        st.link_button("Open Regression App", "https://streamlit.app")

    with col8:
        st.subheader("⚡ Classification + Regression")
        st.write("Dual-purpose models executing multi-task predictions simultaneously.")
        st.link_button("Open Joint ML App", "https://streamlit.app")

    st.divider()
