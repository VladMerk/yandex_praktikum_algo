from heapq import heappush, heappop


def add_vertex(v, graph, not_added, edges):
    not_added.remove(v)

    # Вершины представлены в виде tuple (w, v, u), очередь с приоритетом реализует min-heap-sort,
    # поэтому - веса отрицательные.
    for edge in [(-item[1], v, item[0]) for item in graph.get(v).items() if item[0] in not_added]:
        heappush(edges, edge)


def find_mst(graph, edges, mst):
    not_added = {v for v in range(1, len(graph) + 1)}

    start = 1
    add_vertex(start, graph, not_added, edges)

    while not_added and edges:
        e = heappop(edges)

        if e[2] in not_added:
            mst += -e[0]
            add_vertex(e[2], graph, not_added, edges)

    if not_added:
        raise ValueError('Oops! I did it again')

    return mst
