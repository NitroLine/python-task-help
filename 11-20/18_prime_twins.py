# Написать генератор возвращающий пары простых чисел-близнецов (отличающихся на 2)(30 баллов)

from math import sqrt


def is_prime(x):
    return all(x % i != 0 for i in range(2, int(sqrt(x) + 1)))


def is_twin(x):
    return is_prime(x) and (is_prime(x - 2) or is_prime(x + 2))


def generate_prime_twin():
    for x in range(4,100000000):
        if is_twin(x):
            yield x - 2, x + 2

