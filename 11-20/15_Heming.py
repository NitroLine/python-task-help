#  Написать, функцию, которая принимает два итератора и возвращает расстояние Хэминга между этими итераторами.

def hamming_distance(iter1, iter2):
    distance = 0
    while True:
        elem1 = next(iter1, None)
        elem2 = next(iter2, None)
        if elem1 is None and elem2 is None:
            break
        elif elem1 is None or elem2 is None:
            raise ValueError('У итераторов должна быть одинаковая длина!')
        if elem1 != elem2:
            distance += 1
    return distance


if __name__ == '__main__':
    s1 = iter('bda')
    s2 = iter('abd')
    print(hamming_distance(s1, s2))
