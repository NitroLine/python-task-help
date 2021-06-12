# Пусть панграмма это такая строка в которой содержатся все буквы алфавита.
# Пример такой фразы:
#     The quick brown fox jumps over the lazy dog.
#  Написать такую функцию определяющую является ли строка панграммой.
#  На вход функции подается сама строка и алфавит.


def test_panagram(text, abc):
    return set(text) == set(abc)


if __name__ == '__main__':
    test = 'The quick brown fox jumps over the lazy dog'
    test2 = 'abracadabra'
    abc = 'abcdefghijklmnopqrsTtuvwxyz '
    print(test_panagram(test, abc))
    print(test_panagram(test2, abc))

