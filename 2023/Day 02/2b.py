input = open("input")

def game_minimum_set(game):
	min_set = [0,0,0]
	for subset in game:
		cubes = subset.split(', ')
		for colour in cubes:
			space = colour.find(' ')
			if "red" in colour:
				r = int(colour[:space])
				if r > min_set[0]:
					min_set[0] = r
			if "green" in colour:
				g = int(colour[:space])
				if g > min_set[1]:
					min_set[1] = g
			if "blue" in colour:
				b = int(colour[:space])
				if b > 
				min_set[2]:
					min_set[2] = b
	return min_set

def game_power(game_set):
	return game_set[0] * game_set[1] * game_set[2]

answer = 0

for line in input:
	colon = line.find(':')
	id = int(line[5:colon])
	game = line[colon+2:].split('; ')
	answer += game_power(game_minimum_set(game))

print(answer)

