# Реализовать функцию roots, принимающую вектор (список) коэффициентов многочлена (заданы по убыванию степеней)
# над кольцом ℤ
# и возвращающую список, который содержит все целые корни многочлена в порядке убывания.


def roots(polynomial):
    ans = []
    if polynomial[-1] == 0:
        ans.append(0)
        while polynomial[-1] != 0:
            polynomial = polynomial[:-1]
    for d in divisors(abs(polynomial[-1])):
        if polynomial_value(polynomial, d) == 0:
            ans.append(d)
    return sorted(ans, reverse=True)

def divisors(number):
    i = 1
    while i * i <= number:
        if number % i == 0:
            yield i
            yield -i
        i += 1

def polynomial_value(polynomial, x):
    value = 0
    for i in range(len(polynomial)):
        value += polynomial[i] * x ** (len(polynomial) - i - 1)
    return value
