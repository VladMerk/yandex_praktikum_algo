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


def factorize(n):
    i = 2
    primes = []
    while i * i <= n:
        while n % i == 0:
            primes.append(i)
            n = n // i
        i = i + 1
    if n > 1:
        primes.append(n)
    return primes


# Работающий алгоритм, но не эффективный при большом значении n
#
# def eratosthenes(n):
#     lp = [0] * (n + 1)
#     primes = []
#     for i in range(2, n + 1):
#         if lp[i] == 0:
#             lp[i] = i
#             primes.append(i)
#         for p in primes:
#             x = p * i
#             if (p > lp[i]) or (x > n):
#                 break
#             lp[x] = p
#     return primes, lp
#
#
# def factorize(n: int) -> list[int]:
#     primes: list = eratosthenes(n)[0]
#     lst_facts = []
#
#     for prime in primes:
#         if prime:
#             while n % prime == 0:
#                 lst_facts.append(prime)
#                 n //= prime
#         else:
#             continue
#
#     if n > 1:
#         lst_facts.append(n)
#
#     return lst_facts


@pytest.mark.parametrize(
    "n, expected",
    [
        (8, [2, 2, 2]),
        (13, [13]),
        (100, [2, 2, 5, 5]),
        (862399, [862399]),
        (917521579, [13, 70578583]),
        (802066951, [7, 4951, 23143]),
        (333826595, [5, 53, 281, 4483]),
    ],
)
def test_eratosthenes(n: int, expected: list[int]) -> None:
    assert factorize(n) == expected
