import pytest


def binary_search(arr: list[int], x: int, left: int, right: int) -> int:
    if right <= left:
        return -1

    mid = (left + right) // 2

    if arr[mid] >= x > arr[mid-1] or mid == 0:
        return mid + 1
    elif arr[mid] >= x:
        return binary_search(arr, x, left, mid)
    else:
        return binary_search(arr, x, mid+1, right)


def two_bikes(arr, x):
    left: int = 0
    right: int = len(arr)
    mid = (left + right) // 2

    return binary_search(arr, x, left, mid), binary_search(arr, 2 * x, left, right)


def read_input():
    n = int(input())
    days = list(map(int, input().split()))
    price = int(input())

    return n, days, price


def main():
    n, days, price = read_input()
    print(*two_bikes(days, price), sep=" ")


@pytest.mark.parametrize(
    "lst, x, expected",
    [
        ([1, 2, 4, 4, 6, 8], 3, (3, 5)),
        ([1, 2, 4, 4, 4, 4], 3, (3, -1)),
        ([1, 2, 4, 4, 4, 4], 10, (-1, -1)),
        ([1, 2, 4, 4, 4, 4], 1, (1, 2)),
    ],
)
def test_two_bikes(lst, x, expected):
    assert two_bikes(lst, x) == expected, f"{lst=}, {x=}"


if __name__ == "__main__":
    pytest.main([__file__] + ["-vvv"])
    # two_bikes([1, 2, 4, 4, 4, 4], 3)
    # main()
