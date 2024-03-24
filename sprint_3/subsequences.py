import pytest


def is_subsequences(s: str, t: str) -> bool:
    if len(s) > len(t):
        return False
    i = j = 0
    while j < len(t):
        if s[i] == t[j]:
            i += 1
            if i == len(s):
                return True
        j += 1

    return False


def read_input() -> tuple[str, str]:
    s = input()
    t = input()

    return s, t


@pytest.mark.parametrize(
    "s, t, expected",
    [
        ("abc", "ahbgdcu", True),
        ("abcp", "ahpc", False),
    ],
)
def test_is_subquences(s, t, expected) -> None:
    assert is_subsequences(s, t) == expected


if __name__ == "__main__":
    pytest.main([__file__] + ["-vvv"])
