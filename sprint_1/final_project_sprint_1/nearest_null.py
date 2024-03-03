"""
Задача "Ближайший ноль".

Ссылка на посылку: https://contest.yandex.ru/contest/22450/run-report/108690070/
"""


def get_input() -> tuple[int, list]:
    n = int(input())
    houses = list(map(int, input().split()))

    return n, houses


def get_nearest_null(n: int, houses: list) -> list:
    distances = []
    distance_to_zero = n
    for i in range(n):
        if houses[i] == 0:
            distance_to_zero = 0
        else:
            distance_to_zero += 1
        distances.append(distance_to_zero)

    distance_to_zero = n
    for i in range(n - 1, -1, -1):
        if houses[i] == 0:
            distance_to_zero = 0
        else:
            distance_to_zero += 1
        distances[i] = min(distances[i], distance_to_zero)

    return distances


if __name__ == "__main__":
    n, houses = get_input()
    distances = get_nearest_null(n, houses)
    print(*distances)
