INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"
NUMBER = 'number.txt'

class Fibonachi:
    def __init__(self):
        self.two_number = []
        self.number = 0

    def fibonachi_append(self, list_fibonachi = []):
        len_list = len(list_fibonachi)

        if len_list < 2:
            next_number = float(self.two_number[0]) + float(self.two_number[1]) if len_list == 0 else float(list_fibonachi[0]) + float(self.two_number[1])
        else:
            next_number = float(list_fibonachi[-1]) + float(list_fibonachi[-2])

        if next_number <= self.number:
            list_fibonachi.append(next_number)
            return self.fibonachi_append(list_fibonachi)
        else:
            return list_fibonachi

    def read(self):
        try:
            with open(INPUT_FILE, "r") as file:
                fibonacci_numbers = list(map(lambda x: float(x), file.read().split()))
                if len(fibonacci_numbers) < 2:
                    raise ValueError("There should be at least two numbers in the file")
                self.two_number = fibonacci_numbers

        except FileNotFoundError:
            print('File ' + INPUT_FILE + ' not found')
            exit(-1)
        except ValueError as e:
            print(str(e))
            exit(-1)

        try:
            with open(NUMBER, "r") as file:
                self.number = float(file.read())
        except FileNotFoundError:
            print('File ' + NUMBER + ' not found')
            exit(-1)
        except ValueError:
            print("There is no valid number in the file " + NUMBER)
            exit(-1)

obj = Fibonachi()
obj.read()
result = obj.fibonachi_append()
print(result)
