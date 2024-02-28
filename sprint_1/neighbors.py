"""
Дана матрица. Нужно написать функцию, которая для элемента возвращает всех его соседей.
Соседним считается элемент, находящийся от текущего на одну ячейку влево, вправо, вверх или вниз.
Диагональные элементы соседними не считаются.

A = [[1, 2, 3],
     [0, 2, 6],
     [7, 4, 1],
     [2, 7, 0]]

Например, в матрице A соседними элементами для (0, 0) будут 2 и 0. А для (2, 1) –— 1, 2, 7, 7.
"""

import pytest


def get_neighbors(n: int, m: int, matrix: list[list[int]], x: int, y: int) -> list:
    neighbors = []
    if x > 0:
        neighbors.append(matrix[x - 1][y])
    if x < n - 1:
        neighbors.append(matrix[x + 1][y])
    if y > 0:
        neighbors.append(matrix[x][y - 1])
    if y < m - 1:
        neighbors.append(matrix[x][y + 1])

    return neighbors


@pytest.mark.parametrize(
    "n, m, matrix, x, y, expected",
    [
        (4, 3, [[1, 2, 3], [0, 2, 6], [7, 4, 1], [2, 7, 0]], 3, 0, [7, 7]),
        (4, 3, [[1, 2, 3], [0, 2, 6], [7, 4, 1], [2, 7, 0]], 0, 0, [0, 2]),
        (2, 1, [[1], [9]], 0, 0, [9]),
    ],
)
def test_get_neighbors(
    n: int, m: int, matrix: list[list[int]], x: int, y: int, expected: list
):
    assert get_neighbors(n, m, matrix, x, y) == expected
