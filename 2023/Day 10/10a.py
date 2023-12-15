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


def where_to_next(current, from_dir):
	if current == '.':
		raise ValueError
	opts = connections[current]
	if opts[0] == from_dir:
		return opts[1]
	if opts[1] == from_dir:
		return opts[0]
	raise ValueError

def follow_path(currentPos, from_dir):
	steps = 1
	y,x = currentPos
	current = maze[currentPos[0]][currentPos[1]]
	while current != "S":
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
maze = []

with open("input") as file:
	maze = file.readlines()
	for y, line in enumerate(maze):
		for x, char in enumerate(line):
			if char == "S":
				start = (x, y)

path_length = 0

try:
	where_to_next(maze[start[1]][start[0]+1], "W")
	path_length = follow_path((start[1],start[0]+1), "W")
except ValueError:
	try:
		where_to_next(maze[start[1]][start[0]-1], "E")
		path_length = follow_path((start[1],start[0]-1), "E")
	except ValueError:
		path_length = follow_path((start[1]-1,start[0]), "S")

answer = int(path_length / 2)
print(answer)
