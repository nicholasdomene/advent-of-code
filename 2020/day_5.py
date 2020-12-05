f = list(open("day_5_input.txt", "r"))








def decode(passport):

	front = 0
	back = 127
	for i in range(7):
		mid = (front+back)//2
		if passport[i] == "F":
			back = mid-1
		else:
			front = mid+1
	row = (front+back+1)//2

	left = 0
	right = 7
	for i in range(3):
		mid = (left+right)//2
		if passport[7+i] == "L":
			right = mid-1
		else:
			left = mid+1
	column = (left+right+1)//2

	passport_id = row*8 + column
	return row, column, passport_id

def solution_1():
	highest_id = 0
	for passport in f:
		r, c, pass_id = decode(passport)
		if pass_id > highest_id:
			highest_id = pass_id

	return highest_id

def solution_2():
	max_id = solution_1()
	seats = set([i for i in range(max_id)])

	for passport in f:
		r, c, pass_id = decode(passport)
		if pass_id in seats:
			seats.remove(pass_id)

	for seat in seats:
		if seat-1 not in seats and seat+1 not in seats:
			return seat

s1 = solution_1()
print("Solution for part 1: ", s1)

s2 = solution_2()
print("Solution for part 2: ", s2)