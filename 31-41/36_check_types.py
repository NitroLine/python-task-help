# Реализовать декоратор check_types, принимающий типы (или списки типов) и проверяющий, что параметры функции,
# к которой применён декоратор, являются объектами соответствующих типов или их подклассами.
# В случае несоответствия выбрасывать исключение TypeError.


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