#  Написать функцию, которая принимает на вход матрицу (список списков) и возвращает матрицу, повернутую на -90 градусов.
#  Если на вход идёт не список списков, то выдать TypeError, если на входе не матрица, то выдать ValueError (30 баллов)

def transpose_matrix(m):
    check_matrix(m)
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]) - 1, -1, -1)]


def check_matrix(matrix):
    width = len(matrix[0])
    for row in matrix:
        if len(row) != width:
            raise ValueError


if __name__ == '__main__':
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    print(transpose_matrix(matrix))
