# Модой называется значение в последовательности, встречающееся наиболее часто.
# Реализовать функцию mode, принимающую список произвольных объектов и возвращающую моду списка.
# Если мод несколько, вернуть список мод.

import collections


def mode(l):
    d = dict()
    for item in l:
        if isinstance(item, collections.Hashable):
            if item in d:
                d[item][0] += 1
            else:
                d[item] = [1, item]
        else:
            if str(item) in d:
                d[str(item)][0] += 1
            else:
                d[str(item)] = [1, item]
    ans = []
    ma = None
    for it in sorted(d.items(), key=lambda x: x[0], reverse=True):
        if ma is None:
            ma = it[0]
            ans.append(it[1])
        elif ma == it[0]:
            ans.append(it[1])
        else:
            break
    return ans



