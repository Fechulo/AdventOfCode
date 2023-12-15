data = open("input")

answer = 0

for line in data:
	line = line.replace("  "," ") #removes double spaces
	line = line.replace("\n","") #removes new lines

	winning_numbers = line[line.find(':')+2:line.find('|')-1].split(' ')
	drawn_numbers = line[line.find('|')+2:].split(' ')
	
	win_count = 0
	for number in drawn_numbers:
		if number in winning_numbers:
			win_count+=1

	points = 0
	if win_count > 0:
		points = 2**(win_count-1)

	answer += points

print(answer)