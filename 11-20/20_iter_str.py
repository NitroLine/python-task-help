#  Функция, принимающая итератор строк, которая возвращает только те строки, которые отсортированы лексикографически(30)


def get_sorted_strings(iter):
    for string in iter:
        if list(string) == sorted(string):
            yield string


if __name__ == '__main__':
    it = iter(['abc', 'dd', 'ada'])
    print(*get_sorted_strings(it))