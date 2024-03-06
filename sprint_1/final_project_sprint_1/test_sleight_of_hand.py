import pytest

from sleight_of_hand import sleight_of_hand


@pytest.mark.parametrize(
    "k, field, expected",
    [
        (3, "12312..22..22..2", 2),
        (4, "1111999911119911", 1),
        (4, ["1111111111111111"], 0),
    ],
)
def test_sleight_of_hand(k: int, field: str, expected: int) -> None:
    assert sleight_of_hand(k, field) == expected
