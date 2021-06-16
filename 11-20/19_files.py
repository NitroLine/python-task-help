# Написать функцию выполняющую слияние файлов, принимающую имя файла для вывода и *args имён файлов для слияния(30 баллов)


def merge_files(output_file, *args):
    with open(output_file, 'wb') as output:
        for file in args:
            with open(file, 'rb') as input:
                for line in input:
                    output.write(line)
                output.write(b'\n')
