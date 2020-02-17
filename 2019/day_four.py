min_range = 156218
max_range = 652527

def convert (list_password):
	s = [str(i) for i in list_password] 
	password = int("".join(s))
	return password

def valid_password_part_one(min_range, max_range):

	valid = 0
	password = min_range
	while password <= max_range:
		digits = list(str(password))
		for i in range(5):
			if digits[i + 1] < digits [i]:
				digits[i + 1] = digits[i]

		repetidos = 0
		for i in range(5):
			if digits[i + 1] == digits [i]:
				repetidos += 1

		password = convert(digits)

		if repetidos > 0:
			valid += 1
			print("%s is a valid password"%password)
		password += 1

	print("There are %s valid passwords in said range."%valid)

def valid_password_part_two(min_range, max_range):

	valid = 0
	password = min_range
	while password <= max_range:
		digits = list(str(password))
		for i in range(5):
			if digits[i + 1] < digits [i]:
				digits[i + 1] = digits[i]

		repeated = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		for i in range(6):
			for j in range(10):
				if digits[i] == str(j):
					repeated[j] += 1

		password = convert(digits)

		if 2 in repeated:
			valid += 1
			print("%s is a valid password"%password)
		password += 1

	print("There are %s valid passwords in said range."%valid)

valid_password_part_two(min_range, max_range)