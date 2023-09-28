# Зчитуємо вхідні дані з файлів

with open('input.txt', 'r') as input_file:
    input_data = input_file.read().split(',')
    print(input_data)
    
    
with open('steps.txt', 'r') as steps_file:
    num_steps = int(steps_file.read())

# Просимо  вхідні дані
first_number, second_number = map(int, input_data)
fibonacci_sequence = [first_number, second_number]

# Генеруємо ряд Фібоначі
while len(fibonacci_sequence) < num_steps:
    next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    fibonacci_sequence.append(next_number)

# Записуємо результат у вихідний файл
with open('output.txt', 'w') as output_file:
    output_file.write(','.join(map(str, fibonacci_sequence)))

# Виводимо результат у консоль
print(','.join(map(str, fibonacci_sequence)))
