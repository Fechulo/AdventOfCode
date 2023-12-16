connections = {
	"|": "NS",
	"-": "EW",
	"L": "NE",
	"J": "NW",
	"7": "SW",
	"F": "SE"
}

opposite = {
	"N": "S",
	"S": "N",
	"E": "W",
	"W": "E"
}

vertices = "LJ7F"


def where_to_next(current, from_dir):
	if current == '.':
		return "X"
	opts = connections[current]
	if opts[0] == from_dir:
		return opts[1]
	if opts[1] == from_dir:
		return opts[0]
	return "X"

def follow_path(currentPos, from_dir):
	steps = 1
	y,x = currentPos
	current = maze[currentPos[0]][currentPos[1]]
	while current != "S":
		maze_copy[y][x] = current
		steps+=1
		next_dir = where_to_next(current, from_dir)
		from_dir = opposite[next_dir]

		if next_dir == "N":
			y = y-1
		elif next_dir == "S":
			y = y+1
		elif next_dir == "E":
			x = x+1
		elif next_dir == "W":
			x=x-1
		else:
			print("HUH?")

		current = maze[y][x]

	return steps

start = (0,0)
start_dirs = ""
maze = []
maze_copy = []

with open("input") as file:
	maze = file.readlines()

	h = len(maze)
	w = len(maze[0])
	for i in range(h):
		maze_copy.append(list("."*w))

	for y, line in enumerate(maze):
		for x, char in enumerate(line):
			if char == "S":
				start = (x, y)

				start_dirs = ""
				if where_to_next(maze[y-1][x], "S") != "X":
					start_dirs += "N"
				if where_to_next(maze[y+1][x], "N") != "X":
					start_dirs += "S"
				if where_to_next(maze[y][x+1], "W") != "X":
					start_dirs += "E"
				if where_to_next(maze[y][x-1], "E") != "X":
					start_dirs += "W"				

				vertex = list(connections.keys())[list(connections.values()).index(start_dirs)]
				maze_copy[y][x] = vertex
				break

start_dir = start_dirs[0]
if start_dir == "N":
	follow_path((start[1]-1,start[0]), "S")
elif start_dir == "S":
	follow_path((start[1]+1,start[0]), "N")
elif start_dir == "E":
	follow_path((start[1],start[0]+1), "W")
elif start_dir == "W":
	follow_path((start[1],start[0]-1), "E")
else:
	print("HUH?")

answer = 0
h = len(maze_copy)
for y in range(h):
	w = len(maze_copy[y])
	inside = False
	last_vertex = ""
	for x in range(w):
		p = maze_copy[y][x]
		if p == "." and inside:
			answer+=1
			maze_copy[y][x] = "I"
		elif p == "|":
			inside = not inside
		elif p in vertices:
			if last_vertex == "":
				last_vertex = p
			else:
				if connections[p][0] == opposite[connections[last_vertex][0]]:
					inside = not inside
				last_vertex = ""
print(answer)