n, m = map(int, input().split())

matrix: list[list[int]] = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    i, j = map(int, input().split())
    matrix[i-1][j-1] = 1

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()
