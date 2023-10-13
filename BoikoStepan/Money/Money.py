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


n = int(input("Введіть місткість скарбнички: "))
m = int(input("Скільки монет поклали в скарбничку: "))
k = int(input("Кількість монет, які хочуть покласти в скарбничку: "))

money_box = MoneyBox(n)
money_box.add(m)
print(money_box.can_add(k))
