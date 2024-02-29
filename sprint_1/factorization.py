"""
Основная теорема арифметики говорит: любое число раскладывается на произведение простых множителей единственным образом,
 с точностью до их перестановки.

   Например:
Число 8 можно представить как 2 × 2 × 2.
Число 50 –— как 2 × 5 × 5 (или 5 × 5 × 2, или 5 × 2 × 5). Три варианта отличаются лишь порядком следования множителей.

Разложение числа на простые множители называется факторизацией числа.

Напишите программу, которая производит факторизацию переданного числа.
"""

import pytest
import pytest_timeout
#
# def eratosthenes_effective(n: int) -> list[int]:
#     """Алгоритм можно оптимизировать. Для каждого простого числа
#     p начнём отмечать числа, начиная с p^2,
#     как составные. Ведь все составные числа,
#     которые меньше него, будут уже рассмотрены.
#     """
#     numbers = list(range(n + 1))
#     numbers[0] = numbers[1] = False
#     for num in range(2, n):
#         if numbers[num]:
#             for j in range(num * num, n + 1, num):
#                 numbers[j] = False
#     return [num for num in numbers if num]


def eratosthenes(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp


def factorize(n: int) -> list[int]:
    primes: list = eratosthenes(n)[0]
    lst_facts = []

    for prime in primes:
        if prime:
            while n % prime == 0:
                lst_facts.append(prime)
                n //= prime
        else:
            continue

    if n > 1:
        lst_facts.append(n)

    return lst_facts


@pytest.mark.parametrize(
    "n, expected",
    [
        (8, [2, 2, 2]),
        (13, [13]),
        (100, [2, 2, 5, 5]),
        (862399, [862399]),
        (917521579, [13, 70578583]),
        (802066951, [7, 4951, 23143]),
    ],
)
def test_eratosthenes(n: int, expected: list[int]) -> None:
    assert factorize(n) == expected
