# 10. Написать функцию которая принимает на вход число и возвращает для него значение функции Эйлера (30 баллов)

from math import gcd
from utilities.tests_help import make_tests


def calculate_euler_func(n: int) -> int:
    k = 0
    for i in range(1, n + 1):
        k += 1 if gcd(i, n) == 1 else 0
    return k


if __name__ == "__main__":
    tests = [(1, 1), (2, 1), (5, 4), (6, 2), (66, 20)]
    make_tests(calculate_euler_func, tests)

