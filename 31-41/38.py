# Реализовать менеджер контекстов open_files(*filenames, mode, encoding),
# открывающий заданные файлы в указанном режиме и кодировке.

from contextlib import contextmanager


@contextmanager
def open_files(*args, mode='r', encoding='cp866'):
    files = []
    print(args)
    try:
        for file_path in args:
            f_obj = open(file_path, mode, encoding=encoding)
            files.append(f_obj)
        yield files
    except OSError as e:
        raise e
    finally:
        for file in files:
            file.close()


if __name__ == '__main__':
    with open_files('1.txt', '2.txt', mode='r', encoding='cp866') as (f, g):
        print(f.read(), g.read())