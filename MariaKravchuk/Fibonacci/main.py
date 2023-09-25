INPUT_CODE="input.txt"
OUTPUT_CODE="output.txt"
with open(INPUT_CODE, "r") as read_code:

 array_fibonacci = read_code.read().split("\n")
array_fibonacci = [float(i) for i in array_fibonacci if i.isdigit()]
for i in range(2, 10):
    array_fibonacci.append((array_fibonacci[i - 2]) + array_fibonacci[i - 1])

with open(OUTPUT_CODE, "w") as output_file:
