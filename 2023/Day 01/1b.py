input = open("input")

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
    }

answer = 0

for line in input:
    first = 0
    for i, char in enumerate(line):
        n = ord(char) - 48
        if n >= 0 and n <=9:
            first = n
            break
        else:
            options = list(digits)
            for l in range(len(line)):
                candidate = line[i:i+l+1]
                if candidate in digits:
                    first = digits[candidate]
                    break
                else:
                    options = []
                    for option in list(digits):
                        if option.startswith(candidate):
                            options.append(option)
                    if len(options) == 0:
                        break
                    
            if first != 0:
                break

    last = 0    
    for i, char in enumerate(reversed(line)):
        n = ord(char) - 48
        if n >= 0 and n <=9:
            last = n
            break
        else:
            endi = len(line)-i
            for l in range(len(line)):
                starti = endi-l-1
                candidate = line[starti:endi]
                if candidate in digits:
                    last = digits[candidate]
                    break
                else:
                    options = []
                    for option in list(digits):
                        if option.startswith(candidate):
                            options.append(option)
                    if len(options) == 0:
                        break
                
            if last != 0:
                break

    answer += (first * 10) + last

print(answer)
