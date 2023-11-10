class ArrayList:
    def __init__(self):
        self.DEFAULT_CAPACITY = 10
        self.array = [None] * self.DEFAULT_CAPACITY
        self.size = 0

    def add(self, element):
        self.ensure_capacity()
        self.array[self.size] = element
        self.size += 1

    def remove(self, index):
        try:
            if index < 0 or index >= self.size:
                raise IndexError("Index out of bounds")

            del self.array[index]
            self.size -= 1
        except IndexError as e:
            print(f"Error: {e}")

    def insert(self, index, element):
        try:
            if index < 0 or index > self.size:
                raise IndexError("Index out of bounds")

            self.ensure_capacity()
            self.array.insert(index, element)
            self.size += 1
        except IndexError as e:
            print(f"Error: {e}")

    def clear(self):
        self.array = [None] * self.DEFAULT_CAPACITY
        self.size = 0

    def ensure_capacity(self):
        if self.size == len(self.array):
            new_capacity = int(1.5 * len(self.array)) + 1
            self.array = self.array + [None] * (new_capacity - len(self.array))

    def print_list(self):
        print(" ".join(str(elem) for elem in self.array[:self.size]))


array_list = ArrayList()
array_list.add(1)
array_list.add(2)
array_list.add(3)

print("Original ArrayList:")
array_list.print_list()

array_list.remove(1)

print("\nArrayList after removing element at index 1:")
array_list.print_list()

array_list.insert(10, 5)

print("\nArrayList after attempting to insert at an invalid index:")
array_list.print_list()

array_list.clear()

print("\nArrayList after clearing:")
array_list.print_list()
