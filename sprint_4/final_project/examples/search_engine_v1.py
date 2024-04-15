import sys

import pytest

# from collections import defaultdict


def build_index(documents: list[str]) -> dict:
    index: dict = {}

    for doc_id, document in enumerate(documents, 1):
        words: list[str] = document.split()
        for word in words:
            index.setdefault(word, []).append(doc_id)

    return index


def search(index: dict, query: str) -> list[int]:
    query_words: set[str] = set(query.split())

    relevance: dict = {}
    for word in query_words:
        for doc_id in index.get(word, []):
            relevance[doc_id] = relevance.get(doc_id, 0) + 1

    return [result[0] for result in sorted(relevance.items(), key=lambda item: (-item[1], item[0]))[:5]]


def search_engine(documents: list[str], queries: list[str]) -> list[list[int]]:
    indx = build_index(documents)
    return [search(index=indx, query=query) for query in queries]


def main():
    n = int(input())
    input_docs = []
    while n > 0:
        input_docs.append(sys.stdin.readline().strip())
        n -= 1

    m = int(input())
    input_queries = []
    while m > 0:
        input_queries.append(sys.stdin.readline().strip())
        m -= 1

    results = search_engine(documents=input_docs, queries=input_queries)
    for res in results:
        print(" ".join([str(x) for x in res]))


def test():
    # documents = ["i love coffee", "coffee with milk and sugar", "free tea for everyone"]
    documents = ["i like dfs and bfs", "i like dfs dfs", "i like bfs with bfs and bfs"]

    index = build_index(documents=documents)
    print(index)
    # queries = ["i like black coffee without milk", "everyone loves new year", "mary likes black coffee without milk"]
    queries = ["dfs dfs dfs dfs bfs"]
    result = [search(index=index, query=query) for query in queries]
    print(result)


# def build_index(documents: list[str]) -> dict:
#     index = defaultdict(list)
#     for doc_id, document in enumerate(documents, 1):
#         words = set(document.split())
#         for word in words:
#             index[word].append(doc_id)
#     return index


# def search(index: dict, query: str) -> list[int]:
#     query_words = set(query.split())
#     relevance = defaultdict(int)
#     for word in query_words:
#         for doc_id in index.get(word, []):
#             relevance[doc_id] += 1
#     return [result[0] for result in nsmallest(5, relevance.items(), key=lambda item: (-item[1], item[0]))]


# def search_engine(documents: list[str], queries: list[str]) -> list[list[int]]:
#     indx = build_index(documents)
#     return [search(index=indx, query=query) for query in queries]


# def main():
#     n = int(input())
#     input_docs = [input() for _ in range(n)]

#     m = int(input())
#     input_queries = [input() for _ in range(m)]

#     results = search_engine(documents=input_docs, queries=input_queries)
#     for res in results:
#         print(" ".join(map(str, res)))


# if __name__ == "__main__":
#     main()


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
    test()
