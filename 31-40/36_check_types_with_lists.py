# Реализовать декоратор check_types, принимающий типы (или списки типов)
# и проверяющий, что параметры функции, к которой применён декоратор,
# являются объектами соответствующих типов или их подклассами.
# В случае несоответствия выбрасывать исключение TypeError.


def check_types(*types):
    def decorator(f):
        def wrapper(*args, **kwargs):
            check_list(args, types)
            return f(*args, **kwargs)
        return wrapper
    return decorator


def check_list(args_list, types_list):
    if len(args_list) != len(types_list):
        raise TypeError
    for i in range(len(args_list)):
        if isinstance(args_list[i], list) and isinstance(types_list[i], list):
            check_list(args_list[i], types_list[i])
        elif not isinstance(args_list[i], types_list[i]):
            raise TypeError

if __name__ == '__main__':
    @check_types([str, int, [int, str, [str, list]]])
    def test(a):
        print(a)
    test(['a', 5, [5, 'b', ['c,', 5]]])