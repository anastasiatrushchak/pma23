with open('input.txt', 'r') as file:
    line = file.readline().split()
    a, b = int(line[0]), int(line[1])
N = 100
fibonacci = [a, b]
for i in range(2, N):
    next_number = a + b 
    fibonacci.append(next_number)
    a, b = b, next_number
with open('output.txt', 'w') as output_file:
    output_file.write(f"{fibonacci}")
print(f"{fibonacci}")
