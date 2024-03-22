import pytest


def get_biggest(lst: list) -> int:
    if len(lst) == 0:
        return -1
    max_len = max(map(len, [str(x) for x in lst]))
    sorted_lst = sorted(lst, key=lambda x: str(x) * max_len, reverse=True)
    return int("".join(map(str, sorted_lst)))


@pytest.mark.parametrize(
    "lst,expected",
    [
        ([3, 2, 1], 321),
        ([61, 228, 9, 3, 11], 961322811),
        ([], -1),
        ([7, 71, 72], 77271),
        ([15, 56, 2], 56215),
        ([1, 783, 2], 78321),
    ],
)
def test_get_biggest(lst, expected):
    assert get_biggest(lst) == expected


if __name__ == "__main__":
    pytest.main([__file__] + ["-ra", "-vvv"])
