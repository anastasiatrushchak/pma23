first = "file.txt"
second = "output.txt"

with open(first, "r") as file:
    original_file = file.read()
fibonacci = original_file.split()

for i in range(0, 2):
    fibonacci[i] = float(fibonacci[i])

for i in range(2, 10):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])

with open(second, "w") as new:
    new.write(str(fibonacci))
