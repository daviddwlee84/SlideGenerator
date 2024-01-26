import streamlit as st
import utils
from dotenv import load_dotenv
import os

curr_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(curr_dir, ".env"))

st.set_page_config(page_title="Slide Generator")
st.title("Slide Generator")

with st.sidebar:
    openai_selection = utils.generate_api_and_language_model_selection()

files = st.file_uploader("Upload files", accept_multiple_files=True)
additional_content = st.text_area("Content to supplement")

st.write(files)
st.write(additional_content)

"""
1. TODO: Load documents and additional contents to LlamaIndex
2. TODO: Slide template / style selection => Decide which prompt set / chain to use
3. TODO: Combine results and dump into Marp readable format
4. TODO: Add download button to trigger Marp generation => html, pdf, pptx
"""
