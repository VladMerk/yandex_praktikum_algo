"""
Задача: "Эффективная быстрая сортировка".

Тимофей решил организовать соревнование по спортивному программированию, чтобы найти талантливых стажёров.
Задачи подобраны, участники зарегистрированы, тесты написаны.
Осталось придумать, как в конце соревнования будет определяться победитель.

Каждый участник имеет уникальный логин. Когда соревнование закончится,
к нему будут привязаны два показателя: количество решённых задач Pi и размер штрафа Fi.
Штраф начисляется за неудачные попытки и время, затраченное на задачу.

Тимофей решил сортировать таблицу результатов следующим образом: при сравнении двух участников выше будет идти тот,
у которого решено больше задач. При равенстве числа решённых задач первым идёт участник с меньшим штрафом.
Если же и штрафы совпадают, то первым будет тот, у которого логин идёт раньше в алфавитном (лексикографическом) порядке.

Тимофей заказал толстовки для победителей и накануне поехал за ними в магазин.
В своё отсутствие он поручил вам реализовать алгоритм быстрой сортировки (англ. quick sort) для таблицы результатов.
Так как Тимофей любит спортивное программирование и не любит зря расходовать оперативную память,
то ваша реализация сортировки не может потреблять O(n) дополнительной памяти для промежуточных
данных (такая модификация быстрой сортировки называется "in-place").

Временная сложность: O(n*logn)
Пространственная сложность: O(1)

Идеи брал здесь: "https://stackoverflow.com/questions/17773516/in-place-quicksort-in-python".
Посылка: https://contest.yandex.ru/contest/23815/run-report/110701405/
"""


class User:
    """Класс описания стажера."""

    def __init__(self, name: str, tasks: int, penalty: int) -> None:
        self.name: str = name
        self.tasks: int = tasks
        self.penalty: int = penalty

    def __lt__(self, other: "User") -> bool:
        """
        Метод вызываемый при сравнении 2х объектов класса на "меньше".
        Нужен для сравнения при сортировке.
        """

        if self.tasks != other.tasks:
            return self.tasks < other.tasks
        elif self.penalty != other.penalty:
            return self.penalty > other.penalty
        else:
            return self.name > other.name

    def __repr__(self) -> str:
        """Метод для вывода объекта при печати в терминале."""
        return f"User(username={self.name}, tasks={self.tasks}, penalty={self.penalty})"


def quicksort(array: list, ilx: int, irx: int) -> None | int:
    """Функция быстрой сортировки.
    Так как стажеры сортируются с начала от большего количества решенных задач, то по сути необходимо
    написать функцию-аналог: sorted(list, reverse=True)

    Args:
    ilx - левая граница массива
    irx - правая граница массива

    Returns:
    Функция изменяет передаваемый массив, поэтому она ничего не возвращает.
    """

    # Если левый указатель больше чем правый, тогда выходим из рекурсии.
    if ilx >= irx:
        return -1

    left, right = ilx, irx
    pivot: User = array[ilx]

    # Найдем индексы, где слева объекты больше pivot, а с права меньше
    while left <= right:
        while array[left] > pivot:
            left += 1
        while array[right] < pivot:
            right -= 1

        # переносим объекты меньше pivot на право, а больше влево
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    quicksort(array, ilx, right)  # передаем в рекурсию границы массива, где элементы больше pivot
    quicksort(array, left, irx)  # где элементы меньше pivot


def get_input() -> list[User]:
    n = int(input())
    users = []
    while n > 0:
        name, tasks, penalty = input().split()
        users.append(User(name=name, tasks=int(tasks), penalty=int(penalty)))
        n -= 1
    return users


def main():
    users: list[User] = get_input()
    quicksort(users, ilx=0, irx=len(users) - 1)
    for user in users:
        print(user.name)


if __name__ == "__main__":
    main()
