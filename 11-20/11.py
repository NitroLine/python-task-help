# Дана строка из символов, вывести список в формате (символ, число повторений), отсортированный по убыванию частоты вхождения
# символа в строку. Если частота одинаковая, первым выводить лексикографически меньший символ.
# Считать регистронезависимо (т.е строку привести в нижний регистр) (30 баллов)

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
	