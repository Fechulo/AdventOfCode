input = open("input")
bag = (12,13,14)

def game_is_possible(game):
	for subset in game:
		cubes = subset.split(', ')
		if not set_is_possible(cubes):
			return False
	return True

def set_is_possible(subset):
	for colour in subset:
			space = colour.find(' ')
			if "red" in colour:
				r = int(colour[:space])
				if r > bag[0]:
					return False
			if "green" in colour:
				g = int(colour[:space])
				if g > bag[1]:
					return False
			if "blue" in colour:
				b = int(colour[:space])
				if b > bag[2]:
					return False
	return True

answer = 0

for line in input:
	colon = line.find(':')
	id = int(line[5:colon])
	game = line[colon+2:].split('; ')
	if game_is_possible(game):
		answer += id

print(answer)

