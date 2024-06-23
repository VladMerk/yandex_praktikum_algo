"""
-- Принцип работы --
Алгоритм использует комбинацию бора (префиксного дерева) и динамического программирования.

1. Построение бора:
   - Каждое слово из словаря добавляется в бор.
   - Бор представлен списком словарей, где каждый словарь - узел дерева.
   - Терминальные узлы (концы слов) отмечаются в отдельном списке.

2. Проверка возможности разбиения:
   - Используется массив valid, где valid[i] означает, можно ли разбить подстроку до i-й позиции.
   - Для каждой позиции в строке:
     - Если позиция достижима, проверяем все возможные продолжения в боре.
     - Если находим слово, отмечаем соответствующую позицию как достижимую.
   - В конце проверяем, достижима ли последняя позиция строки.

-- Пространственная сложность --
O(N + M), где:
N - суммарная длина всех слов в словаре
M - длина входной строки

- Бор занимает O(N) памяти.
- Массив valid занимает O(M) памяти.

-- Временная сложность --
O(N + M^2), где:
N - суммарная длина всех слов в словаре
M - длина входной строки

- Построение бора занимает O(N) времени.
- Проверка разбиения в худшем случае может потребовать O(M^2) операций,
  так как для каждой позиции мы можем пройти до конца строки.

ID Посылки: https://contest.yandex.ru/contest/26133/run-report/115465606/
"""


def add_strings(trie: list[dict[str, int]], terminals: list[bool], strings: str) -> None:
    current_node: int = 0
    for char in strings:
        if char not in trie[current_node]:
            trie[current_node][char] = len(trie)
            trie.append({})
            terminals.append(False)
        current_node = trie[current_node][char]
    terminals[current_node] = True


def break_words(trie, terminals, strings):
    valid: list[bool] = [True] + [False] * len(strings)
    for pos in range(len(strings)):
        if not valid[pos]:
            continue
        current_node: int = 0
        for offset in range(len(strings) - pos):
            symbol: str = strings[pos + offset]
            if symbol not in trie[current_node]:
                break
            current_node = trie[current_node][symbol]
            if terminals[current_node]:
                valid[pos + offset + 1] = True
    return valid[-1]


def main():
    strings: str = input().strip()
    n = int(input())
    trie: list[dict[str, int]] = [{}]
    terminals: list[bool] = [False]

    for _ in range(n):
        add_strings(trie, terminals, input().strip())

    is_valid: bool = break_words(trie, terminals, strings)

    print("YES" if is_valid else "NO")


if __name__ == "__main__":
    main()
