def calculate_distance(press_duration, total_duration):
	speed = 0
	for i in range(press_duration):
		speed+=1
		total_duration-=1

	distance = 0
	for i in range(total_duration):
		distance += speed

	return distance

def is_number(char):
	return char >= '0' and char <= '9'

def read_numbers(line):
	output = []
	n = 0
	for char in line:
		if is_number(char):
			n*=10
			n+=int(char)
		else:
			if n != 0:
				output.append(n)
				n = 0
	if n != 0:
		output.append(n)
	return output

data = open("input")
times = read_numbers(data.readline())
distances = read_numbers(data.readline())

answer = 1
for i, time in enumerate(times):
	min_press = 0
	for t in range(time):
		d = calculate_distance(t, time)
		if d > distances[i]:
			min_press = t
			break


	answer *= (time - (min_press*2) + 1)

print(answer)