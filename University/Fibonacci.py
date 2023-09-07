CONSTANTAA = 'input.txt'
with open(CONSTANTAA, 'r') as f:
    array = f.read().split()

array = [float(i) for i in array if i.isdigit()]

for i in range(2, 10):
    array.append((array[i-1]) + (array[i-2]))

CONST = 'output.txt'
with open (CONST, 'w') as file:
    file.write(str(array))