"""
Задача "Поиск в сломанном массиве".

Алла ошиблась при копировании из одной структуры данных в другую.
Она хранила массив чисел в кольцевом буфере. Массив был отсортирован по возрастанию,
и в нём можно было найти элемент за логарифмическое время.
Алла скопировала данные из кольцевого буфера в обычный массив,
но сдвинула данные исходной отсортированной последовательности (при этом массив все равно мог остаться отсортированным).

Тем не менее, нужно обеспечить возможность находить в нем элемент за O(logn).

Можно предполагать, что в массиве только уникальные элементы.

Временная сложность: O(logn)
Пространственная сложность: O(1)

Посылка: https://contest.yandex.ru/contest/23815/run-report/110415655/
"""


def _binary_search(nums: list, target: int, left: int, right: int) -> int:
    """
    Функция бинарного поиска в массиве.

    Args:
    nums: list - массив, в котором производиться поиск
    target: int - искомое число
    left: int - левая граница поиска
    right: int - права граница поиска

    Returns:
    Функция возращает индекс, по которому находится искомое число
    или -1, если число не найдено.
    """

    # если левый указатель больше, чем правый - выходим из рекурсии
    if left > right:
        return -1

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    # Существует 4 варианта расположения искомого числа
    if nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            # target находится в первой четверти массива
            return _binary_search(nums, target, left, mid - 1)
        else:
            # если во второй
            return _binary_search(nums, target, mid + 1, right)
    else:
        if nums[mid] < target <= nums[right]:
            # в третьей
            return _binary_search(nums, target, mid + 1, right)
        else:
            # в четвертой
            return _binary_search(nums, target, left, mid - 1)


def broken_search(nums: list, target: int) -> int:
    return _binary_search(nums, target, 0, len(nums) - 1)


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 21) == 1


if __name__ == "__main__":
    test()
