from langchain_openai import ChatOpenAI

import streamlit as st

from dotenv import load_dotenv
load_dotenv()

def get_llm():
    llm = ChatOpenAI(model='gpt-4o-mini', api_key=st.secrets['OPENAI_API_KEY'])
    return llm