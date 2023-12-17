def expand(universe):
	expanded = []
	for i in range(len(universe)):
		expanded.append(1)
		try:
			galaxy = universe[i].index("#")
		except ValueError:
			expanded[i] = 1000000
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

expansion_x = expand(universe)
universe = rotate(universe)
expansion_y = expand(universe)
galaxies = find_galaxies(universe)

answer = 0
for i in range(len(galaxies)):
	for j in range(i+1, len(galaxies)):
		g1 = galaxies[i]
		g2 = galaxies[j]
		dx = sum(expansion_x[min(g1[0],g2[0])+1:max(g1[0],g2[0])+1])
		dy = sum(expansion_y[min(g1[1],g2[1])+1:max(g1[1],g2[1])+1])
		answer += (dx + dy)
print(answer)