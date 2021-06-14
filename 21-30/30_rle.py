# Реализовать RLE-упаковщик и распаковщик. Первое принимает итератор и выдает упакованный итератор,
# второе принимает упакованный итератор, выдает распакованный. (30 баллов)


def rle_encode(data):
    prev_char = ''
    count = 1
    for char in data:
        if char != prev_char:
            if prev_char:
                if count != 1:
                    for s in str(count):
                        yield s
                yield prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        if count != 1:
            for s in str(count):
                yield s
        yield prev_char


def rle_decode(data):
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            if count == '':
                count = '1'
            for i in range(int(count)):
                yield char
            count = ''


import unittest


class RLETests(unittest.TestCase):
    def test_edges(self):
        self.assertEqual(''.join(rle_encode('')), '')  # empty
        self.assertEqual(''.join(rle_encode('a')), 'a')  # one
        self.assertEqual(''.join(rle_encode('aa')), '2a')  # two
        self.assertEqual(''.join(rle_encode('aab')), '2ab')  # two + one
        self.assertEqual(''.join(rle_encode('abb')), 'a2b')  # one + two
        self.assertEqual(''.join(rle_encode('aabb')), '2a2b')  # two + two

    def test_nonletter(self):
        self.assertEqual(''.join(rle_encode('ab b')), 'ab b')

    def test_input(self):
        self.assertEqual(''.join(rle_encode('aaabccccCCaB')), '3ab4c2CaB')

    def test_decode(self):
        self.assertEqual(''.join(rle_decode(rle_encode('aaabccccCCaB'))),
                         'aaabccccCCaB')
