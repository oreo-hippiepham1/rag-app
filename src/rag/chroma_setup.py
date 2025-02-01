from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()

def get_chroma_db():
    persist = st.secrets['CHROMA_DB_DIR']

    return Chroma(
        collection_name='yt_data',
        embedding_function=OpenAIEmbeddings(model='text-embedding-3-small'),
        persist_directory=persist
    )
