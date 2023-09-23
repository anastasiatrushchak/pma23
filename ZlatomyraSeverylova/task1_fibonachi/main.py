INPUT = 'input.txt'
OUT = 'out.txt'
with open(INPUT, 'r') as f:
    array = f .read().split("\n")
    array = [float(i) for i in array if i.isdigit()]

for i in range(2, 10):
    array.append(array[i-1] + array[i-2])

with open(OUT, 'w') as f:
    f .write(str(array))
