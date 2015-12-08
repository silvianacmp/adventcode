memoryCount = 0
literalCount = 0
newCount = 0

while True:
    line = raw_input()
    if line == "end":
        break
    # add 2 ch for the beginning and ending quotes from the start
    memoryCount += 2
    newCount += 6
    i = 1
    while i < len(line) - 1:
        if line[i] == '\\':
            if line[i + 1] == '\\' or line[i + 1] == '\"':
                literalCount += 1
                memoryCount += 2
                newCount += 4
                i += 2
            elif line[i + 1] == 'x':
                literalCount += 1
                memoryCount += 4
                newCount += 5
                i += 4
        else:
            literalCount += 1
            memoryCount += 1
            newCount += 1
            i += 1

print memoryCount - literalCount
print newCount - memoryCount

