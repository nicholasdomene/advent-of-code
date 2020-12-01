f = list(open("day_1_input.txt", "r"))

for i in range(len(f)):
	f[i] = int(f[i].replace("\n", ""))

def solution_1():
	for i in range(len(f)-1):
		for j in range(1, len(f)):
			if f[i] + f[j] == 2020:
				return f[i]*f[j]

def solution_2():
	for i in range(len(f)-2):
		for j in range(1, len(f)-1):
			for k in range(2, len(f)):
				if f[i] + f[j] + f[k] == 2020:
					return f[i]*f[j]*f[k]

s1 = solution_1()
print(s1)

s2 = solution_2()
print(s2)
