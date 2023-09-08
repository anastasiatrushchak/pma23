F1 = "input.txt"
F2 = "output.txt"
with open(F1, "r") as input_file:
    array = input_file.readline().split()
for i in range(0,array.__len__()):
    array[i] = float(array[i])
for i in range(2, 10):
    array.append(array[i-1]+array[i-2])
with open(F2, "w") as output_file:
    output_file.write(array.__str__())
