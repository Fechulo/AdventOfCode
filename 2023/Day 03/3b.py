input = open("input")

answer = 0

lines = input.readlines()
h = len(lines)

def is_number(char):
	return char >= '0' and char <= '9'

def go_left(line,x):
	n = ""

	if x > 0:
		d = 1
		c = line[x-d]
		while is_number(c):
			n = c + n
			d += 1
			if x-d < 0:
				break
			c = line[x-d]

	return n

def go_right(line,x):
	n = ""

	if x < len(line)-1:
		d = 1
		c = line[x+d]
		while is_number(c):
			n += c
			d += 1
			if x+d >= len(line):
				break
			c = line[x+d]

	return n

for y, line in enumerate(lines):
	for x, char in enumerate(line):
		if char == '*':
			numbers = []

			l = go_left(line,x)
			if l!="":
				numbers.append(l)

			r = go_right(line,x)
			if r!="":
				numbers.append(r)


			if y > 0:
				l = go_left(lines[y-1],x)
				r = go_right(lines[y-1],x)

				if is_number(lines[y-1][x]):
					n = l + lines[y-1][x] + r
					if n!="":
						numbers.append(n)
				else:
					if l!="":
						numbers.append(l)
					if r!="":
						numbers.append(r)

			if y < h-1:
				l = go_left(lines[y+1],x)
				r = go_right(lines[y+1],x)

				if is_number(lines[y+1][x]):
					n = l + lines[y+1][x] + r
					if n!="":
						numbers.append(n)
				else:
					if l!="":
						numbers.append(l)
					if r!="":
						numbers.append(r)

			if len(numbers) == 2:
				ratio = int(numbers[0]) * int(numbers[1])
				answer += ratio

print(answer)