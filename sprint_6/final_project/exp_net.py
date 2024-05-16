from heapq import heappush


def add_vertex(v, graph, not_added, edges):
    not_added.remove(v)

    # Вершины представлены в виде tuple (w, v, u), очередь с приоритетом реализует min-heap-sort,
    # поэтому - веса отрицательные.
    for edge in [(-item[1], v, item[0]) for item in graph.get(v).items() if item[0] in not_added]:
        heappush(edges, edge)
