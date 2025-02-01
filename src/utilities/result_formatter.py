from typing import List, Dict, Any
from collections import defaultdict

from langchain_core.documents import Document

def format_results(results: List[Document]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Groups results by title and formats them for display.

    Args:
        results (List[Document]): The retrieved documents (containing metadata and content).

    Returns:
        Dict[str, List[Dict[str, Any]]]: A dictionary where keys are titles and values are lists of timestamps and URLs.
    """
    grouped_results = defaultdict(list)

    for doc in results:
        title = doc.metadata['title']
        start_time = int(doc.metadata['start'])
        url = f"{doc.metadata['url']}&t={start_time}s"

        grouped_results[title].append({
            'start_time': start_time,
            'url': url
        })

    return grouped_results


def display_results(grouped_results: Dict[str, List[Dict[str, Any]]]):
    """
    Displays the grouped results.

    Args:
        grouped_results (Dict[str, List[Dict[str, Any]]]): The grouped results.
    """
    for title, entry_list in grouped_results.items():
        print(f"\n{title}:")
        for e in entry_list:
            print(f"- {e['start_time']//60}m{e['start_time']%60}s: {e['url']}")