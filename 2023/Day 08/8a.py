data = open("test")

directions = data.readline().replace("\n","");

grammar = {}

for line in data:
	if line != "\n":

		eq = line.find('=')
		comma = line.find(',')
		rparen = line.find(')')

		node = line[:eq-1]
		left = line[eq+3:comma]
		right = line[comma+2:rparen]
		
		grammar.update({node: (left, right)})

current = "AAA"
dirs = directions
steps = 0
while current != "ZZZ":
	left, right = grammar[current]

	if dirs[0]=='L':
		current = left
	if dirs[0]=='R':
		current = right

	steps+=1
	dirs = dirs[1:]
	if len(dirs) == 0:
		dirs = directions

print(steps)