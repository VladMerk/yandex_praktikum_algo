
def effective_solution(A, x):
    history = set()
    n: int = len(x)
    x.sort()
    triples = set()
    for i in range(n):
        for j in range(i + 1, n):
            target: int = A - x[i] - x[j]
            if target in history:
                # Заметим, что тут тройка уже отсортирована за счёт предварительной
                # сортировки всего массива.
                triples.add((target, x[i], x[j]))
        history.add(x[i])
    return triples
