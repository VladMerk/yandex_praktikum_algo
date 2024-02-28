"""
Тимофей записал два числа в двоичной системе счисления и попросил Гошу вывести их сумму, также в двоичной системе.
 Встроенную в язык программирования возможность сложения двоичных чисел применять нельзя.
 Помогите Гоше решить задачу.

Решение должно работать за O(N), где N –— количество разрядов максимального числа на входе.

Формат ввода
Два числа в двоичной системе счисления, каждое на отдельной строке. Длина каждого числа не превосходит 10 000 символов.

Формат вывода
Одно число в двоичной системе счисления.
"""

import pytest


def get_binary_sum(num_1: str, num_2: str) -> str:
    max_len = max(len(num_1), len(num_2))
    num_1 = num_1.zfill(max_len)
    num_2 = num_2.zfill(max_len)

    result = ""
    swap = 0

    for i in range(max_len - 1, -1, -1):
        sum_ = int(num_1[i]) + int(num_2[i]) + swap
        result = str(sum_ % 2) + result
        swap = sum_ // 2

    if swap:
        result = "1" + result

    return result


@pytest.mark.parametrize("num_1, num_2, expected", [("1010", "1011", "10101"), ("1", "1", "10")])
def test_get_binary_sum(num_1: str, num_2: str, expected: str) -> None:
    assert get_binary_sum(num_1, num_2) == expected
