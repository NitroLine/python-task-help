# Реализовать декоратор call_count на функцию, подсчитывающий количество вызовов функции.
# Количество вызовов должно сохраняться в атрибута calls функции.


def call_count(f):
    class CallCounter:
        def __init__(self):
            self._count = 0

        @property
        def count(self):
            return self._count

    count = CallCounter()

    def wrapper(*args, **kwargs):
        count._count += 1
        return f(*args, **kwargs)

    wrapper.calls = count
    return wrapper


if __name__ == '__main__':
    @call_count
    def test():
        pass
    print(test.calls.count)
    test()
    print(test.calls.count)
