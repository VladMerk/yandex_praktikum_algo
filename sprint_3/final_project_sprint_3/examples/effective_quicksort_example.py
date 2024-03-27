"""

"""

Array = [3, 7, 2, 8, 1, 6, 8, 9, 6, 9]


def partition(a, left, right):

    pivot = left + (right - left) // 2
    a[left], a[pivot] = a[pivot], a[left]  # swap
    pivot = left
    left += 1

    while right >= left:
        while left <= right and a[left] <= a[pivot]:
            left += 1
        while left <= right and a[right] > a[pivot]:
            right -= 1

        if left <= right:
            a[left], a[right] = a[right], a[left]  # swap
            left += 1
            right -= 1
        else:
            break

    a[pivot], a[right] = a[right], a[pivot]

    return right


def quicksort(array, left, right):
    if left >= right:
        return
    if right - left == 1:
        if array[right] < array[left]:
            array[right], array[left] = array[left], array[right]
            return

    pivot = partition(array, left, right)

    quicksort(array, left, pivot - 1)
    quicksort(array, pivot + 1, right)


def main():
    quicksort(Array, 0, len(Array) - 1)
    print(Array)


main()
