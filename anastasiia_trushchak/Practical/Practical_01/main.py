input_file = 'input.txt'
output_file = "output.txt"
with open(input_file, "r") as file:
    fibonacci = list(file.read().split())
for i in range(2, 10):
    fibonacci.append(float(fibonacci[i-1]) + float(fibonacci[i-2]))
with open(output_file, "w") as record:
    record.write(str(fibonacci))