# Реализовать RLE-упаковщик и распаковщик. Первое принимает итератор и выдает упакованный итератор,
# второе принимает упакованный итератор, выдает распакованный. (30 баллов)


# TODO fix this
import itertools


def rle_encode(data):
    prev_char = ''
    count = 1
    for char in data:
        if char != prev_char:
            if prev_char:
                yield str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        yield str(count) + prev_char


def rle_decode(data):
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            for i in range(len(count)):
                yield char
            count = ''


def rle_encode(text):
    text += '\0'  # dummy
    last = text[0]
    count = 1
    for char in text[1:]:
        if char != last:
            yield last if count == 1 else str(count) + last
            last = char
            count = 0
        count += 1


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
        self.assertEqual(''.join(rle_encode('abb\0\0')), 'a2b')

    def test_input(self):
        self.assertEqual(''.join(rle_encode('aaabccccCCaB')), '3ab4c2CaB')

    def test_decode(self):
        self.assertEqual(''.join(rle_decode(''.join(rle_encode('aaabccccCCaB')))),
                         'aaabccccCCaB')
