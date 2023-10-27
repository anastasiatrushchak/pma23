class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.coins += v

n = int(input("Введіть місткість скарбнички: "))
m = int(input("Скільки разів клали в скарбничку: "))

money_box = MoneyBox(n)
money_box.add(m)

for i in range(m):
    k = int(input("Введіть кількість монет, які хочуть покласти в скарбничку: "))
    if money_box.can_add(k):
        money_box.add(k)
        print("True")
    else:
        print("False")