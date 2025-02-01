from typing import List, Dict, Any

from langchain_chroma import Chroma
from langchain import hub
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

def get_qa_chain(vectorstore: Chroma, llm, k: int=3):
    retriever = vectorstore.as_retriever(searck_kwargs={
        'k': k
    })

    prompt = hub.pull("langchain-ai/retrieval-qa-chat")

    combine_docs_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
    rag_chain = create_retrieval_chain(
        retriever=retriever,
        combine_docs_chain=combine_docs_chain
    )

    return rag_chain