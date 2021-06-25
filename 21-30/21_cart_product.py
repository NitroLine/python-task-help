# На вход подаются два итератора написать генераторную функцию, которая возвращает декартово произведение
#
#     a b c ..
#   A 1 4 9 ..
#   B 2 3 8 ..
#   C 5 6 7 ..
#   .. .. ..


def cart_product(iter1, iter2):
    mem1 = []
    mem2 = []
    i = 0
    j = 0
    level = 1
    try:
        a = get_item(i, mem1, iter1)
        b = get_item(j, mem2, iter2)
    except StopIteration:
        return
    yield a, b
    while True:
        level += 1
        j = 0
        i = level
        while j < level:
            try:
                a = get_item(i, mem1, iter1)
                b = get_item(j, mem2, iter2)
                j += 1
            except StopIteration:
                return
            yield a, b
        j -= 1
        while i > 0:
            i -= 1
            try:
                a = get_item(i, mem1, iter1)
                b = get_item(j, mem2, iter2)
            except StopIteration:
                return
            yield a, b


def get_item(ind, mem, iterator):
    if len(mem) > ind:
        return mem[ind]
    next_item = next(iterator)
    mem.append(next_item)
    return next_item


if __name__ == '__main__':
    print(*cart_product(iter('abc'), iter('123')))

