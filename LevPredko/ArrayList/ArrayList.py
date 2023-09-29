import Constants


class ArrayList:

    def __init__(self):
        self.array = []

    def read_from_file(self, filename, use_comma=True):
        with open(filename, 'r') as file:
            line = file.readline()
            if use_comma:
                self.array = line.strip().split(',')
            else:
                self.array = line.strip().split()

    def add(self, item):
        self.array.append(item)

    def remove(self, item):
        if item in self.array:
            self.array.remove(item)

    def insert(self, index, item):
        self.array.insert(index, item)

    def clear(self):
        self.array = []

    def __str__(self):
        return ', '.join(map(str, self.array))


my_list = ArrayList()

my_list.read_from_file(Constants.ARRAYLISTFILE)

my_list.add(1)
my_list.add(2)
my_list.add(3)
print(my_list)

my_list.remove(2)
print(my_list)

my_list.insert(1, 10)
print(my_list)

my_list.clear()
print(my_list)