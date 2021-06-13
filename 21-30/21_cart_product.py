# На вход подаются два итератора написать генераторную функцию, которая возвращает декартово произведение


def cart_product(iter1, iter2):
    for item1 in iter1:
        for item2 in iter2:
            yield item1, item2


if __name__ == '__main__':
    print(*cart_product('abc', '123'))

