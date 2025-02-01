from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings

from pinecone import Pinecone, ServerlessSpec

import streamlit as st


def get_pinecone_db():
    PINECONE_API_KEY = st.secrets['PINECONE_API_KEY']
    pc = Pinecone(api_key=PINECONE_API_KEY)

    existing_indexes = [index_info["name"] for index_info in pc.list_indexes()]
    index_name = "rotten-mango-data-v1"

    if index_name not in existing_indexes:
        pc.create_index(
            name=index_name,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region="us-east-1"),
        )

    index = pc.Index(index_name)
    embeddings = OpenAIEmbeddings(model='text-embedding-3-small', api_key=st.secrets['OPENAI_API_KEY'])

    return PineconeVectorStore(index=index, embedding=embeddings)