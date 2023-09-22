import Constants

class FibonacciCalculator:
    def __init__(self):
        self.numbers = []
        self.final_number = 0
        self.result_sequence = []

    def fibonacci_recursive(self, current_sequence):
        try:
            if len(current_sequence) < 2:
                current_sequence.append(0)
                return self.fibonacci_recursive(current_sequence)
            elif current_sequence[-1] + current_sequence[-2] < self.final_number:
                current_sequence.append(current_sequence[-1] + current_sequence[-2])
                return self.fibonacci_recursive(current_sequence)
            else:
                return current_sequence[2:]
        except Exception as e:
            print(f"Error occurred in recursive function: {e}")

    def read_input_files(self):
        try:
            with open(Constants.Fibonacci, 'r') as file:
                numbers = file.readline().split()
                for i in range(len(numbers)):
                    self.numbers.append(int(numbers[i]))
        except EOFError as e:
            print("Error: Empty file", e)
            return False
        except FileNotFoundError as e:
            print("Error: One or more files not found.", e)
            return False
        try:
            with open(Constants.Final_Fibonacci, 'r') as file:
                self.final_number = int(file.readline())
        except ValueError as e:
            print("Error: Different sizes are specified in the file", e)
        except EOFError as e:
            print("Error: Empty file", e)

        return True

    def calculate_fibonacci_sequence(self):
        self.result_sequence = self.fibonacci_recursive(self.numbers.copy())

    def write_result_to_file(self):
        try:
            with open(Constants.output, 'w') as f:
                f.write("Result:\n")
                for num in self.result_sequence:
                    f.write(str(num) + ' ')
        except ValueError as e:
            print("Error: Different sizes are specified in the file", e)
        except EOFError as e:
            print("Error: Empty file", e)

    def run(self):
        if self.read_input_files():
            self.calculate_fibonacci_sequence()
            self.write_result_to_file()


calculator = FibonacciCalculator()
calculator.run()
b = " "
