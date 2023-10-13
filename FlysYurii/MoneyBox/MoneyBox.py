class MoneyBox:
    def __init__(self, capacity):
        if isinstance(capacity, int) and capacity >= 0:
            self.capacity = capacity
        else:
            raise ValueError("Місткість повинна бути не від'ємним цілим числом.")
        self.coins = 0

    def can_add(self, coin):
        if isinstance(coin, int) and coin >= 0:
            return self.coins + coin <= self.capacity
        else:
            raise ValueError("Кількість монет повинна бути не від'ємним цілим числом.")

    def add(self, coin):
        if self.can_add(coin):
            self.coins += coin
        else:
            raise ValueError("Не можна додати більше монет, ніж дозволяє місткість.")


try:
    n = int(input("Введіть місткість скарбниці:"))
    m = int(input("Введіть кількість монет, які ми додаємо в скарбницю:"))
    k = int(input("Введіть кількість монет, яку ви хочете ще додати:"))

except ValueError:
    print("Введіть коректні дані.")

else:
    try:
        box = MoneyBox(n)
        box.add(m)
        print(box.can_add(k))
    except ValueError as e:
        print(e)
