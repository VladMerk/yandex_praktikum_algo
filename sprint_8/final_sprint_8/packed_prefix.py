"""
-- Принцип работы --
Решение основано на рекурсивном подходе к распаковке строк и последующем поиске наибольшего общего префикса.

1. Распаковка строк (unpack):
Функция проходит по символам строки слева направо. При встрече цифры, она накапливается для определения количества
повторений. При встрече '[', функция рекурсивно вызывает себя для обработки содержимого скобок.
Результат рекурсивного вызова повторяется нужное количество раз. Обычные символы добавляются к результату напрямую.
При встрече ']', функция возвращает текущий результат и индекс.

2. Поиск наибольшего общего префикса (longest_common_prefix):
Находится самая короткая строка среди распакованных. Происходит посимвольное сравнение всех строк.
Возвращается префикс до первого несовпадения.

-- Пространственная сложность --
Пространственная сложность равна O(N), где N - суммарная длина всех распакованных строк.

- Каждая распакованная строка хранится в памяти.
- Рекурсивные вызовы создают стек вызовов, глубина которого пропорциональна уровню вложенности скобок.
- В худшем случае (много вложенных скобок) стек может достигать O(M), где M - длина самой длинной запакованной строки.

-- Временная сложность --
O(N), где N - суммарная длина всех распакованных строк.

- Распаковка каждой строки требует O(Ni) операций, где Ni - длина i-й распакованной строки.
- Поиск наибольшего общего префикса выполняется за O(N) в худшем случае.
- Суммарно получаем O(N1 + N2 + ... + Nk) = O(N), где k - количество строк.

Важно отметить, что хотя алгоритм линеен относительно длины распакованных строк,
сама длина распакованной строки может экспоненциально превышать длину запакованной строки
(например, для строки вида "2[2[2[a]]]").

ID Посылки: https://contest.yandex.ru/contest/26133/run-report/115463661/
"""


def unpack(s: str, i: int = 0) -> tuple[str, int]:
    result: list = []
    num: int = 0
    while i < len(s):
        if s[i].isdigit():
            num = num * 10 + int(s[i])
        elif s[i] == "[":
            substring, end = unpack(s, i + 1)
            result.extend(substring * num)
            i: int = end
            num = 0
        elif s[i] == "]":
            return "".join(result), i
        else:
            result.append(s[i])
        i += 1
    return "".join(result), i


def longest_common_prefix(strings: list[str]) -> str:
    if not strings:
        return ""
    shortest: str = min(strings, key=len)
    for i, char in enumerate(shortest):
        if any(string[i] != char for string in strings):
            return shortest[:i]
    return shortest


def main():
    n: int = int(input())
    packed_strings: list[str] = [input() for _ in range(n)]

    unpacked_strings: list[str] = [unpack(s)[0] for s in packed_strings]

    result: str = longest_common_prefix(unpacked_strings)

    print(result)


if __name__ == "__main__":
    main()
