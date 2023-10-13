class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.coins += v
            return True
        else:
            return False

n = int(input("Enter the capacity of the money box: "))
m = int(input("Enter the initial number of coins in the money box: "))

box = MoneyBox(n)
box.coins = m

k = int(input("Enter the number of coins to add to the money box: "))

result = box.add(k)
print(result)
