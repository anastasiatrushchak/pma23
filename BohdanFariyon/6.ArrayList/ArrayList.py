class ArrayList:
    def __init__(self, array=[]):
        self.capacity = len(array)
        self.size = len(array)
        self.data = array


    def add(self, element):
        if self.size >= self.capacity:
            self._resize()
        self.data[self.size] = element
        self.size += 1

    def remove(self, index):
        try:
            if 0 <= index < self.size:
                for i in range(index, self.size - 1):
                    self.data[i] = self.data[i + 1]
                self.data[self.size - 1] = None
                self.size -= 1
            else:
                raise IndexError("Invalid remove index")
        except IndexError as e:
                print(f"Insertion error: {e}")
    def insert(self, index, element):
        if self.size >= self.capacity:
            self._resize()
        try:
            if index < 0 or index > self.size:
                raise IndexError("Invalid insert index")

            for i in range(self.size, index, -1):
                self.data[i] = self.data[i - 1]
            self.data[index] = element
            self.size += 1
        except IndexError as e:
            print(f"Insertion error: {e}")

    def clear(self):
        self.data = [None] * self.capacity
        self.size = 0
    def __len__(self):
        return self.size
    def _resize(self):
        self.capacity = int(1.5 * self.capacity) + 1
        new_data = [None] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def __str__(self):
        return str(self.data[:self.size])


my_list = ArrayList([1,4,4,4,4,4,2,1,23,1,4,23,1,12,3,])
my_list.add(1)
my_list.add(2)
my_list.add(3)
print(my_list)

my_list.insert(12, 4)
print(my_list)

my_list.remove(100)
print(my_list)

print(len(my_list))
my_list.clear()
print(my_list)
