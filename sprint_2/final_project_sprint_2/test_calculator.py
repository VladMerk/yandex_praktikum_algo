import pytest
from calculator import postfix_calculator


@pytest.mark.parametrize(
    "expression, expected", [("2 1 + 3 *", 9), ("7 2 + 4 * 2 +", 38), ("3 4 +", 7), ("12 5 /", 2), ("10 2 4 * -", 2)]
)
def test_postfix_calculator(expression: str, expected: int) -> None:
    assert postfix_calculator(expression) == expected
