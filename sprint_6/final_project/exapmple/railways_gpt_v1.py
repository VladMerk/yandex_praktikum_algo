from collections import defaultdict, deque


def is_optimal_map(n, roads):
    graph_R = defaultdict(list)
    graph_B = defaultdict(list)

    for i in range(n - 1):
        for j, road in enumerate(roads[i]):
            if road == "R":
                graph_R[i + 1].append(i + j + 2)
            else:
                graph_B[i + 1].append(i + j + 2)

    def bfs(graph):
        reachable: list[bool] = [False] * (n + 1)
        queue = deque([1])
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if not reachable[neighbor]:
                    reachable[neighbor] = True
                    queue.append(neighbor)
        return reachable

    reachable_R = bfs(graph_R)
    reachable_B = bfs(graph_B)

    for city in range(1, n + 1):
        if reachable_R[city] and reachable_B[city]:
            return "NO"

    return "YES"


# Чтение ввода
n = int(input())
roads = [input().strip() for _ in range(n - 1)]

# Проверка и вывод результата
print(is_optimal_map(n, roads))
