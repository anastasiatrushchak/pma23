class MoneyBox:
    def __init__(self, capacity):
        if capacity >= 0:
            self.capacity = capacity
        else:
            raise ValueError("Місткість повинна бути не від'ємним числом.")
        self.coins = 0

    def can_add(self, coin):
        if coin >= 0:
            return self.coins + coin <= self.capacity
        else:
            raise ValueError("Кількість монет повинна бути не від'ємним числом.")

    def add(self, coin):
        if self.can_add(coin):
            self.coins += coin
        else:
            raise ValueError("Не можна додати більше монет.")


try:
    n = int(input("Введіть місткість скарбнички: "))
    m = int(input("Скільки монет вже є в скарбничці: "))
    k = int(input("Скільки монет хочете додати: "))

except ValueError:
    print("Дані введені неправильно7"
          ".")
    exit(-1)



try:
    box = MoneyBox(n)
    box.add(m)
    print(box.can_add(k))
except ValueError as e:
    print(e)

