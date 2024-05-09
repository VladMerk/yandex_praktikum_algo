m, n = map(int, input().split())

d: dict[int, list] = {key: [] for key in range(m)}

for _ in range(n):
    j, value = map(int, input().split())
    d[j-1].append(value)

for key, value in d.items():
    print(len(d[key]), *value)
