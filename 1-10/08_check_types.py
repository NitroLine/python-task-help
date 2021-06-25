#  Написать функцию-декоратор, который принимает типы или списки типов и проверяет что параметры, передаваемые в функцию,
#  соответствуют указанным типам. Если один из переданных параметров не соответствует ни одному из типов,
#  выкинуть исключение TypeError. (40 баллов)


def check_types(types):
    def decorator(f):
        def wrapper(*args, **kwargs):
            if len(args) != len(types):
                raise TypeError
            for i in range(len(args)):
                if not isinstance(args[i], types[i]):
                    raise TypeError
            return f(*args, **kwargs)
        return wrapper
    return decorator


if __name__ == '__main__':
    @check_types([int,str])
    def test(a,b):
        print(a,b)
    test(5,'me')