from typing import Literal

import pytest


def compare(s: str, t: str) -> Literal["YES", "NO"]:
    if len(s) != len(t):
        return "NO"

    s_to_t: dict[str, str] = {}
    t_to_s: dict[str, str] = {}

    for char_s, char_t in zip(s, t):
        if char_s not in s_to_t and char_t not in t_to_s:
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s
        elif s_to_t.get(char_s) != char_t or t_to_s.get(char_t) != char_s:
            return "NO"

    return "YES"


def main():
    s = input()
    t = input()
    print(compare(s, t))


@pytest.mark.parametrize(
    "s_str, t_str, expected",
    [
        ("mxyskaoghi", "qodfrgmslc", "YES"),
        ("agg", "xdd", "YES"),
        ("agg", "xda", "NO"),
        ("abacaba", "abacabac", "NO"),
        ("aba", "xxx", "NO"),
    ],
)
def test_compare(s_str, t_str, expected):
    assert compare(s=s_str, t=t_str) == expected


if __name__ == "__main__":
    pytest.main([__file__] + ["-vvv"])
