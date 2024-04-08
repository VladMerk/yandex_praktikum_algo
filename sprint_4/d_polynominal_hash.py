import pytest


def poly_hash(a: int, m: int, s: str) -> int:
    if s == '':
        return 0
    index = 0
    result = 0
    size = len(s) - 1
    while index < size:
        result = (((result + ord(s[index])) % m) * a) % m
        index += 1
    return (result + ord(s[index])) % m


def main():
    a = int(input())
    m = int(input())
    s = input()
    print(poly_hash(a, m, s))


@pytest.mark.parametrize(
    "a, m, s, expected",
    [
        (123, 100003, "a", 97),
        (123, 100003, "hash", 6080),
        (123, 100003, "HaSH", 56156),
    ],
)
def test_poly_hash(a, m, s, expected) -> None:
    assert poly_hash(a, m, s) == expected


if __name__ == "__main__":
    pytest.main([__file__] + ["-vvv"])
