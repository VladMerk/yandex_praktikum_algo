import sys


def insertion_sort(array):
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j - 1]:
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert
        print("step {}, sorted {} elements: {}".format(i, i + 1, array))


insertion_sort([11, 2, 9, 7, 1])

digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6]  # длины слов «ноль», «один»,...


def is_first_card_weaker(card_1, card_2) -> bool:  # функция-компаратор
    return digit_lengths[card_1] < digit_lengths[card_2]


def is_first_card_weaker_by_len(card_1: int, card_2: int) -> bool:
    return card_1 < card_2


# воспользуемся уже знакомой сортировкой вставками
def insertion_sort_by_comparator(array, less) -> list[int]:
    for i in range(1, len(array)):
        item_to_insert = array[i]
        j = i
        # заменим сравнение item_to_insert < array[j-1] на компаратор less
        while j > 0 and less(item_to_insert, array[j - 1]):
            array[j] = array[j - 1]
            j -= 1
        array[j] = item_to_insert

    return array


cards = [3, 7, 9, 2, 3]
print("Sort by comparator: ")
sys.stdout.flush()
print(insertion_sort_by_comparator(cards, is_first_card_weaker))
print("Sort by comaparator 'len'")
print(insertion_sort_by_comparator(cards, is_first_card_weaker_by_len))
