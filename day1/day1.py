def solve_one():
	f = open("a.in", "r")
	Lines = f.readlines()
	sum = 0
	for line in Lines:
		# find forward number
		for c in line:
			if(c.isdigit()):
				sum += int(c)
				break

		# last num
		for c in reversed(line):
			if(c.isdigit()):
				sum += int(c)
				break

	print(sum)

solve_one()