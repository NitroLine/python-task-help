# Написать функцию, возвращающую True или False, если число является александрийским.


def isAlexanderNumber(number):
    for p in range(1, int(number ** (1 / 3)) + 1):
        if number / p != number // p:
            continue
        ppplus1 = p * p + 1
        for k in range(1, int(ppplus1**(1 / 2)) + 1):
            r = -ppplus1 / k - p
            if r != int(r):
                continue
            q = -k - p
            if number == p * r * q and 1 == p*q + p*r + q*r:
                return True
    return False


if __name__ == '__main__':
    print(isAlexanderNumber(1884161251122450))
