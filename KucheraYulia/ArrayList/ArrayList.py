class ArrayList:
    def __init__(self, array: list = []):
        self.size = 1.5*len(array)+1
        self.array = array

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

    def insert(self, index, value):
        if index < 0 or index > len(self.array):
            print("problem index")
            return

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


masiv = ArrayList([21, 74, 4, 19, 109, 69, 14, 88, 52, 25])
masiv.append(5)
masiv.append(7)
masiv.insert(100, 9)
print(masiv.array)
masiv.clear()
print(masiv.array)
