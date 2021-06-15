#  Реализовать декоратор `debug`, принимающий в качестве параметра file-like object и печатающий в него название функции,
#  параметры её вызова, результат и время работы (в секундах), согласно примерам:
#  ```
#    1.5 func1(1, 2) -> 3
#    0.5 func1(‘1’, y=2) -> 12
#    2.04 func1(‘a’, ‘’) -> TypeError(‘y’)
#  ```

import time


def debug(file):
    def decorator(function):
        def wrapper(*args, **kwargs):
            with open(file, 'a') as f:
                start_time = time.clock()
                try:
                    res = function(*args, **kwargs)
                except Exception as e:
                    res = type(e).__name__ + f"('{e}')"
                working_time = time.clock() - start_time
                kwargs_str = ''
                for key, val in kwargs.items():
                    if isinstance(val, str):
                        val = f"\'{val}\'"
                    kwargs_str += f'{key}={val}, '
                f.write(f'{working_time} {function.__name__}'
                        f'({str(args)[1:-1]} {kwargs_str[:-2]}) -> {str(res)}\n')
        return wrapper
    return decorator
