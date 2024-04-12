from collections import Counter


def build_index(documents: list[str]) -> dict:
    index: dict[str, list[tuple[int, int]]] = {}

    for idx, document in enumerate(documents, 1):
        words = Counter(document.split())
        for word in words:
            word_index: list[tuple[int, int]] | None = index.get(word)
            index_el: tuple[int, int] = (idx, words[word])

            if word_index is None:
                index[word] = [index_el]
            else:
                index[word].append(index_el)

    return index


def search(index: dict[str, tuple[int, int]], query: str) -> list[int]:
    relevance: dict[int, int] = {}

    for word in set(query.split()):
        index_item: tuple[int, int] | None = index.get(word)

        if index_item is None:
            continue

        for idx, count in index_item:  # type: ignore
            rel: int | None = relevance.get(idx)

            if rel is None:
                relevance[idx] = count
            else:
                relevance[idx] += count

    return [result[0] for result in sorted(relevance.items(), key=lambda item: (-item[1], item[0]))[:5]]


def search_engine(documents: list[str], queries: list[str]) -> list[list[int]]:
    indx: dict[str, tuple[int, int]] = build_index(documents)
    return [search(index=indx, query=query) for query in queries]


def main():
    n = int(input())
    input_docs = []
    while n > 0:
        input_docs.append(input())
        n -= 1

    m = int(input())
    input_queries = []
    while m > 0:
        input_queries.append(input())
        m -= 1

    results: list[list[int]] = search_engine(documents=input_docs, queries=input_queries)
    for res in results:
        print(" ".join([str(x) for x in res]))


if __name__ == "__main__":
    main()
