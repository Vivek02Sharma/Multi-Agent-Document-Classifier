import streamlit as st
import requests

st.set_page_config(page_title = "Multi-Agent", layout = "centered")

st.title("Multi-Agent Document Classifier")

st.markdown("Upload a file (PDF, JSON) or paste email content. The app will classify and process it.")

# fastapi url
API_URL = "http://localhost:8000/process"

uploaded_file = st.file_uploader("Upload File (PDF or JSON)", type = ["pdf", "json"])
text_input = st.text_area("Enter your text here", height = 200)

submit = st.button("Process")

if submit:
    if uploaded_file:
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}
        response = requests.post(API_URL, files = files)
    elif text_input.strip():
        response = requests.post(API_URL, files = {"file": ("email.txt", text_input)})
    else:
        st.warning("Please upload a file or enter your text.")
        st.stop()

    if response.ok:
        result = response.json()
        st.success("✅ Processed successfully!")
        
        st.subheader("🔎 Detected Format & Intent")
        st.write(f"**Thread Id:** {result.get('thread_id')}")
        st.write(f"**Format:** {result.get('format')}")
        st.write(f"**Intent:** {result.get('intent')}")

        st.subheader("📤 Extracted Output")
        st.json(result.get("content"))

    else:
        st.error("❌ Error processing file.")
