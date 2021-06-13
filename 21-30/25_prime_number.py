# Реализовать функцию принимающую натуральное число и возвращающую количество простых множителей в разложении числа.
# Если передано не число выбросить typeerror. Если передано не натуральное число то valueerror


def count_prime_factors(n):
    if not isinstance(n, (int, float)):
        raise TypeError
    if not (isinstance(n, int) and n > 0):
        raise ValueError
    count = 0
    i = 2
    while n != 1:
        if n % i == 0:
            n = n // i
            count += 1
        else:
            i += 1
    return count


if __name__ == '__main__':
    print(count_prime_factors(500))
