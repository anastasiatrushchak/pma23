
class MoneyBox:
    def __init__(self, capacity=0, max=50):
        self.__max = max
        self.capacity = 0
        self.add(capacity)
    def add(self,new_coin=1):
        if (self.capacity + new_coin) > self.__max or (self.capacity + new_coin) < self.capacity:
            return False
        else:
            self.capacity += new_coin
            return True
    def __str__(self):
        return (f"Max: {self.__max}\n"
                f"Capacity: {self.capacity}\n")

box = MoneyBox(capacity=10)
print(box)

print(box.add(90))
print(box)


