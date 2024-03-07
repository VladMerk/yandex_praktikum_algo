"""
Задача "Ловкость рук"
https://contest.yandex.ru/contest/22450/run-report/109043233/
"""

from collections import Counter


def get_input():
    k = int(input())
    field = ""
    for _ in range(4):
        field += input().strip()
    return k, field


def sleight_of_hand(k: int, field: str) -> int:
    result = 0
    dfield = Counter(field)

    for key, value in dfield.items():
        if key != "." and value <= k * 2:
            result += 1

    return result


def main():
    k_value, field_value = get_input()
    print(sleight_of_hand(k_value, field_value))


if __name__ == "__main__":
    main()
