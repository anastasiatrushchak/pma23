
input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r") as file:
    fibonacci_numbers = list(file.read().split())


for i in range(2, 10):
    fibonacci_numbers.append(float(fibonacci_numbers[i - 1]) + float(fibonacci_numbers[i - 2]))

with open(output_file, "w") as record:
    record.write(str(fibonacci_numbers))





