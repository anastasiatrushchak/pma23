InputFile = "input.txt"
OutputFile = "output.txt"
STEPS = "steps.txt"
with open(InputFile, "r") as input_file:
    array = input_file.readline().split()
for i in range(0,array.__len__()):
    array[i] = float(array[i])
with open(STEPS, "r") as steps:
    steps = int(steps.readline())
for i in range(2, steps):
    array.append(array[i-1]+array[i-2])
with open(OutputFile, "w") as output_file:
    output_file.write(array.__str__())
