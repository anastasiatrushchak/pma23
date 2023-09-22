import Constants
class ArrayList:
    def __init__(self, initial_size=10):
        self.array_size = initial_size
        self.my_list = [None] * initial_size
        self.size = 0

    def read_from_file(self, filename):
        with open(filename, "r") as file:
            for line in file:
                value = line.strip()
                self.add(value)

    def resize(self):
        new_size = int(1.5 * self.array_size) + 1
        new_list = [None] * new_size
        for i in range(self.array_size):
            new_list[i] = self.my_list[i]
        self.my_list = new_list
        self.array_size = new_size

    def add(self, value):
        if self.size == self.array_size:
            self.resize()
        self.my_list[self.size] = value
        self.size += 1

    def remove(self, value):
        index = 0
        while index < self.size:
            if self.my_list[index] == value:
                for i in range(index, self.size - 1):
                    self.my_list[i] = self.my_list[i + 1]
                self.my_list[self.size - 1] = None
                self.size -= 1
            else:
                index += 1

    def insert(self, index, value):
        if self.size == self.array_size:
            self.resize()
        for i in range(self.size, index, -1):
            self.my_list[i] = self.my_list[i - 1]
        self.my_list[index] = value
        self.size += 1


    def clear(self):
        self.my_list = self.my_list.copy()
        self.my_list = [None] * self.array_size
        self.size = 0

    def display(self):
        for i in self.my_list[:self.size]:
            if i != None:
                print(i)


my_array_list = ArrayList(10)

my_array_list.read_from_file(Constants.ARRAYLISTFILE)
my_array_list.display()

my_array_list.insert(2,100)
my_array_list.display()







