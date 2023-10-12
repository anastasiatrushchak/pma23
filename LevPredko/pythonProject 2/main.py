'''
from datetime import date

print("Hello world")

print(3 + 4)
print(3 * 5)
print(3 ** 2)


name = input("Put your name there: ")
print("Hi,", name, ",nice to meet you:)")


first = input("first: ")
second = input("second: ")
print("first type:", type(first))
print("second type:", type(second))
first = int(first)
second = int(second)
print("first type:", type(first))
print("second type:", type(second))
print(first, second)
print(first + second)
print(first - second)
print(first * second)
print(first / second)
print(first ** second)

first = int(input("first: "))
second = int(input("second: "))
print("first:", first, "\nsecond:", second)
if (first > second):
    print(first)
else:
    print(second)
print(first if first > second else second)

number = float(input("number: "))
cycleBorder = int(input("border: "))
iterator = 0
while (iterator < cycleBorder):
     number = number * 3
     iterator += 1
     print(number.__str__())

matrix = []
length = int(input("Enter number of elements : "))
for rowIterator in range(0, length):
     row = []
     for columnIterator in range(0, length):
         element = int(input())
         row.append(element)
     matrix.append(row)

print(matrix)
file = open("test.txt")
print(file.read())

file = open("test.txt")
print(file.read(5))

file = open("test.txt")
print(file.readline())

file = open("demofile.txt", "w")
file.write("Now the file has more content!")
 file.close()

 file = open("demofile.txt", "r")
 print(file.read())


 class Student:
     def __init__(self, name, age):
         self.name = name
         self.age = age

     @classmethod
     def calculate_age(cls, name, birth_year):
         return cls(name, date.today().year - birth_year)

     def show(self):
         print(self.name + "'s age is: " + str(self.age))

 jessa = Student('Jessa', 20)
 jessa.show()

 joy = Student.calculate_age("Joy", 1995)
 joy.show()

 function = lambda x, y: x + y
 print(function(1, 2))

 def add(a, b, c=2):
     return a + b + c

 print(add(1, 2, 3))
 print(add(1, 2))


 try:
     number = 1 / 0
 except ZeroDivisionError:
     number = 0
     print(number)
'''



