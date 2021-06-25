# Реализовать функцию `print_matrix`, принимающую матрицу, заданную в виде списка списков, элементы матрицы
# - вещественные числа. Функция должна вывести матрицу чисел на экран так, чтобы значения в столбцах были выровнены по правому
# краю, все столбцы имели одинаковый размер и каждое число выведено с точностью до 2-х знаков после запятой.
# Столбцы друг от друга разделять двумя пробелами.
import pprint
def print_matrix(matrix):
    len_elem = get_len_of_max_element(matrix)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            s = '%.2f' % matrix[row][col]
            s = ' ' * (len_elem - len(s)) + s
            print(s, end="  ")
        print()


def get_len_of_max_element(matrix):
    max_elem = matrix[0][0]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            max_elem = max(max_elem, matrix[row][col])
    return len(str(round(max_elem, 2)))


if __name__ == '__main__':
    matrix = [[1.001, 2.1, 3.2], [4, 5.06, 7.21], [9.10, 5.6, 4]]
    print_matrix(matrix)