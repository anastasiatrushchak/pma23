import constants

class Fibonacci:
    def __init__(self, sequence, limit):
        self.sequence = sequence
        self.limit = limit

    def fibonacci_sum_recursive(self, sequence=None):
        fibonacci_sum = lambda seq: seq if (int(seq[-1]) + int(seq[-2]) > self.limit) else \
            self.fibonacci_sum_recursive(seq + [int(seq[-1]) + int(seq[-2])])

        if sequence is None:
            sequence = self.sequence

        return fibonacci_sum(sequence)
number = None

try:
    with open(constants.INPUT, 'r') as file:
        numbers = file.readline().split()
        for i in range(len(numbers)):
            try:
                numbers[i] = int(numbers[i])
            except ValueError:
                print(f"Invalid integer format in {constants.INPUT}: {numbers[i]}")
                exit(1)
except Exception as e:
    print(f"Error reading file {constants.INPUT}: {e}")
    exit(1)

try:
    with open(constants.NUMBER, 'r') as file:
        number = file.readline()
        try:
            number = int(number)
        except ValueError:
            print(f"Invalid integer format in {constants.NUMBER}: {number}")
            exit(1)
except Exception as e:
    print(f"Error reading file {constants.NUMBER}: {e}")
    exit(1)

for num in Fibonacci(numbers, number).fibonacci_sum_recursive():
    print(num, end=' ')

try:
    with open(constants.OUTPUT, 'w') as f:
        f.write("Result:\n ")
        for num in Fibonacci(numbers, number).fibonacci_sum_recursive():
            f.write(str(num) + ' ')
except Exception as e:
    print(f"Error writing to file {constants.OUTPUT}: {e}")
    exit(1)


