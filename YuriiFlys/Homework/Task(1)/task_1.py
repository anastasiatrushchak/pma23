import constants

def fibonacci_sum_recursive(sequence, limit):
    try:
        if sequence[-1] + sequence[-2] < limit:
            sequence.append(sequence[-1] + sequence[-2])
            return fibonacci_sum_recursive(sequence, limit)
        else:
            return sequence
    except Exception as e:
        print(f"Error occurred in recursive function: {e}")

try:
    with open(constants.INPUT, 'r') as file:
        numbers = file.readline().split()
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
except Exception as e:
    print(f"Error reading file {constants.INPUT}: {e}")

try:
    with open(constants.NUMBER, 'r') as file:
        number = int(file.readline())
except Exception as e:
    print(f"Error reading file {constants.NUMBER}: {e}")

for num in fibonacci_sum_recursive(numbers, number):
    print(num, end=' ')

try:
    with open(constants.OUTPUT, 'w') as f:
        f.write("Result:\n ")
        for num in fibonacci_sum_recursive(numbers, number):
            f.write(str(num) + ' ')
except Exception as e:
    print(f"Error writing to file {constants.OUTPUT}: {e}")
