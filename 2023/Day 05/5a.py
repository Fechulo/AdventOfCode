data = open("test")

seeds = data.readline().replace("\n","")
values = seeds[seeds.find(':')+2:].split(' ')
values = [int(i) for i in values]
mappings = []

print(values)

def convert_values():
	global values,mappings
	new_values = []
	mapped_values = []
	for mapping in mappings:
		for value in values:
			if value >= mapping[1] and value < mapping[1] + mapping[2]:
				new_values.append(value + (mapping[0] - mapping[1]))
				mapped_values.append(value)
	
	for value in values:
		if not value in mapped_values:
			new_values.append(value)
	values = new_values
	mappings = []

for line in data:
	if line[0] >= '0' and line[0] <= '9':
		mapping = line.replace("\n","").split(' ')
		mapping = [int(i) for i in mapping]
		mappings.append(mapping)

	elif len(mappings) != 0:
		convert_values()
		print(values)

		#dest_min = line[:line.find(' ')]
		#source_min = line[line.find(' ')+1:line.find(' ', )]

convert_values()
print(values)
answer = min(values)
print(answer)