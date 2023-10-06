def read_initial_conditions():
    with open('input.txt', 'r') as file:
        initial_conditions = file.read().split()
        return int(initial_conditions[0]), int(initial_conditions[1])

def read_steps():
    with open('steps.txt', 'r') as file:
        return int(file.read())

def write_fibonacci_sequence(sequence):
    with open('output.txt', 'w') as file:
        for num in sequence:
            file.write(str(num) + '\n')

def fibonacci(n, initial_conditions):
    fib_sequence = list(initial_conditions)
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Читання початкових умов
initial_conditions = read_initial_conditions()
n = read_steps()

# Генерація ряду Фібоначі
result = fibonacci(n, initial_conditions)

# Запис результату у файл
write_fibonacci_sequence(result)

# Виведення результату на екран
print(result)
