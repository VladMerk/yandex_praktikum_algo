"""
Задача "Ловкость рук"
Посылка: https://contest.yandex.ru/contest/22450/run-report/108937357/
"""


def get_input():
    k = int(input())
    field = ""
    for _ in range(4):
        field += input().strip()
    return k, field


def sleight_of_hand(k: int, field: str) -> int:
    result = 0
    for i in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        if i in field:
            value = field.count(i)
            if value <= k * 2:
                result += 1

    return result


if __name__ == "__main__":

    k_value, field_value = get_input()
    print(sleight_of_hand(k_value, field_value))
