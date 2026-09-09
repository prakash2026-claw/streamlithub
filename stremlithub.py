import streamlit as st

st.title("🚀 My Streamlit App Portfolio")
st.write("Click any of the links below to open my apps instantly (no login required).")

# App 1
st.subheader("📊 test app ")
st.write("A cool tool to analyze sales trends.")
st.link_button("Open App", "https://kaggle-models-a3vmespwdbjyhqxxoavuvb.streamlit.app/")

st.divider()

# App 2
st.subheader("🤖 Image Classifier")
st.write("Upload an image to detect objects.")
st.link_button("Open App", "https://streamlit.app")

# ... Repeat for your other apps
