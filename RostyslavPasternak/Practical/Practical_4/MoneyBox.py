class CountError(Exception):
    def __init__(self):
        super().__init__("Count Error")
class MoneyBox:
    def __init__(self, count=0, max=50):
        self.__capacity = max
        self.count = 0
        self.add(count)
    def can_add(self, new_coin):
        if (self.count + new_coin) > self.__capacity or new_coin < 0:
            return False
        else:
            return True
    def add(self,new_coin=1):
        temp = self.can_add(new_coin)
        if temp:
            self.count += new_coin
        return temp

    def __str__(self):
        return (f"Max: {self.__capacity}\n"
                f"Count: {self.count}\n")

box = MoneyBox()

n = int(input("First number: "))
print(box.add(n))
print(box)

m = int(input("First number: "))
print(box.add(m))
print(box)

k = int(input("First number: "))
print(box.add(k))
print(box)


