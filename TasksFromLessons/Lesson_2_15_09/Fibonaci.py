import copy

class Fibonacci:
    def __init__(self, initial_numbers=None, limit=None):
        self.initial_numbers = initial_numbers
        self.limit = limit

    def fibonacci(self):
        sequence = copy.deepcopy(self.initial_numbers)
        while sequence[-1] + sequence[-2] <= self.limit:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)
        return sequence
