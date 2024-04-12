from collections import defaultdict
from heapq import nsmallest

import pytest


def build_index(documents: list[str]) -> dict:
    index = defaultdict(list)
    for doc_id, document in enumerate(documents, 1):
        words = document.split()
        for word in words:
            index[word].append(doc_id)
    return index


def search(index: dict, query: str) -> list[int]:
    query_words = set(query.split())
    relevance: dict = defaultdict(int)
    for word in query_words:
        for doc_id in index.get(word, []):
            relevance[doc_id] += 1
    return [result[0] for result in nsmallest(5, relevance.items(), key=lambda item: (-item[1], item[0]))]


def search_engine(documents: list[str], queries: list[str]) -> list[list[int]]:
    indx = build_index(documents)
    return [search(index=indx, query=query) for query in queries]


def main():
    n = int(input())
    input_docs = [input() for _ in range(n)]

    m = int(input())
    input_queries = [input() for _ in range(m)]

    results = search_engine(documents=input_docs, queries=input_queries)
    for res in results:
        print(" ".join(map(str, res)))


@pytest.mark.parametrize(
    "documents, queries, expected",
    [
        (
            ["i love coffee", "coffee with milk and sugar", "free tea for everyone"],
            ["i like black coffee without milk", "everyone loves new year", "mary likes black coffee without milk"],
            [[1, 2], [3], [2, 1]],
        ),
        (
            [
                "buy flat in moscow",
                "rent flat in moscow",
                "sell flat in moscow",
                "want flat in moscow like crazy",
                "clean flat in moscow on weekends",
                "renovate flat in moscow",
            ],
            ["flat in moscow for crazy weekends"],
            [[4, 5, 1, 2, 3]],
        ),
        (
            ["i like dfs and bfs", "i like dfs dfs", "i like bfs with bfs and bfs"],
            ["dfs dfs dfs dfs bfs"],
            [[3, 1, 2]],
        ),
    ],
)
def test_search_engine(documents, queries, expected) -> None:
    assert search_engine(documents, queries) == expected


if __name__ == "__main__":
    pytest.main([__file__] + ["-vvv"])

# if __name__ == "__main__":
#     main()
