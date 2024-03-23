import pytest


def conferences(lst: list, k: int) -> list:
    students = dict()
    for id in lst:
        students[id] = students.get(id, 0) + 1
    return [item[0] for item in sorted(students.items(), key=lambda x: x[1], reverse=True)][:k]


def read_input():
    n = int(input())
    ids = list(map(int, input().split()))
    k = int(input())

    return n, ids, k


def main():
    n, ids, k = read_input()
    print(*conferences(ids, k), sep=" ")


@pytest.mark.parametrize(
    "lst, k, expected",
    [
        ([1, 2, 3, 1, 2, 3, 4], 3, [1, 2, 3]),
        ([1, 1, 1, 2, 2, 3], 1, [1]),
        ([1, 1, 1, 2, 2, 3, 7, 5, 5], 3, [1, 2, 5]),
        ([10000], 1, [10000]),
        ([1], 2, [1])
    ],
)
def test_conf(lst, k, expected):
    assert conferences(lst, k) == expected


if __name__ == "__main__":
    pytest.main([__file__] + ["-vvv"])
