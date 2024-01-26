import streamlit as st
import utils

st.set_page_config(page_title="Debug: File Analysis")
st.title("Debug: File Analysis")

with st.sidebar:
    openai_selection = utils.generate_api_and_language_model_selection()


file = st.file_uploader("Upload file", accept_multiple_files=False)
st.write(file)

"""
- TODO: Try extract different file document types here
- TODO: List document content like paragraphs, table of contents, pictures, tables, etc.
"""
