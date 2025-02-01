import streamlit as st

from src.rag import get_qa_chain, get_pinecone_db, get_llm
from src.utilities import format_results, display_results

def display_result_st(grouped_results):
    for title, entry_list in grouped_results.items():
        st.markdown(f"**{title}**")
        for e in entry_list:
            mins, secs = divmod(e["start_time"], 60)
            full_url = f"https://{e['url']}" if not e['url'].startswith("http") else e['url']
            st.markdown(f"- [{mins}m{secs}s]({full_url})")


# Quick UI
def main():
    st.title('Rotten Mango 🥭 Podcast - RAG')
    st.write('Ask any questions on the 🔎🕵️‍♂️🔪 truecrime podcasts!')

    vector_store = get_pinecone_db()
    llm = get_llm()

    # Input query
    query = st.text_input('Enter your question:',
                        placeholder="e.g., which celebs were associated with the Epstein case?")

    button = st.button('Ask')
    if button:
        with st.spinner('Searching for answer...'):
            # Creates QA chain
            rag_chain = get_qa_chain(vector_store, llm, k=5)

            # Runs the query
            result = rag_chain.invoke({'input': query})

            # Prints results
            st.subheader('Answer')
            answer = result['answer']
            st.markdown(f"{answer}")

            st.subheader("Sources")
            grouped_results = format_results(result['context'])
            display_result_st(grouped_results)


if __name__ == '__main__':
    main()