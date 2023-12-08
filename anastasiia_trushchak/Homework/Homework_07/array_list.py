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
        try:
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
            else:
                raise ValueError("Value not found in the list")

        except ValueError as e:
            print(f"Error: {e}")

    def clear(self):
        try:
            if len(self.array) == 0:
                print("The list is already empty")
                return

            self.array = []
        except Exception as e:
            print(f"Error: {e}")

    def insert(self, index, value):
        try:
            if index < 0 or index > len(self.array):
                raise IndexError("Index out of bounds")

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

        except IndexError as e:
            print(f"Error: {e}")


l = ArrayList([])
#l.append(5)
#l.append(7)
print(l.array)
# l.append('5')
l.remove(1)
#l.insert(10, 9)
#print(l.array)
l.clear()
print(l.array)