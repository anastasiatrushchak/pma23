class ArrayList:
    def __init__(self, arr=[]):
        self.__list = arr
        self.__len = len(arr)
        self.__free_cells = 0

    def __increase_len(self):
        add = int(1.5 * self.__len + 1)
        arr = []
        self.__list += [arr.append(None) for i in range(add)]
        self.__free_cells = add
        self.__len += add

    def push_back(self, element):
        if self.__free_cells == 0:
            self.__increase_len()
        for i in range(self.__len):
            if self.__list[i] == None:
                self.__list[i] = element
                break
        self.__free_cells -= 1

    def print_elements(self):
        print("arr:", self.__list)
        print("len:", self.__len)
        print("free cells:", self.__free_cells)#

    def delete_element(self, index):
        try:
            if index > (self.__len - self.__free_cells):
                raise Exception("Error! Index out of range!")
            if index < 0:
                raise Exception("Error! Wrong value(i<0)")
            del self.__list[index]
            self.__len -= 1
        except Exception as err:
            print(err)

    def add(self, element, index):
        try:
            if index >= self.__len:
                raise Exception("Error! Index out of range")
            if index < 0:
                raise Exception("Error! Wrong value(i<0)")
            self.__list[index] = element
            self.__free_cells = 0
            for i in range(self.__len):
                if self.__list[i] is None:
                    self.__free_cells += 1
            if self.__free_cells == 0:
                self.__increase_len()
        except Exception as err:
            print(err)

    def clear(self, index):
        try:
            if index >= self.__len:
                raise Exception("Error! Index out of range")
            if index < 0:
                raise Exception("Error! Wrong value(i<0)")
            self.__list[index] = None
            self.__free_cells += 1
        except Exception as err:
            print(err)



a = ArrayList([1, 2, 3])
a.push_back(4)
a.print_elements()
a.delete_element(0)
a.print_elements()
a.add(5, 4)
a.print_elements()
a.push_back(6)
a.print_elements()
a.clear(2)
a.print_elements()
