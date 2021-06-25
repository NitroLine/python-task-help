# Реализовать функцию sum_time, принимающую текст, содержащий время в формате d.hh:mm:ss (части d. и d.hh: могут отсутствовать)
# и возвращающую сумму времён. Результатом должна быть строка в аналогичном формате.

import datetime
import re


def sum_time(*timeList):
    stub = "00:00:00:00"
    mysum = datetime.timedelta()
    for i in timeList:
        i = stub[:len(stub)-len(i)] + i
        (d, h, m, s) = i.split(':')
        d = datetime.timedelta(days=int(d), hours=int(h), minutes=int(m), seconds=int(s))
        mysum += d
    return format_date(mysum.days, mysum.seconds // 3600, (mysum.seconds % 3600) // 60, mysum.seconds % 60)


def format_date(days, hours, minutes, seconds):
    hours = '0' * (2 - len(str(hours)))+str(hours)
    minutes = '0' * (2 - len(str(minutes))) + str(minutes)
    seconds = '0' * (2 - len(str(seconds))) + str(seconds)
    return f"{days}:{hours}:{minutes}:{seconds}"


def find_times_in_text(text):
    for match in re.findall(r'\d?\d?:?\d?\d?:?\d{2}:\d{2}', text):
        yield match


if __name__ == '__main__':
    text = '''00:23:02:02
                01:02:02
                02:02
                0:0:02:02'''
    print(sum_time(*find_times_in_text(text)))
