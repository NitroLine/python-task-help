# Реализовать генераторную функцию cross, принимающую два итератора иd
# выдающую их декартово произведение по схеме (цифрами указан порядок выдачи элементов):
#         ```
#            A  B  C …  ..
#         a  1  3  6 10 ..
#         b  2  5  9 ..
#         c  4  8  ..
#            7  ..
#            ..

def cross(iter1, iter2):
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
        i = level - 1
        while j < level:
            try:
                a = get_item(i, mem1, iter1)
                b = get_item(j, mem2, iter2)
                j += 1
                i -= 1
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
    print(*cross(iter('abc'), iter('ABC')))

