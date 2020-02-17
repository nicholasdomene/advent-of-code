f = open("day_one_input.txt", "r")


def fuel(mass):
	return int(mass//3 - 2)

def part_one():
	total_fuel = 0
	for line in f:
		total_fuel += fuel(int(line))

	print("Total amount of fuel needed is %s"%total_fuel)

def part_two():
	total_fuel_for_fuel = 0
	fu = 0

	for line in f:
		fu = fuel(int(line))
		total_fuel_for_fuel += fu
		while fuel(int(fu)) > 0:
			fu = fuel(int(fu))
			total_fuel_for_fuel += fu

	print("Total amount of fuel for fuels needed is %s"%total_fuel_for_fuel)

part_two()