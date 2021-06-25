# Реализовать функцию sum_time, принимающую текст, содержащий время в формате d.hh:mm:ss (части d. и d.hh: могут отсутствовать)
# и возвращающую сумму времён. Результатом должна быть строка в аналогичном формате.

import datetime
import re


def sum_time(text):
    stub = "00:00:00:00"
    mysum = datetime.timedelta()
    for i in re.findall(r'\d?\d?:?\d?\d?:?\d{2}:\d{2}', text):
        i = stub[:len(stub)-len(i)] + i
        (d, h, m, s) = i.split(':')
        d = datetime.timedelta(days=int(d), hours=int(h), minutes=int(m), seconds=int(s))
        mysum += d
    return f"{mysum.days}:{str(mysum.seconds // 3600).zfill(2)}:{str((mysum.seconds % 3600) // 60).zfill(2)}:{str(mysum.seconds % 60).zfill(2)}"


if __name__ == '__main__':
    text = '''00:01:02:02
                01:02:02
                02:02
                0:0:02:02'''
    print(sum_time(text))
