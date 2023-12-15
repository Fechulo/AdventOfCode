data = open("input")

seeds = data.readline().replace("\n","")
seed_values = seeds[seeds.find(':')+2:].split(' ')
seed_values = [int(i) for i in seed_values]

values = []
for i in range(0,len(seed_values),2):
	values.append((seed_values[i],seed_values[i+1]))

mappings = []

#print(values)

def convert_values():
	global values,mappings
	new_values = []
	mapped_values = []
	for value in values:
		for mapping in mappings:
			if value[0] >= mapping[1] and value[0] < mapping[1] + mapping[2]:
				if value[0] + value[1] <= mapping[1] + mapping[2]:
					#print(str(value) + " fits in range (" + str(mapping[1]) + ", "+str(mapping[2])+")")
					new_values.append((value[0] + (mapping[0] - mapping[1]),value[1]))
					mapped_values.append(value[0])
				else:
					#print(str(value) + " does not fit in range (" + str(mapping[1]) + ", "+str(mapping[2]) + ") ... splitting")
					new_values.append((value[0] + (mapping[0] - mapping[1]), mapping[1] + mapping[2] - value[0]))
					mapped_values.append(value[0])
					values.append((mapping[1] + mapping[2], value[1] - (mapping[1] + mapping[2] - value[0])))
	
	for value in values:
		if not value[0] in mapped_values:
			#print("No mapping found for "+str(value))
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
		#print(values)

convert_values()
#print(values)
print(min(values)[0])