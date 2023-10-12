INDEX_ERROR = 'Index error'
class ArrayList:
    def __init__(self):
        self.list = []
        self.size = 0

    def is_empty(self):
        return len(self.list) == 0

    def increase_size(self):
        try:
            size = len(self.list)
            new_size = int(1.5 * size + 1)
            new_list = [] * new_size
            for i in range(size):
                new_list[i] = self.list[i]
            self.list = new_list
        except IndexError:
                print(INDEX_ERROR)
                exit(-1)

    def push(self, elem):
        if len(self.list) == self.size:
            self.increase_size()
            self.list.append(elem)
        else:
            self.list.append(elem)

    def pop(self):
        if self.is_empty():
            return "Array is empty"
        else:
            try:
                self.list = self.list[:-1]
            except IndexError:
                print(INDEX_ERROR)
                exit(-1)

    def __str__(self):
        return str(self.list)







