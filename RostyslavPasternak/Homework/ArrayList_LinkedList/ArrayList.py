class ArrayList:
    def __init__(self, size=10):
        self.array = [None] * size
        self.size = size
        self.capacity = 0
    @classmethod
    def from_list(cls, arr):
        instance = cls()
        instance.add(arr)
        return instance
    @classmethod
    def from_file(cls,file_name,separator=" "):
        with open(file_name, 'r') as readFile:
            line = readFile.readline()

        array = line.split(separator)
        array = [int(i) for i in array if i.isdigit()]
        return ArrayList.from_list(array)

    def add(self,new_element):
        if isinstance(new_element, list):
            for element in new_element:
                self.add(element)
        else:
            if new_element != None:
                self.__increase_size()
                self.array[self.capacity] = new_element
                self.capacity += 1

    def __increase_size(self):
        if self.size == self.capacity:
            temp = self.array
            self.size = int(1.5 * self.size + 1)
            self.array = [None] * int(self.size)
            self.capacity = 0
            self.add(temp)
    def remove_by_index(self,index):
        self.array.pop(index)
        self.capacity -= 1
    def add_by_index(self, index, new_element):
        self.array.insert(index, new_element)
        self.capacity += 1
        self.__increase_size()
    def delete(self):
        self.array = []
        self.size = 0
        self.capacity = 0

    def __str__(self):
        return str(self.array[0:self.capacity])



list1 = ArrayList.from_file("array.txt")
print(f"Size: {list1.size}")
print(f"Capacity: {list1.capacity}")
print(f"Array: {list1}")

print("<--------------------------------Create Array------------------------>")
list1 = ArrayList.from_list([0,1,2,3,4,5,6,7,8,9])
print(f"Size: {list1.size}")
print(f"Capacity: {list1.capacity}")
print(f"Array: {list1}")

print("<--------------------------------Add New Elements------------------------>")
list1.add(10)
print(f"Size: {list1.size}")
print(f"Capacity: {list1.capacity}")
print(f"Array: {list1}")

print("----")
list1.add([11,12,13,14,15,16])
print(f"Size: {list1.size}")
print(f"Capacity: {list1.capacity}")
print(f"Array: {list1}")

print("<--------------------------------Remove By index------------------------>")
list1.remove_by_index(6)
print(f"Size: {list1.size}")
print(f"Capacity: {list1.capacity}")
print(f"Array: {list1}")

print("<--------------------------------Add by index------------------------>")
list1.add_by_index(6,222222)
print(f"Size: {list1.size}")
print(f"Capacity: {list1.capacity}")
print(f"Array: {list1}")

print("<--------------------------------Delete Array------------------------>")
list1.delete()
print(f"Size: {list1.size}")
print(f"Capacity: {list1.capacity}")
print(f"Array: {list1}")

print("<--------------------------------Add new element------------------------>")

list1.add(12)
print(f"Size: {list1.size}")
print(f"Capacity: {list1.capacity}")
print(f"Array: {list1}")

