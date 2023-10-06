import os
def file_exists(filename):
    if os.path.isfile(filename):
        print("Файл існує.")
        with open(filename, 'r') as file:
            if file.read() == "":
                print("Файл порожній.")
            else:
                print("Файл не порожній.")
    else:
        print("Файл не існує.")
file_exists("input.txt")
file_exists("steps.txt")
file_exists("output.txt")
def next_fibonacci(a, b, max_value, fibonacci_numbers):
    if a >= max_value:
        return
    fibonacci_numbers.append(str(a))
    next_fibonacci(b, a + b, max_value, fibonacci_numbers)

with open('input.txt', 'r') as input_file:
    n, m = map(lambda x: int(x), input_file.readline().split())

with open('steps.txt', 'r') as steps_file:
    max_value = int(steps_file.readline())

fibonacci_numbers = []
next_fibonacci(n, m, max_value, fibonacci_numbers)

with open('output.txt', 'w') as output_file:
    output_file.write(' '.join(fibonacci_numbers))

