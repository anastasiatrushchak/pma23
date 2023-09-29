from pyxtension.streams import stream
class MyClass:
    def __init__(self, value):
        self.value = value

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

my_list = (MyClass(1), MyClass(2), MyClass(3), MyClass(4), MyClass(5))
print("Original list:")

for item in my_list:
    print(item.get_value())

my_stream = (stream(my_list)
             .map(lambda x: x.get_value() * 2)
             .filter(lambda x: x>=5)
             .toList())
print("Filtered list:")

for item in my_stream:
    print(item)
