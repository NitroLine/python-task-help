# Реализовать декоратор call_count на функцию, подсчитывающий количество вызовов функции.
# Количество вызовов должно сохраняться в атрибута calls функции.


def call_count(f):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        return f(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


if __name__ == '__main__':
    @call_count
    def test():
        pass
    print(test.calls)
    test()
    print(test.calls)
