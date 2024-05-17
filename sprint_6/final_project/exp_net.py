import heapq
from typing import Literal

"""
-- ПРИНЦИП РАБОТЫ --
В данной задаче мы реализуем модифицированный алгоритм Прима для поиска максимального остовного дерева.
В отличие от традиционного алгоритма Прима, который ищет минимальное остовное дерево, мы используем max-heap
для выбора ребер с максимальным весом. Это позволяет найти максимальное остовное дерево, что и требуется по заданию.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Поскольку для поиска мы используем очередь с приоритетом (max-heap), временная сложность зависит от числа вершин и
ребер графа. Для каждого ребра выполняется операция добавления в heap, которая имеет сложность O(log E). Таким образом,
временная сложность алгоритма составляет O(E * log V), где V - количество вершин, E - количество ребер. В случае
плотного графа, где E стремится к V^2, временная сложность будет O(V^2 * log V).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Пространственная сложность зависит от хранения списка смежности и max-heap. Список смежности требует O(V + E) памяти,
где V - количество вершин, E - количество ребер. Max-heap также может содержать до E элементов. Таким образом, общая
пространственная сложность составляет O(V + E).

Посылка: https://contest.yandex.ru/contest/25070/run-report/114201914/
"""


class Graph:
    def __init__(self, n: int) -> None:
        self.n: int = n
        self.adj_list: list[list[tuple[int, int]]] = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int, weight: int):
        self.adj_list[u].append((weight, v))
        self.adj_list[v].append((weight, u))

    def find_mst(self) -> int | Literal["Oops! I did it again"]:
        if self.n == 1:
            return 0

        max_heap: list = []
        visited: list[bool] = [False] * self.n
        mst_weight = 0
        edges_in_mst = 0

        # Начинаем с вершины 0
        visited[0] = True
        for weight, neighbor in self.adj_list[0]:
            heapq.heappush(max_heap, (-weight, neighbor))

        while max_heap and edges_in_mst < self.n - 1:
            weight, vertex = heapq.heappop(max_heap)
            weight = -weight  # Обратно к положительным весам
            if not visited[vertex]:
                mst_weight += weight
                edges_in_mst += 1
                visited[vertex] = True
                for next_weight, neighbor in self.adj_list[vertex]:
                    if not visited[neighbor]:
                        heapq.heappush(max_heap, (-next_weight, neighbor))

        return mst_weight if edges_in_mst == self.n - 1 else "Oops! I did it again"


if __name__ == "__main__":
    n, m = map(int, input().split())

    graph = Graph(n)
    for _ in range(m):
        u, v, weight = map(int, input().split())
        graph.add_edge(u - 1, v - 1, weight)

    result = graph.find_mst()
    print(result)
