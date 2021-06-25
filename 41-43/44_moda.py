# Модой называется значение в последовательности, встречающееся наиболее часто.
# Реализовать функцию mode, принимающую список произвольных объектов и возвращающую моду списка.
# Если мод несколько, вернуть список мод.

import collections


def mode(l):
    d = dict()
    for item in l:
        if isinstance(item, collections.Hashable):
            if item in d:
                d[item] += 1
            else:
                d[item] = 1
        else:
            if str(item) in d:
                d[str(item)] += 1
            else:
                d[str(item)] = 1
