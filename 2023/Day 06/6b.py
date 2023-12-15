import math 

def is_number(char):
	return char >= '0' and char <= '9'

def read_number(line):
	n = 0
	for char in line:
		if is_number(char):
			n*=10
			n+=int(char)
	return n

data = open("input")
t = read_number(data.readline())
d = read_number(data.readline())

solution = round(t - 2*(t - (math.sqrt((t*t)-4*d)))/2)
print(solution)