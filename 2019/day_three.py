f = open("day_three_input.txt", "r")
f = list(f)

directions_one = f[0]
directions_two = f[1]

def convert (list_steps):
	s = [str(i) for i in list_steps] 
	steps = int("".join(s))
	return steps


def steps(direction, position):
	d = (direction.split(','))[0]
	s = direction.split(',')[1:]
	print(s)
	print(d)
	quantity = convert()
	steps = set()
	if d == "U": 
		for i in range(quantity):
			position += (0, 1)
	elif d == "D":
		for i in range(quantity):

			position += (0, -1)
	elif d == "L":
		for i in range(quantity):

			position += (1, 0)
	elif d == "R":
		for i in range(quantity):

			position += (-1, 0)
	return steps, position

def path(directions):
	p = set()
	position = (0, 0)
	print(directions)
	for direction in directions:
		step, position = steps(direction, position)
		p.add(step)
	return p

print(path(directions_one))