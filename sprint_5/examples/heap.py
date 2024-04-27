def sift_up(heap, index):
    if index == 1:
        return

    parent_index = index // 2
    if heap[index] > heap[parent_index]:
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        sift_up(heap, parent_index)


def heap_add(heap, key):
    heap.append(key)
    index = len(heap) - 1
    sift_up(heap, index)


def sift_down(heap, index):
    heap_max_index = len(heap) - 1
    left = index * 2
    right = index * 2 + 1

    # нет дочерних узлов
    if left > heap_max_index:
        return

    # проверяем, что есть оба дочерних узла
    if right <= heap_max_index and heap[right] > heap[left]:
        index_largest = right
    else:
        index_largest = left
    # отправляем максимум на вершину кучи и рекурсивно завпускаем просеивание в ребенке
    if heap[index_largest] > heap[index]:
        heap[index_largest], heap[index] = heap[index], heap[index_largest]
        sift_down(heap, index_largest)


def pop_max(heap):
    result = heap[1]
    heap[1] = heap[len(heap) - 1]
    heap.pop()
    sift_down(heap, 1)
    return result
