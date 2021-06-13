# Написать функцию, дается на вход две строки, вернуть сдвиг если вторая строка это циклический сдвиг первой,
# если хотя бы один аргумент не строка выкинуть TypeError


def is_cycle_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise TypeError
    if len(str1) != len(str2):
        return False
    for shift in range(len(str1)+1):
        shifted = str2[-shift:] + str2[:-shift]
        if shifted == str1:
            return True
    return False


if __name__ == '__main__':
    print(is_cycle_strings('abc', 'cab'))
    print(is_cycle_strings('abc', 'cba'))

