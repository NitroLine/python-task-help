# Реализовать генераторную функцию, принимающую итератор произвольных объектов и возвращающую их без повторений.
# Порядок следования объектов должен сохраниться.


def distinct(iter):
    used = set()
    for item in iter:
        if item not in used:
            used.add(item)
            yield item

