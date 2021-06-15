# Реализовать функцию `solve`, принимающую числовую функцию `f(x)`, действительные числа `a` и `b`, точность `eps`
# (по умолчанию примем равной `1e-10`). Функция должна вернуть одно из решений уравнения `f(x) = 0` на отрезке `[a; b]`
# с (абсолютной) точностью `eps`; либо выбросить исключение `ValueError`, если `f(a) < 0` или `f(b) > 0`.


def solve(function, a, b, eps=1e-10):
    if function(a) < 0 or function(b) > 0:
        raise ValueError
    while a + eps < b:
        mid = (a + b) / 2
        if abs(function(mid)) < eps:
            break
        if function(mid) > eps:
            a = mid
        elif function(mid) < -eps:
            b = mid
    return (a + b) / 2
