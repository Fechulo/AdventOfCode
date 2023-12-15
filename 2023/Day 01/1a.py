input = open("input")

answer = 0

for line in input:
    first = 0
    for char in line:
        n = ord(char) - 48
        if n >= 0 and n <=9:
            first = n
            break

    last = 0    
    for char in reversed(line):
        n = ord(char) - 48
        if n >= 0 and n <=9:
            last = n
            break

    answer += (first * 10) + last

print(answer)
