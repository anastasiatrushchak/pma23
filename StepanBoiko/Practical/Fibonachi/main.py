import const

with open(const.INPUT, 'r') as readFile:
    line = readFile.readline()

numbers = line.split(const.SEPARATOR)
for i in range(numbers.__len__()):
   numbers[i] = int(numbers[i])
for i in range(0, 8):
    numbers.append(numbers[i] + numbers[i + 1])

print(numbers)
with open(const.OUTPUT, 'w') as writeFile:
    writeFile.write(str(numbers))
"""file = open('input.txt')
line = file.read()
file.close()
numbers = line.split(",")


for i in range(numbers.__len__()):
   numbers[i] = int(numbers[i])
file = open('output.txt', 'w')

for i in range(0, 15):
   numbers.append(numbers[i] + numbers[i+1])

file.write(str(numbers))
file.close()
"""
