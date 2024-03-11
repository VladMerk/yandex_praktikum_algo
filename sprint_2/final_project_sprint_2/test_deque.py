import pytest
from deque import Deque, get_result_operation


def deque_resul(n, m, operations: list) -> list:
    deque = Deque(m)
    results = []
    i = 0

    while n != 0:
        results.append(get_result_operation(deque, operations[i]))
        n -= 1
        i += 1

    return results


@pytest.mark.parametrize(
    "n, m, operations, expected",
    [
        (
            7,
            10,
            ["push_front -855", "push_front 0", "pop_back", "pop_back", "push_back 844", "pop_back", "push_back 823"],
            [None, None, -855, 0, None, 844, None],
        ),
        (
            6,
            6,
            [
                "push_front -201",
                "push_back 959",
                "push_back 102",
                "push_front 20",
                "pop_front",
                "pop_back",
            ],
            [None, None, None, None, 20, 102],
        ),
        (4, 4, ["push_front 861", "push_front -819", "pop_back", "pop_back"], [None, None, 861, -819]),
    ],
)
def test_get_result_operation(n, m, operations, expected):
    assert expected == deque_resul(n, m, operations)
