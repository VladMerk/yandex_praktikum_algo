"""
Помогите Васе понять, будет ли фраза палиндромом. Учитываются только буквы и цифры,
заглавные и строчные буквы считаются одинаковыми.

Решение должно работать за O(N), где N — длина строки на входе.

Формат ввода
В единственной строке записана фраза или слово. Буквы могут быть только латинские.
Длина текста не превосходит 20000 символов.

Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания.

Формат вывода
Выведите «True», если фраза является палиндромом, и «False», если не является.
"""

import pytest


def is_palindrome(s: str) -> bool:
    s = s.lower()
    left_index = 0
    right_index = len(s) - 1
    wrong_symbols = [
        ",",
        ".",
        ":",
        " ",
        "_",
        "-",
        "@",
        "`",
        "~",
        "*",
        "!",
        ">",
        "'",
        "(",
        ")",
    ]
    while left_index < right_index:
        if s[left_index] in wrong_symbols:
            left_index += 1
            continue
        if s[right_index] in wrong_symbols:
            right_index -= 1
            continue
        if s[left_index] != s[right_index]:
            return False

        left_index += 1
        right_index -= 1

    return True


@pytest.mark.parametrize(
    "s,expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("zo", False),
        ("e.", True),
        ("12321!", True),
        ("-Luke, I'm your Father! -N00Oo! -oo00n -rehTAFruoymiekul", True),
        ("ThiS_String-is-@-PALIND0m3```~3m0DNILAP-()-si*!gnirts>>>siht", True),
    ],
)
def test_is_palindrome(s: str, expected: bool) -> None:
    assert is_palindrome(s) == expected
