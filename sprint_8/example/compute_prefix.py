"""
Алгоритм Кнута-Морриса-Пратта (КМП)
"""


def compute_prefix(S: str) -> list[int]:
    n: int = len(S)
    pi: list[int] = [0] * n
    k: int = 0
    for i in range(1, n):
        while k > 0 and S[k] != S[i]:
            k = pi[k - 1]
        if S[k] == S[i]:
            k += 1
        pi[i] = k
    return pi


if __name__ == "__main__":
    assert compute_prefix('abracadabra') == list(map(int, '0 0 0 1 0 1 0 1 2 3 4'.split()))
    assert compute_prefix('aaaaa') == list(map(int, '0 1 2 3 4'.split()))
