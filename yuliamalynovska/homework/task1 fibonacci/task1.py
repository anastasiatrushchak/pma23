import constant
with open(constant.NAME_INPUT, 'r') as input_file:
    array = input_file.readline().split()
# array = [float(i) for i in array if i.isdigit()]
array2 = []
for i in array:
    if i.isdigit():
        array2.append(float(i))
with open(constant.NAME_OUTPUT, 'w') as output_file:
    for i in range(2, 10):
        array2.append(array2[i - 1] + array2[i - 2])
    output_file.write(str(array2))
