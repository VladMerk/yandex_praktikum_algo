import pytest
from broken_massive import broken_search


@pytest.mark.parametrize(
    "arr, k, expected",
    [
        ([5, 1], 1, 1),
        ([19, 21, 100, 101, 1, 4, 5, 7, 12], 5, 6),
        ([3, 5, 6, 7, 9, 1, 2], 4, -1),
        ([19, 21, 100, 101, 1, 4, 5, 7, 12], 21, 1),
    ],
)
def test_broken_search(arr, k, expected):
    assert broken_search(arr, k) == expected


if __name__ == "__main__":
    pytest.main([__file__] + ["-vvv"])
