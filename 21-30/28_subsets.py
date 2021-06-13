# Написать генераторную функцию, возвращающую подмножества множества.
# itertools.combinations использовать нельзя: (30 баллов)


def subsets(s):
    power_set = [[]]
    yield {}
    for x in s:
        for i in range(len(power_set)):
            tmp_list = power_set[i].copy()
            tmp_list.append(x)
            power_set.append(tmp_list)
            yield set(tmp_list)


if __name__ == '__main__':
    S = [1, 2, 3]
    for s in subsets(S):
        print(s)

