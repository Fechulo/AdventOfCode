import math

data = open("input")

directions = data.readline().replace("\n","");

paths = {}
nodes = []

for line in data:
	if line != "\n":

		eq = line.find('=')
		comma = line.find(',')
		rparen = line.find(')')

		node = line[:eq-1]
		left = line[eq+3:comma]
		right = line[comma+2:rparen]
		
		paths.update({node: (left, right)})

		if node[-1] == 'A':
			nodes.append(node)

steps = []

for node in nodes:
	dirs = directions
	step = 0
	while node[-1] != "Z":
		left, right = paths[node]

		if dirs[0]=='L':
			node = left
		if dirs[0]=='R':
			node = right

		step+=1
		dirs = dirs[1:]
		if len(dirs) == 0:
			dirs = directions

	if not step in steps:
		steps.append(step)

lcm = math.lcm(*steps)
print(lcm)