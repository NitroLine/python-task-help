import functools


def with_retries(max_tries):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for n in range(1, max_tries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if n == max_tries:
                        raise
        return wrapper
    return decorator


if __name__ == '__main__':
    import random

    @with_retries(max_tries=5)
    def do_something_unreliable():
        """Do something unreliably."""
        if random.randint(0, 10) > 1:
            raise IOError("Broken sauce, everything is hosed!!!111one")
        else:
            return "Awesome sauce!"

    print(do_something_unreliable())