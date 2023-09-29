import os
import exceptions as exc


class Fibonacci:
    def __init__(self):
        self.input_numbers = []
        self.stop_number = 0.0

    def load_info(self, start_data, stop_data):
        try:
            if os.path.exists(start_data) and os.path.exists(stop_data):
                with open(start_data, "r") as inputStart:
                    if os.path.getsize(start_data) == 0:
                        raise exc.EmptyFile("File is empty!")
                    self.input_numbers = [float(number) for line in inputStart for number in line.split(",") if
                                          number.isdigit()]

                with open(stop_data, "r") as inputStop:
                    if os.path.getsize(stop_data) == 0:
                        raise exc.EmptyFile("File is empty!")
                    self.stop_number = inputStop.readline()
                    if self.stop_number.isdigit():
                        self.stop_number = float(self.stop_number)
            else:
                raise exc.FileDoesntExist("No input file was found!")
        except exc.FileDoesntExist as FDE:
            print(FDE)
            raise SystemExit
        except exc.EmptyFile as EF:
            print(EF)
            raise SystemExit

    def count_row(self, sequence=None):
        if sequence is None:
            sequence = self.input_numbers.copy()

        last_number = sequence[-1]
        if last_number >= self.stop_number:
            return sequence
        else:
            lam = lambda seq: seq[-2] + seq[-1]
            next_number = lam(sequence)
            sequence.append(next_number)
            return self.count_row(sequence)

    def save(self, result):
        with open("fibonacci_output.txt", "w") as writeResult:
            writeResult.write(str(result))



a = Fibonacci()
a.load_info("fibonachi2.txt", "stopnnumber.txt")
b = a.count_row()
a.save(b)
