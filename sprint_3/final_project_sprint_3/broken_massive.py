import pytest


def _binary_search(nums: list, target: int, left: int, right: int) -> int:
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    if nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            return _binary_search(nums, target, left, mid - 1)
        else:
            return _binary_search(nums, target, mid + 1, right)
    else:
        if nums[mid] < target <= nums[right]:
            return _binary_search(nums, target, mid + 1, right)
        else:
            return _binary_search(nums, target, left, mid - 1)


def broken_search(nums: list, target: int) -> int:
    return _binary_search(nums, target, 0, len(nums) - 1)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 21) == 1


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
    # pytest.main([__file__] + ["-vvv"])
    test()
