# Реализовать функцию find_last, принимающую упорядоченный по неубыванию список объектов и элемент.
# Функция должна найти последнее вхождение элемента в список, используя бинарный поиск и вернуть индекс вхождения (число).
# Если вхождения нет, вернуть None.

def find_last(array, elem):
    left = -1
    right = len(array)
    while left + 1 < right:
        middle = (left + right) // 2
        if elem < array[middle]:
            right = middle
        else:
            left = middle
    if array[right - 1] != elem:
        return None
    return right - 1
