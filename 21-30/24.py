﻿# Пусть дано натуральное число k. Обозначим S(k) сумму цифр числа k.
# Реализовать функцию, принимающую натуральное число k и возвращающую (S(...S(k)...)).
# S применяются для тех пор, пока не останется одна цифра.
# При реализации ЗАПРЕЩЕНО использовать циклы for, while а также if


def s(k):
    a = [9, 1, 2, 3, 4, 5, 6, 7, 8]
    return a[k % 9]
