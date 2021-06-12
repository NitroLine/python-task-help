# Написать функцию, которая считает определитель данной матрицы (matrix=[[...],[...],[...],...,[...]].


def determinant(matrix, coefficient=1):
    width = len(matrix)
    if width == 1:
        return coefficient * matrix[0][0]
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            total += coefficient * determinant(m, coefficient=sign * matrix[0][i])
        return total
