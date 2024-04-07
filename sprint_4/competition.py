def determine_max_rounds_draw(rounds):
    def _hash(num):
        if num == "0":
            return -1
        return 1

    score = 0
    scores = {0: [-1]}
    max_score = 0
    for index, lap in enumerate(rounds.split()):
        score += _hash(lap)
        scores[score] = scores.get(score, []) + [index]
        if len(scores[score]) > 2:
            scores[score] = [scores[score][0], scores[score][-1]]
        if len(scores[score]) == 2:
            size = scores[score][-1] - scores[score][0]
            if max_score < size:
                max_score = size
    return max_score


def longest_draw_segment(n, results):
    max_length = 0
    sum_index_map = {0: -1}  # Инициализация хэш-таблицы с суммой 0 и индексом -1

    current_sum = 0
    for i in range(n):
        if results[i] == 0:
            current_sum += 1
        else:
            current_sum -= 1

        if current_sum in sum_index_map:
            max_length = max(max_length, i - sum_index_map[current_sum])
        else:
            sum_index_map[current_sum] = i

    return max_length


# Тестовый случай
n = 10
results = [0, 0, 1, 0, 1, 1, 1, 0, 0, 0]

# Вызов функции и вывод результата
print(longest_draw_segment(n, results))  # Должно вывести 8
