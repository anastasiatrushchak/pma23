class ArrayList:
    def __init__(self):
        self.capacity = 1
        self.data = [None] * self.capacity
        self.length = 0

    def _resize(self):
        new_capacity = int(1.5 * self.capacity) + 1
        new_data = [None] * new_capacity
        for i in range(self.length):
            new_data[i] = self.data[i]
        self.data = new_data
        self.capacity = new_capacity

    def append(self, value):
        if self.length == self.capacity:
            self._resize()
        self.data[self.length] = value
        self.length += 1

    def get(self, index):
        if 0 <= index < self.length:
            return self.data[index]
        else:
            raise IndexError("Index out of bounds")

    def remove(self, value):
        new_data = [None] * self.capacity
        j = 0
        for i in range(self.length):
            if self.data[i] != value:
                new_data[j] = self.data[i]
                j += 1
        self.data = new_data
        self.length = j
        if self.length < self.capacity // 2:
            self._resize()

    def insert(self, index, value):
        if self.length == self.capacity:
            self._resize()
        for i in range(self.length, index, -1):
            self.data[i] = self.data[i-1]
        self.data[index] = value
        self.length += 1

    def clear(self):
        self.data = [None] * self.capacity
        self.length = 0

    def __str__(self):
        if self.data is not None:
            return str(self.data[:self.length])
        else:
            return "[]"
