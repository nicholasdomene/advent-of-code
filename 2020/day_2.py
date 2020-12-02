f = list(open("day_2_input.txt", "r"))

def separate_entry(row):
	first_second = row[0].split("-")
	first = int(first_second[0])
	second = int(first_second[1])
	letter = row[1][:-1]
	password = row[2]
	return first, second, letter, password

def count_letter(password, letter):
	count = 0
	for l in password:
		if l == letter:
			count += 1
	return count

def position_letter(password, pos1, pos2, letter):
	contains = 0
	if len(password) <= pos2: return 0
	if password[pos1] == letter: contains += 1
	if password[pos2] == letter: contains += 1
	if contains == 1: return 1
	return 0

def solution_1():
	valid = 0
	for entry in f:
		row = entry.split()
		minimum, maximum, letter, password = separate_entry(row)
		count = count_letter(password, letter)
		if count >= minimum and count <= maximum:
			valid += 1
	return valid

def solution_2():
	valid = 0
	for entry in f:
		row = entry.split()
		pos1, pos2, letter, password = separate_entry(row)
		#toboggan corporate policies have no concept of index zero
		pos1 -= 1
		pos2 -= 1
		v = position_letter(password, pos1, pos2, letter)
		valid += v
	return valid



s1 = solution_1()
print("Solution for part 1 is ", s1)
s2 = solution_2()
print("Solution for part 2 is ", s2)