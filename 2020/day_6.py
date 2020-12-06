import collections as c

f = list(open("day_6_input.txt", "r"))
for i in range(len(f)):
	f[i] = f[i].replace("\n", "")
f.append("")

def count_answer_any(group):
	#string -> int
	return len(c.Counter(group))

def count_answer_all(group, group_size):
	#list, list -> int
	s = 0
	counter = c.Counter(group)
	for letter in counter:
		if counter[letter] == group_size:
			s += 1
	return s


def separate_groups(file):
	#list -> list
	group = ""
	groups = []
	group_size = 0
	groups_size = []
	for i in range(len(f)):
		if file[i] == "":
			groups.append(group)
			groups_size.append(group_size)
			group = ""
			group_size = 0
		else:
			group += file[i]
			group_size += 1
	return groups, groups_size


def solution_1():
	s = 0
	groups, g_s = separate_groups(f)
	for group in groups:
		s += count_answer_any(group)
	return s

def solution_2():
	s = 0
	groups, groups_size = separate_groups(f)
	for i in range(len(groups)):
		s += count_answer_all(groups[i], groups_size[i])

	return s

s1 = solution_1()
print("Solution for part 1: ", s1)

s2 = solution_2()
print("Solution for part 2: ", s2)
