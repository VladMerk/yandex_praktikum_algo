"""
Представьте себе онлайн-игру для поездки в метро: игрок нажимает на кнопку,
и на экране появляются три случайных числа.

Если все три числа оказываются одной чётности, игрок выигрывает.

Напишите программу, которая по трём числам определяет, выиграл игрок или нет.
"""

import pytest


def get_even_number(number: int) -> bool:
    return number % 2 == 0


def even_odd_numbers(a: int, b: int, c: int) -> str:
    if all([get_even_number(x) for x in (a, b, c)]):
        return "WIN"
    elif all([not get_even_number(x) for x in (a, b, c)]):
        return "WIN"
    else:
        return "FAIL"


@pytest.mark.parametrize(
    "a, b, c, expected",
    [
        (1, 2, -3, "FAIL"),
        (7, 11, 7, "WIN"),
        (6, -2, 0, "WIN"),
        (29, 19, -25, "WIN"),
        (703684863, 232269301, 765132875, "WIN"),
        (-687373597, 423392027, 259465703, "WIN"),
    ],
)
def test_even_odd_numbers(a, b, c, expected: str):
    assert even_odd_numbers(a, b, c) == expected
