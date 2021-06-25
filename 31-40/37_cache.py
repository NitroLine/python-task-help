# Написать кэширующий декоратор, для функции f, если f(x) и f(x=) можно считать разными вызовами(40 баллов).


def cache(f):
    values = dict()

    def wrapper(*args, **kwargs):
        key = str(args) + str(sorted(kwargs))
        if key not in values:
            values[key] = f(*args, **kwargs)
        return values[key]

    return wrapper
