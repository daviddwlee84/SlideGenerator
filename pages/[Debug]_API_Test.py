import streamlit as st
import utils


st.set_page_config(page_title="Debug: API Test")
st.title("Debug: API Test")

with st.sidebar:
    openai_selection = utils.generate_api_and_language_model_selection()


"""
- TODO: Test OpenAI API is working
"""
