import pytest
from effective_quicksort import quicksort, User


@pytest.mark.parametrize(
    "array, expected",
    [
        (
            [
                ["alla", 4, 100],
                ["gena", 6, 1000],
                ["gosha", 2, 90],
                ["rita", 2, 90],
                ["timofey", 4, 80],
            ],
            [
                "gena",
                "timofey",
                "alla",
                "gosha",
                "rita",
            ],
        ),
        (
            [
                ["alla", 0, 0],
                ["gena", 0, 0],
                ["gosha", 0, 0],
                ["rita", 0, 0],
                ["timofey", 0, 0],
            ],
            [
                "alla",
                "gena",
                "gosha",
                "rita",
                "timofey",
            ],
        ),
    ],
)
def test_quicksort(array, expected):
    users = [User(item[0], item[1], item[2]) for item in array]
    quicksort(users, ilx=0, irx=len(array) - 1)
    print()
    for a, b in zip(users, expected):
        print(f"{a=}", f"{b=}")
        assert a.name == b


if __name__ == "__main__":
    pytest.main([__file__] + ["-vvvs"])
