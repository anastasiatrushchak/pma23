class MoneyBox:
    def __init__(self, capacity, coins = 0):
        self.capacity = capacity
        self.coins = 0
        self.add(coins)
    def can_add(self, v):
        if self.capacity >= v + self.coins or v < 0:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.coins += v
            return True
        else:
            return False


n = int(input("Input capacity money box: "))
m = int(input("Enter how many coins were placed in the money box: "))
k = int(input("Enter how many coins you want to put in the money box: "))

money = MoneyBox(n, m)
print(money.add(k))




