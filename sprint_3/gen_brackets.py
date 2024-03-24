"""
Рита по поручению Тимофея наводит порядок в правильных скобочных последовательностях (ПСП),
состоящих только из круглых скобок (). Для этого ей надо сгенерировать все ПСП длины 2n в алфавитном порядке
 —– алфавит состоит из ( и ) и открывающая скобка идёт раньше закрывающей.

Помогите Рите —– напишите программу, которая по заданному n выведет все ПСП в нужном порядке.

Рассмотрим второй пример. Надо вывести ПСП из четырёх символов. Таких всего две:

(())
()()

(()) идёт раньше ()(), так как первый символ у них одинаковый,
а на второй позиции у первой ПСП стоит (, который идёт раньше ).

Формат ввода
На вход функция принимает n — целое число от 0 до 10.

Формат вывода
Функция должна напечатать все возможные скобочные последовательности заданной длины в алфавитном (лексикографическом)
порядке.

Псевдокод из пачки:
func gen(balance, s) {
  if (s.length == <сколько нам надо>) {
    выводим
  }
  gen(balance+1, s+'(')
  gen(balance-1, s+')')
}
"""


def gen_brackets(n: int, prefix: str = "", prev: int | None = None, post: int | None = None):
    if prev is None:
        prev = n
    if post is None:
        post = n

    if prev == 0 and post == 0:
        return [prefix]

    result = []

    if prev > 0:
        result.extend(gen_brackets(n, prefix + "(", prev - 1, post))

    if post > prev:
        result.extend(gen_brackets(n, prefix + ")", prev, post - 1))

    return result


[print(arr) for arr in gen_brackets(3)]
