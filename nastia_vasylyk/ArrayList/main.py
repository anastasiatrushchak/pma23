class ArrayList:
    def __init__(self, array:list=[]):
        self.size = 1.5*len(array)+1
        self.array =array


    def append(self, el):
        if len(self.array) < self.size:

            self.array.append(el)

        else:
            self.size = int(self.size * 1.5 + 1)
            temp = self.array.copy()

            self.array = []
            for i in temp:
                self.array.append(i)
            self.array.append(el)

    def remove(self, value):
        index = -1

        for i in range(len(self.array)):
            if self.array[i] == value:
                index = i
                break
        if index != -1:
            for i in range(index, len(self.array) - 1):
                self.array[i] = self.array[i + 1]

            self.array = self.array[:-1].copy()
        return index

    def clear(self):
        self.array = []

    def insert(self, index, value):  # вставлення
        if len(self.array) < self.size:

            self.array.append(0)
            for i in range(len(self.array) - 1, index, -1):
                self.array[i] = self.array[i - 1]
            self.array[index] = value

        else:
            self.size = int(self.size * 1.5 + 1)
            temp = self.array.copy()

            self.array = []
            for i in temp:
                self.array.append(i)
            self.array.append(0)
            for i in range(len(self.array) - 1, index, -1):
                self.array[i + 1] = self.array[i]
            self.array[index] = value


l = ArrayList([4, 5, 6, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 63, 4, 6, 3, 242, 24, 5, 4])
l.append(5)
l.append(7)
# print(l.array)
# l.append('5')
l.remove(5)
l.insert(1, 9)
print(l.array)
l.clear()
# print(l.array)
