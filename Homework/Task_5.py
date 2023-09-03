class Vector:
    def __init__(self, vector):
        self.vector = vector
    def __add__(self, other):
        sum=[]
        for i in range( min( len(self.vector), len(other.vector))):
            sum.append(self.vector[i]+other.vector[i])
        return sum
    def __sub__(self, other):
        difference = []
        for i in range( min( len(self.vector), len(other.vector))):
            difference.append(self.vector[i]-other.vector[i])
        return difference
    def __mul__(self, other):
        multipliation = []
        for i in range( min( len(self.vector), len(other.vector))):
            multipliation.append(self.vector[i]*other.vector[i])
        return multipliation
    def __truediv__(self, other):
        divide=[]
        for i in range( min( len(self.vector), len(other.vector))):
            divide.append(self.vector[i]/other.vector[i])
        return divide
list1 = Vector([1, 2, 3, 4])
list2 = Vector([1, 2, 3, 4])

print("Сума:")
print(list1+list2)

print("Різниця:")
print(list1-list2)

print("Ділення:")
print(list1/list2)

print("Множення:")
print(list1*list2)