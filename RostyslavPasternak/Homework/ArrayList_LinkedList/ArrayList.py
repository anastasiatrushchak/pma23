
class ArrayList:
    def __init__(self, size=10):
        self.array = [None] * size
        self.size = size
    def add(self,new_element):
        if isinstance(new_element, list | tuple | set):
            for element in new_element:
                self.add(element)
        else:
            if new_element != None:
                ...

    def __increase_size(self):
        temp = self.array
        self.size = 1.5 * self.size + 1
        self.array = [None] * int(self.size)
        self.add(temp)



list = list()

print(list.size)
