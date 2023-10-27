n = int(input("Введіть місткість вашої скарбнички: "))
m = int(input("Скільки монет поклали в скарбничку: "))
k = int(input("К-сть монет, які хочуть покласти в скарбничку: "))
class MoneyBox:
    def __init__(self, capacity):
        # Конструктор з аргументом - місткість скарбнички
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



money_box = MoneyBox(n)

for _ in range(m):
    if not money_box.add(1):
        print("False")
        break
else:
    for _ in range(k):
        if not money_box.add(1):
            print("False")
            break
    else:
        print("True")
