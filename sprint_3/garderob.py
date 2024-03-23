import pytest


def garderob(n: int, lst: list[int]) -> list[int]:
    things = [0] * 3
    for item in lst:
        things[item] += 1

    index = 0
    for value in range(3):
        for _ in range(things[value]):
            lst[index] = value
            index += 1
    return lst


def garderob_with_key(n: int, lst: list[int]) -> list[int]:
    things = [0, 1, 2]
    return sorted(lst, key=lambda x: things.index(x))


def read_input():
    n = int(input())
    lst = list(map(int, input().split()))

    return n, lst


def main():
    n, lst = read_input()
    print(*garderob(n, lst), sep=" ")


@pytest.mark.parametrize(
    "n, lst, expected",
    [
        (7, [0, 2, 1, 2, 0, 0, 1], [0, 0, 0, 1, 1, 2, 2]),
        (5, [2, 1, 2, 0, 1], [0, 1, 1, 2, 2]),
        (6, [2, 1, 1, 2, 0, 2], [0, 1, 1, 2, 2, 2]),
    ],
)
def test_garderob(n: int, lst: list, expected: list):
    assert garderob(n, lst) == expected
    assert garderob_with_key(n, lst) == expected


if __name__ == "__main__":
    pytest.main([__file__] + ["-vvv"])
