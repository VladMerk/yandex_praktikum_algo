"""
Вот какую задачу Тимофей предложил на собеседовании одному из кандидатов.
Если вы с ней ещё не сталкивались, то наверняка столкнётесь –— она довольно популярная.

Дана скобочная последовательность. Нужно определить, правильная ли она.

Будем придерживаться такого определения:

- пустая строка —– правильная скобочная последовательность;
- правильная скобочная последовательность, взятая в скобки одного типа, –— правильная скобочная последовательность;
- правильная скобочная последовательность с приписанной слева или
справа правильной скобочной последовательностью —– тоже правильная.

На вход подаётся последовательность из скобок трёх видов: [], (), {}.
Напишите функцию is_correct_bracket_seq, которая принимает на вход скобочную последовательность и возвращает True,
если последовательность правильная, а иначе False.

Формат ввода
На вход подаётся одна строка, содержащая скобочную последовательность. Скобки записаны подряд, без пробелов.

Формат вывода
Выведите «True» или «False».
"""

import pytest


def is_correct_bracket_seq(brackets: str) -> bool:
    if brackets == "":
        return True
    stack = []
    correct_brackets = {"{": "}", "[": "]", "(": ")"}
    for bracket in brackets:
        if bracket in correct_brackets.keys():
            stack.append(bracket)
        elif bracket in correct_brackets.values() and len(stack) == 0:
            return False
        else:
            if correct_brackets[stack.pop()] != bracket:
                return False

    if len(stack) != 0:
        return False

    return True


@pytest.mark.parametrize(
    "brackets,expected",
    [
        ("{[()]}", True),
        ("()", True),
        ("{([)]}", False),
        ("((())", False),
        ("]([(([((({))}])])([({})]}(]))](][}{{", False),
        (")(", False),
    ],
)
def test_is_correct_bracket_seq(brackets: str, expected: bool) -> None:
    assert is_correct_bracket_seq(brackets) == expected
