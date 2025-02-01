from src.rag import get_qa_chain, get_chroma_db, get_llm
from src.utilities import format_results, display_results

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv

load_dotenv()


def main():
    vectorstore = get_chroma_db()
    llm = get_llm()

    rag_chain = get_qa_chain(vectorstore, llm, k=5)

    # Runs a query
    query = "which celebrities were associated with the Epstein case?"
    result = rag_chain.invoke({'input': query})

    # Prints results
    answer = result['answer']
    source = result['context']
    print(f"Answer: {answer}")

    print("Sources:")
    grouped_results = format_results(source)
    display_results(grouped_results)


if __name__ == '__main__':
    main()