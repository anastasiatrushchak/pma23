class ArrayList:
    def __init__(self):
        self.list = []

    def add(self, element):
        self.list.append(element)

    def remove(self, element):
        if element in self.list:
            self.list.remove(element)
        else:
            raise Exception(f"{element} is not in list")

    def insert(self, index, element):
        if 0 <= index <= len(self.list):
            self.list.insert(index, element)
        else:
            raise Exception("Index out of bounds")

    def get(self, index):
        try:
            return self.list[index]
        except IndexError:
            raise IndexError("Index out of bounds")

    def size(self):
        return len(self.list)

    def __str__(self):
        return str(self.list)


