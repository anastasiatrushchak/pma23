class MoneyBox:
    def __init__(self, capacity):
        try:
            if capacity <= 0:
                raise ValueError
            self.capacity = capacity
            self.coins = 0
        except ValueError:
            print("Місткість скарбнички повинна бути більше 0")


    def can_add(self, v):
        try:
            if v <= 0:
                raise ValueError
        except ValueError:
            print("Кількість монет для додавання повинна бути більше 0")
        return self.coins + v <= self.capacity

    def add(self, v):
        try:
            if self.can_add(v)==False:
                raise ValueError
            self.coins += v
            return True
        except ValueError:
            print("Неможливо додати цю кількість монет до скарбнички")


try:
    n = int(input("Введіть місткість скарбнички: "))
    if n<0:
        raise ValueError

    box = MoneyBox(n)
except ValueError:
    print("Місткість має бути додатнім цілим числом")
    exit(-1)
try:
    m = int(input("Скільки монет поклали в скарбничку: "))
    if m < 0:
        raise ValueError
    box.coins = m
except ValueError:
    print("Кількість монет повинна бути не від'ємною")
try:
    k = int(input("Скільки монет хочуть покласти в скарбничку: "))
    if k < 0:
        raise ValueError
except ValueError:
    print("Кількість монет для додавання повинна бути не від'ємною")

if box.can_add(k)==True:
    box.add(k)
    print(True)
else:
    print(False)
