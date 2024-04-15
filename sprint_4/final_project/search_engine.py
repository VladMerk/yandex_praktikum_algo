"""
   --- Описание алгоритма:
В функции `build_index` формируется хэш-таблица состоящая из словаря, где
ключ - слово, а значение - список кортежей, где каждый кортеж содержит
id документа и количество вхождений слова в этот документ.
Для подсчета количества слов используется класс `collections.Counter`
из стандартной библиотеки Python.

В функции `search` производиться поиск слов и формируется список релеватных
документов по этому запросу. Запрос преобразуется в `set` что гарантирует
уникальность слов в запросе.

Функция `search_engine` собирает обе функции в одну. В нее передается список
документов и список запросов, а возращается список списков из номеров релеватных
документов для каждого запроса.


   --- Временная сложность:
для функции `build_index` сложность составляет O(n * m), где
  - n: количество переданных в функцию документов
  - m: количество слов в каждом документе

для функции `search` сложность составляет O(n * mlogm), где
  - n: количество уникальных слов в запросе
  - m: количество совпавших слов, по ним производиться сортировка


   --- Пространственная сложность:
для функции `build_index` сложность составляет O(n), где
  - n: количество уникальных слов во всех документах

для функции `search` O(n), где
  - n: количество уникальных слов в запросе
  (при создании set'a для хранения слов из запроса)


Посылка: https://contest.yandex.ru/contest/24414/run-report/111890010/
"""

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


def search(index: dict[str, list[tuple[int, int]]], query: str) -> list[int]:
    relevance: dict[int, int] = {}

    for word in set(query.split()):
        index_item: list[tuple[int, int]] | None = index.get(word)

        if index_item is None:
            continue

        for idx, count in index_item:
            rel: int | None = relevance.get(idx)

            if rel is None:
                relevance[idx] = count
            else:
                relevance[idx] += count

    return [result[0] for result in sorted(relevance.items(), key=lambda item: (-item[1], item[0]))[:5]]


def search_engine(documents: list[str], queries: list[str]) -> list[list[int]]:
    indx: dict[str, list[tuple[int, int]]] = build_index(documents)
    return [search(index=indx, query=query) for query in queries]


def main() -> None:
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
