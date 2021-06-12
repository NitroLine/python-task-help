# Написать класс "вектор" с операциями
# +(сложение), -(вычитание), *(умножение на число), [ ](доступ к координатам)


class Vector:
    def __init__(self, *args):
        self._coordinates = args

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError
        if len(other._coordinates) != len(self._coordinates):
            raise ValueError
        new_coord = []
        for i in range(len(self._coordinates)):
            new_coord.append(self._coordinates[i]+other._coordinates[i])
        return Vector(*new_coord)

    def __getitem__(self, item):
        return self._coordinates[item]

    def __iter__(self):
        for x in self._coordinates:
            yield x

    def __sub__(self, other):
        if not isinstance(other, Vector):
            raise TypeError
        if len(other._coordinates) != len(self._coordinates):
            raise ValueError
        new_coord = []
        for i in range(len(self._coordinates)):
            new_coord.append(self._coordinates[i]*other._coordinates[i])
        return Vector(*new_coord)

    def __mul__(self, other):
        new_coord = []
        for i in range(len(self._coordinates)):
            new_coord.append(self._coordinates[i]*other)
        return Vector(*new_coord)