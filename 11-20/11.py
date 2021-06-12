# ���� ������ �� ��������, ������� ������ � ������� (������, ����� ����������), ��������������� �� �������� ������� ���������
# ������� � ������. ���� ������� ����������, ������ �������� ����������������� ������� ������.
# ������� ������������������ (�.� ������ �������� � ������ �������) (30 ������)

def symbols_count(string):
	string = string.lower()
	d = dict()
	for symbol in string:
		if symbol not in d:
			d[symbol] = 0
		d[symbol] += 1
	d = sorted(d.items(), key=lambda x: x[1], reverse=True)
	return d	


if __name__ == '__main__':
	test_string = 'AbraCadaBra'
	print(symbols_count(test_string))
	