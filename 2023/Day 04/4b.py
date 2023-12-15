data = open("input")

lines = data.readlines()
line_count = len(lines)
instances = [1]*line_count

for i, line in enumerate(lines):
	line = line.replace("  "," ") #removes double spaces
	line = line.replace("\n","") #removes new lines

	winning_numbers = line[line.find(':')+2:line.find('|')-1].split(' ')
	drawn_numbers = line[line.find('|')+2:].split(' ')
	
	win_count = 0
	for number in drawn_numbers:
		if number in winning_numbers:
			win_count+=1

	for j in range(win_count):
		instances[i+j+1] += instances[i]

answer = sum(instances)
print(answer)