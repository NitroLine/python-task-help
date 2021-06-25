# Написать генераторную функцию, которая возвращает все перестановки данного списка. (без itertools.permutations)


def permutations(array):
    yield from solve(array, 0)

def solve(array, position):
    if position == len(array) - 1:
        yield array
    else:
        for i in range(position, len(array)):
            array[i], array[position] = array[position], array[i]
            yield from solve(array, position + 1)
            array[i], array[position] = array[position], array[i]


if __name__ == '__main__':
    for i, perm in enumerate(permutations([1, 2, 3, 4])):
        print(i, perm)

