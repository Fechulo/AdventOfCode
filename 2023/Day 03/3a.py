input = open("input")

answer = 0

lines = input.readlines()
h = len(lines)

def is_symbol(char):
	if char == '.':
		return False
	if char >= '0' and char <= '9':
		return False
	if char == '\n':
		return False
	return True

for y, line in enumerate(lines):
	n = 0
	is_part = False
	for x, char in enumerate(line):
		if char >= '0' and char <= '9':

			if n == 0:
				if not is_part:
					if x > 0:
						if is_symbol(lines[y][x-1]):
							is_part = True
						if y > 0:
							if is_symbol(lines[y-1][x-1]):
								is_part = True
						if y < h-1:
							if is_symbol(lines[y+1][x-1]):
								is_part = True

			if not is_part:
				if y > 0:
					if is_symbol(lines[y-1][x]):
						is_part = True
				if y < h-1:
					if is_symbol(lines[y+1][x]):
						is_part = True

			n = n*10
			n += int(char)

			if x == len(line)-1:
				if is_part:
					print(n)
					answer += n
		else:
			if n != 0:
				if is_symbol(char):
					is_part = True

				if not is_part:
					if y > 0:
						if is_symbol(lines[y-1][x]):
							is_part = True
					if y < h-1:
						if is_symbol(lines[y+1][x]):
							is_part = True

				if is_part:
					#print(str(n) + " YES")
					answer += n
				#else:
					#print(str(n) + " NO")
					#print("")

				n = 0
				is_part = False

print(answer)