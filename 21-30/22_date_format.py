# На вход подается строка, в которой встречается дата в формате dd.mm.yyyy, ее надо заменить в этой строке на формат yyyy-mm-dd
import re


def format_date(s):
    return re.sub(r'(\d{2}).(\d{2}).(\d{4})',r'\3-\2-\1', s)


if __name__ == '__main__':
    print(format_date('14.06.2021 today!'))