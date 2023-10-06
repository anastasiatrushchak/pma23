class ArrayList:
    def __init__(self):
        self.__list = [None]
        self.__capacity = 1

    def __len__(self):
        return len(self.__list) - self.__list.count(None)

    def __getitem__(self, index):
        return self.__list[index]

    def __setitem__(self, key, value):
        self.__list[key] = value

    def __str__(self):
        return (str(self.__list) +
                '\nSize: ' + str(len(self)) +
                '\nCapacity: ' + str(self.__capacity) +
                '\n')

    def __check_size(self):
        for i in self.__list:
            if i is None:
                return True
            else:
                continue
        return False

    def __increase_size(self):
        delta = len(self.__list)
        self.__capacity = int(len(self.__list) * 1.5) + 1
        delta = self.__capacity - delta
        for i in range(delta):
            self.__list.append(None)

    def append(self, item):
        if self.__check_size() is True:
            for i in range(self.__capacity):
                if self.__list[i] is None:
                    self.__list[i] = item
                    break
        else:
            self.__increase_size()
            for i in range(self.__capacity):
                if self.__list[i] is None:
                    self.__list[i] = item
                    break

    def remove(self, index):
        try:
            if index < 0 or index > len(self):
                raise IndexError
            else:
                del self.__list[index]
                self.__capacity -= 1
        except IndexError:
            print("Wrong index to delete!")

    def add_item(self, index, item):
        try:
            if index < 0:
                raise IndexError
            elif index > self.__capacity:
                while self.__capacity < index:
                    self.__increase_size()
                self.__list.insert(index, item)
            else:
                self.__list.insert(index, item)
        except IndexError:
            print("Wrong index to insert the item!")

    def capacity(self):
        return self.__capacity


a = ArrayList()
a[0] = 'a'
print(a)
a.append('b')
print(a)
a.append('b')
print(a)
a.remove(2)
print(a)
a.add_item(9, '6')
print(a)
