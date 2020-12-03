f = list(open("day_3_input.txt", "r"))

def solution_1():
	trees = 0

	size_row = len(f[0])-1

	for i in range(len(f)):
		location = f[i][i*3%size_row]
		if location == "#":
			trees += 1

	return trees

def find_trees(right, down):
	trees = 0

	size_row = len(f[0])-1

	for i in range(0, len(f), down):
		location = f[i][i*right%size_row]
		if location == "#":
			trees += 1
	return trees

def solution_2():
	slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

	solution = 1
	for slope in slopes:
		solution *= find_trees(slope[0], slope[1])

	return solution

s1 = solution_1()
print("Solution part 1: ", s1)

s2 = solution_2()
print("Solution part 2: ", s2)