from pyxtension.streams import stream


class Numbers:
    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value


first_list = [Numbers(i) for i in range(10)]
print("First list:")

for item in first_list:
    print(item.get_value())

second_list = (stream(first_list)
               .map(lambda x: x.get_value() * -1)
               .filter(lambda x: x <= 10)
               .toList())
print("Second list:")
for item in second_list:
    print(item)
