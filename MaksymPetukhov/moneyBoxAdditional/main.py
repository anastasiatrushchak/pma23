import constants
import os


class FileIsEmpty(Exception):

    def __init__(self, message="File is empty!"):
        self.message = message
        super().__init__(self.message)


class MoneyBox:

    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0

    def can_add(self, v):
        if self.capacity >= v:
            return True
        return False

    def add(self, v):
        if self.can_add(v):
            self.current += v
            return True
        else:
            return False


try:
    with open(constants.INPUT_FILE, 'r') as file:
        if os.path.getsize(constants.INPUT_FILE) == 0:
            raise FileIsEmpty
        lines = file.readlines()
        capacity = int(lines[0])
        already_in_moneybox = int(lines[1])
        add_to_moneybox = int(lines[2])
        print(capacity, already_in_moneybox, add_to_moneybox)
        moneybox = MoneyBox(capacity)
        if not moneybox.add(already_in_moneybox):
            print("False")
        if moneybox.add(add_to_moneybox):
            print("True")
        else:
            print("False")


except FileNotFoundError as e:
    print(e)
except FileIsEmpty as e:
    print(e)
