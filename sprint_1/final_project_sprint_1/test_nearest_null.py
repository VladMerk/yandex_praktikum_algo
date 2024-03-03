import pytest

from nearest_null import get_nearest_null


@pytest.mark.parametrize(
    "n, houses, expected", [(5, [0, 1, 4, 9, 0], [0, 1, 2, 1, 0]), (6, [0, 7, 9, 4, 8, 20], [0, 1, 2, 3, 4, 5])]
)
def test_get_nearest_null(n, houses, expected):
    assert expected == get_nearest_null(n, houses)
