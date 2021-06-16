# Написать функцию, выполняющую слияние нескольких файлов. (Принимает имя итогового файла и сами файлы)


def merge_files(output_file, *args):
    with open(output_file, 'wb') as output:
        for file in args:
            with open(file, 'rb') as input:
                for line in input:
                    output.write(line)
                output.write(b'\n')
