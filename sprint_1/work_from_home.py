"""
Вася реализовал функцию, которая переводит целое число из десятичной системы в двоичную.
Но, кажется, она получилась не очень оптимальной.

Попробуйте написать более эффективную программу.

Не используйте встроенные средства языка по переводу чисел в бинарное представление.

Формат ввода
На вход подаётся целое число в диапазоне от 0 до 10000.

Формат вывода.
Выведите двоичное представление этого числа.
"""

import pytest


def get_binary(number: int) -> str:
    if number == 0:
        return "0"
    result = []
    while number > 0:
        result.append(number % 2)
        number = number // 2

    return "".join(map(str, result[::-1]))


@pytest.mark.parametrize("number,expected", [(5, "101"), (14, "1110"), (0, "0")])
def test_get_binary(number: int, expected: str) -> None:
    assert get_binary(number) == expected
