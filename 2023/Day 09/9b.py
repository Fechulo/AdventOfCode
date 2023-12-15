def read_numbers(line):
	nums = []
	while len(line)>0:
		space = line.find(' ')
		if space == -1:
			nums.append(int(line))
			break
		n = line[:space]
		nums.append(int(n))
		line = line[space+1:]
	return nums

def differences(seq):
	diffs = []
	all_zeros = True
	for i in range(1, len(seq)):
		diffs.append(seq[i]-seq[i-1])
		if seq[i]!=0:
			all_zeros = False
	if all_zeros:
		return 0
	prev_diff = differences(diffs)
	return diffs[0] - prev_diff

data = open("input")

answer = 0
for line in data:
	seq = read_numbers(line)
	diff = differences(seq)
	prev_value = seq[0] - diff
	answer += prev_value

print(answer)