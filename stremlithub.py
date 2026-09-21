import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Streamlit App Portfolio", layout="wide")

# ⚡ THE VISUAL OVERHAUL: Dark Sidebar + Bright Glowing Navigation Blocks
st.markdown("""
    <style>
    /* 1. FORCE DARK BACKGROUND FOR THE ENTIRE SIDEBAR CONTAINER */
    [data-testid="stSidebar"] {
        background-color: #1E293B !important; /* Deep charcoal navy blue */
    }
    
    /* 2. FORCE TEXT INSIDE SIDEBAR TO BE CLEAN WHITE (FOR CONTRAST) */
    [data-testid="stSidebar"] *, [data-testid="stSidebar"] label {
        color: #FFFFFF !important;
    }
    
    /* 3. TRANSFORM RADIO LAYOUT INTO LARGE EXCLUSIVE CLICKABLE BLOCKS */
    div[data-testid="stRadio"] div[role="radiogroup"] > label {
        background-color: #334155 !important; /* Dark slate grey blocks */
        border: 2px solid #475569 !important; /* Clear frame lines */
        border-radius: 10px !important;       /* Clean rounded edges */
        padding: 14px 18px !important;        /* Large padding for an easy click target */
        margin-bottom: 12px !important;       /* Space between buttons */
        width: 100% !important;               /* Span across sidebar layout widths */
        cursor: pointer !important;
        transition: all 0.25s ease-in-out !important;
    }
    
    /* 4. HOVER INTERACTION STYLING */
    div[data-testid="stRadio"] div[role="radiogroup"] > label:hover {
        background-color: #475569 !important; /* Lighter slate on hover */
        border-color: #60A5FA !important;     /* Bright blue glowing border */
    }
    
    /* 5. DYNAMIC STATE: SELECTED BLOCK POP-OUT */
    div[data-testid="stRadio"] div[role="radiogroup"] > label[data-checked="true"] {
        background-color: #2563EB !important; /* Vivid Premium Blue fills the box */
        border-color: #3B82F6 !important;     /* High-luminance accent borders */
        font-weight: 700 !important;          /* Strong text callout */
        box-shadow: 0px 4px 12px rgba(37, 99, 235, 0.3) !important; /* Outer glow drop shadow */
    }
    
    /* HIDE THE DEFAULT TINY STREAMLIT RADIO CIRCLE ICONS TO PREVENT CLUTTER */
    div[data-testid="stRadio"] div[role="radiogroup"] > label div:first-child {
        display: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Main Page Content Structure
st.title("🚀 My Streamlit App Portfolio")
st.write("Welcome! Use the interactive navigation blocks in the dark sidebar menu to filter through project disciplines.")
st.divider()

# 3. Sidebar Radio Setup (The custom CSS rules above target this directly)
st.sidebar.markdown("### 🎯 Portfolio Tracks")

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
        st.write("Predict numbers and continuous trends (e.g., Sales, Pricing forecast).")
        st.link_button("Open Regression App", "https://streamlit.app")

    with col8:
        st.subheader("⚡ Classification + Regression")
        st.write("Dual-purpose models executing multi-task predictions simultaneously.")
        st.link_button("Open Joint ML App", "https://streamlit.app")

    st.divider()
