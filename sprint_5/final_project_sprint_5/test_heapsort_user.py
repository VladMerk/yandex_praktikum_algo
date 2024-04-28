import pytest
from heapsort import User


# Test comparison of User objects with various realistic values
@pytest.mark.parametrize(
    "user_a, user_b, expected",
    [
        # ID: Test different tasks
        (User("Alice", 5, 10), User("Bob", 3, 10), False),
        # ID: Test same tasks, different penalties
        (User("Alice", 5, 10), User("Bob", 5, 5), True),
        # ID: Test same tasks and penalties, different names
        (User("Alice", 5, 10), User("Charlie", 5, 10), False),
        # ID: Test all attributes same
        (User("Alice", 5, 10), User("Alice", 5, 10), False),
    ],
    ids=["different_tasks", "same_tasks_diff_penalties", "same_tasks_penalties_diff_names", "all_attributes_same"],
)
def test_user_comparison(user_a, user_b, expected):
    # Act
    result = user_a < user_b

    # Assert
    assert result == expected, f"Expected {user_a} < {user_b} to be {expected}"


# Test __repr__ method with various realistic values
@pytest.mark.parametrize(
    "user, expected_repr",
    [
        # ID: Test with a simple name
        (User("Alice", 5, 10), "Alice"),
        # ID: Test with a complex name
        (User("Bob Marley", 5, 10), "Bob Marley"),
    ],
    ids=["simple_name", "complex_name"],
)
def test_user_repr(user, expected_repr):
    # Act
    result = repr(user)

    # Assert
    assert result == expected_repr, f"Expected repr of {user} to be '{expected_repr}'"


if __name__ == "__main__":
    pytest.main([__file__] + ["-vvvs"])
