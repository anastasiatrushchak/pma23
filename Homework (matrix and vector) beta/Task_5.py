import numpy as np
class Vector:
    def __init__(self, vector):
        self.vector = np.array(vector)
    def __add__(self, other):
        try:
            sum=self.vector+other.vector
            return sum
        except:
            return "Неможливо додати вектори"

    def __sub__(self, other):
        try:
            difference=self.vector-other.vector
            return difference
        except:
            return "Неможливо відняти вектори"

    def __mul__(self, other):
        try:
            multipliation=self.vector*other.vector
            return multipliation
        except:
            return "Неможливо відняти вектори"

    def __truediv__(self, other):
        try:
            divide=self.vector/other.vector
            return divide
        except:
            return "Не можливо поділити вектори"
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