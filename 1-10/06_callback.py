# Написать менеджер контекста, который принимает callback и reraise, если reraise True прокидывать исключения по стеку вверх,
# иначе вызывать callback, передавая ему ошибку и стек вызовов (и ещё что-то) (40 баллов)


class ContextManager:
    def __init__(self, callback, reraise):
        self._callback = callback
        self._reraise = reraise

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if value is None:
            return
        if self._reraise:
            return False
        else:
            self._callback(type, value, traceback)
            return True