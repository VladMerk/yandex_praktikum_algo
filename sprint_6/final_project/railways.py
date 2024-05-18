"""
-- ПРИНЦИП РАБОТЫ --
Алгоритм следующий: если дорога типа 'B', то добавляем путь как есть, если типа 'R', то инвертируем путь. После этого
вся задача сводится к нахождению цикла в графе.

Поиску цикла в графе был посвящен отдельный пункт в теории к спринту: "DFS. Поиск цикла и времена входа-выхода".

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Нам дано количество городов - n и карта смежности. Из каждого города в каждый другой город существует маршрут.
Исходя из этой терминологии, сложность алгоритма O(n^2)

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
Дополнительная память используется для хранения графа O(n^2) в худшем случае.

Без учета памяти под граф - для хранения списка вершин, посещенных вершин, стека и вершин,
которые в процессе обработки O(n).

Посылка: https://contest.yandex.ru/contest/25070/run-report/114213361/

"""


class Graph:
    def __init__(self, n: int):
        self.n: int = n
        self.graph: list[list[int]] = [[] for _ in range(n)]
        self.visited: list[bool] = [False] * n
        self.on_stack: list[bool] = [False] * n

    def add_edge(self, u: int, v: int, road_type: str) -> None:
        if road_type == "R":
            self.graph[u].append(v)
        else:
            self.graph[v].append(u)

    def dfs(self, v: int) -> bool:
        stack: list[int] = [v]

        while stack:
            s: int = stack[-1]

            if not self.visited[s]:
                self.visited[s] = True
                self.on_stack[s] = True
            else:
                self.on_stack[s] = False
                stack.pop()
                continue

            for neighbor in self.graph[s]:
                if not self.visited[neighbor]:
                    stack.append(neighbor)
                elif self.on_stack[neighbor]:
                    return True
        return False

    def has_cycle(self) -> bool:
        return any(not self.visited[v] and self.dfs(v) for v in range(self.n))


def is_optimal_map(n: int, roads: list[str]) -> str:
    graph = Graph(n)

    for i in range(n - 1):
        for j, symbol in enumerate(roads[i]):
            graph.add_edge(i, i + j + 1, symbol)

    return "NO" if graph.has_cycle() else "YES"


if __name__ == "__main__":
    n = int(input())
    roads: list[str] = [input().strip() for _ in range(n - 1)]
    print(is_optimal_map(n, roads))
