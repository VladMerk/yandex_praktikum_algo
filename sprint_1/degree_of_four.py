"""
Напишите программу, которая определяет, будет ли положительное целое число степенью четвёрки.

Подсказка: степенью четвёрки будут все числа вида 4n, где n – целое неотрицательное число.

Формат ввода
На вход подаётся целое число в диапазоне от 1 до 10000.

Формат вывода
Выведите «True», если число является степенью четырёх, «False» –— в обратном случае.
"""

import pytest

# Менее эффективный алгоритм
#
# def degree_of_four(n: int) -> bool:
#     i = 0
#     result = []
#     while 4**i <= n:
#         result.append(4**i)
#         i += 1
#
#     return n in result


def degree_of_four(n: int) -> bool:
    i = 0
    result = 0
    while 4**i <= n:
        result = 4**i
        i += 1

    return n == result


@pytest.mark.parametrize("n, expected", [(15, False), (16, True), (4, True), (1024, True)])
def test_degree_of_four(n: int, expected: bool) -> None:
    assert degree_of_four(n) == expected
