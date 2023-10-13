import constants


class ArrayList:

    def __init__(self, arr=None):
        self.data = arr
        self.capacity = len(self.data)
        self.increase_size()

        if arr is not None:
            for i in range(len(arr)):
                self.data[i] = arr[i]

    def __len__(self):
        return len(self.data) - self.data.count(None)

    def __str__(self):
        return (str(self.data) +
                '\nSize: ' + str(len(self)) +
                '\nCapacity: ' + str(self.capacity) +
                '\n')

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.insert(index, value)

    def increase_size(self):
        self.capacity = int(1.5 * len(self.data)) + 1
        for i in range(self.capacity - len(self.data)):
            self.data.append(None)

    def append(self, value):
        if self.capacity == 0:
            self.capacity = 1
            self.increase_size()
        for i in range(len(self.data)):
            if self.data[i] is None:
                self.data[i] = value
                return True
        self.increase_size()
        self.append(value)

    def delete(self, index):
        try:
            if index < 0 or index >= len(self.data):
                raise IndexError
            del self.data[index]
            self.capacity -= 1
        except IndexError:
            print("There isn't any element with this index")

    def insert(self, index, value):
        try:
            if index < 0:
                raise IndexError
            while index < 0 or index >= len(self.data):
                self.increase_size()
            self.data[index] = value
        except IndexError:
            print("Can't insert element with this index")

    def clear(self):
        self.data = []
        self.capacity = 0


# values = [1, 2, 3, 4, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 32, 45, 7, 6]  # 19
# arrList = ArrayList(values)
# arrList[0] = 'a'
# print(arr)
# a.append('b')
# print(a)
# a.append('b')
# print(a)
# a.erase(2)
# print(a)
# a.insert(9, 6)
# print(a)
# a.insert(100, "Hello")
# print(a)


values = [1, 2, 3, 4, 2, 3, 4, 5, 6, 7, 8, 9, 5, 4, 32, 45, 7, 6]
# alist = ArrayList(['Hello', 1, 4 ,6])
alist = ArrayList(values)
# alist = ArrayList()

# alist.append(13)
# alist.append(21)
# alist.append(18)
# alist.append(29)
# alist.append(31)
# alist.append(78)

# with open(constants.INPUT_FILE, 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         alist.append(int(line))

# values = []
# with open(constants.INPUT_FILE, 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         values.append(int(line))
#
# alist = LinkedList(values)

print(alist)
print("\nAdd element:")
alist.append("bbb")
print(alist)
print("\nDelete element:")
alist.delete(3)
print(alist)
print("\nInsert value:")
alist.insert(3, 6)
print(alist)
print("\nClear list:")
alist.clear()
print(alist)
