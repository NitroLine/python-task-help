# Написать декоратор, который будет считать кол-во вызовов функции, сохраняя это кол-во в атрибут calls


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
