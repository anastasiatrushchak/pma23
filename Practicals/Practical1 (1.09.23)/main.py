# read_file = open('input.txt')
# line = read_file.readline()
# read_file.close()
# array = line.split(",")
# array = [float(i) for i in array if i.isdigit()]
#
# for i in range(0, 8):
#     array.append(array[i] + array[i + 1])
# print(array)
# output_file = open("output.txt", "w")
# output_file.write(str(array))


import constants
with open(constants.INPUT, 'r') as readFile:
    line = readFile.readline()

array = line.split(constants.SEPARATOR)
array = [float(i) for i in array if i.isdigit()]
for i in range(0, 8):
    array.append(array[i] + array[i + 1])

print(array)
with open(constants.OUTPUT, 'w') as writeFile:
    writeFile.write(str(array))
