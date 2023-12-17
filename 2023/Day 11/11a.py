def expand(universe):
	expanded = []
	for space in universe:
		expanded.append(space)
		try:
			galaxy = space.index("#")
		except ValueError:
			expanded.append(space)
	return expanded

def rotate(universe):
	rotated = []

	for x in range(len(universe[0])):
		rotated.append([])
		for y in range(len(universe)):
			rotated[x].append(universe[y][x])

	return rotated

def find_galaxies(universe):
	galaxies = []
	for y in range(len(universe)):
		for x in range(len(universe[y])):
			if universe[y][x] == "#":
				galaxies.append((x,y))
	return galaxies

universe = []

with open("input") as file:
	lines = file.readlines()

	for line in lines:
		universe.append(list(line.replace("\n","")))

universe = expand(universe)
universe = rotate(universe)
universe = expand(universe)
galaxies = find_galaxies(universe)
answer = 0
for i in range(len(galaxies)):
	for j in range(i+1, len(galaxies)):
		g1 = galaxies[i]
		g2 = galaxies[j]
		dist = abs(g2[0]-g1[0]) + abs(g2[1]-g1[1])
		answer += dist
print(answer)