class ArrayList:
    def __init__(self):
        self.data = [None]
        self.capacity = 1

    def capacity(self):
        return self.capacity

    def __len__(self):
        count=0
        for i in self.data:
            if i is not None:
                count+=1
        return count

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __str__(self):
        return f'ArrayList: {self.data}, Size: {len(self)}, Capacity: {self.capacity+1}'

    def raise_size(self):
        new_size=self.capacity
        self.capacity = int(1.5 * self.capacity) + 1
        new_size=self.capacity-new_size
        for i in range(new_size):
            self.data.append(None)

    def review_size(self):
        for i in self.data:
            if i is None:
                return True
            else:
                continue
        return False

    def append(self, item):
        if self.review_size() is True:
            for i in range(self.capacity):
                if self.data[i] is None:
                    self.data[i] = item
                    break
        else:
            self.raise_size()
            for i in range(self.capacity):
                if self.data[i] is None:
                    self.data[i] = item
                    break

    def insert(self, index, item):
        try:
            if index < 0:
                raise IndexError
            elif index > self.capacity:
                while self.capacity < index:
                    self.raise_size()
                self.data.insert(index, item)
        except IndexError:
            print("Введіть невід'ємний індекс!")

    def remove(self, index):
        try:
            if index < 0 or index > self.capacity:
                raise IndexError
            else:
                for i in range(index,self.capacity-1):
                    self.data[i]=self.data[i+1]
                self.data.pop()
                self.capacity -= 1
        except IndexError:
            print("Неправильний індекс!")

    def clear(self):
        self.data = [None]
        self.capacity = 1


my_list = ArrayList()
my_list[0] = 'a'
my_list.append('b')
my_list.append('c')
my_list.append('d')
print(my_list)
my_list.insert(12, 'd')
my_list.remove(1)
print(my_list)
my_list.remove(23)
print(my_list)
my_list.clear()
print(my_list)