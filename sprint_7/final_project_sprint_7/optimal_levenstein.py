"""
-- ПРИНЦИП РАБОТЫ --
В этой задаче вычисляется матрица расстояний по Левенштейну для двух строк - 's' и 't'.

Инициализируем масссив 'dp' размером len(s) x len(t), где
    dp[i][j] - минимальное количество операций, необходимых для преобразования
символов строки s в строку t.

Заполняем первую строку и первый столбец массива от нуля до длины строки,
что соответствует последовательным удалениям и вставкам символов.

Проходим по массиву и заполняем его:
 - если символы совпадают, тогда берем предыдущее значение из диагонали матрицы.
 - если нет, тогда берем минимальное значение из трех предыдущих значений:
 строки, столбца или диагонали и добавляем 1.
Таким образом происходит подсчет количества изменений одной строки в другую.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Так как у нас на входе принимается 2 массива строк величиной 'M' и 'N', то
временная сложность составляет O(N*M).

-- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
В этом варианте решения мы храним 2 массива - текущую и предыдущие строки,
поэтому пространственная сложность: O(M) + O(N) = O(n).

Посылка: https://contest.yandex.ru/contest/25597/run-report/115012899/
"""


def optimal_levenstein(s: str, t: str) -> int:
    m, n = len(s), len(t)

    prev_row: list[int] = list(range(n + 1))
    curr_row: list[int] = [0] * (n + 1)

    for i in range(1, m + 1):
        curr_row[0] = i
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                curr_row[j] = prev_row[j - 1]
            else:
                curr_row[j] = 1 + min(prev_row[j], curr_row[j - 1], prev_row[j - 1])
        prev_row, curr_row = curr_row, prev_row

    return prev_row[n]


def main():
    s: str = input().strip()
    t: str = input().strip()
    print(optimal_levenstein(s, t))


if __name__ == "__main__":
    main()