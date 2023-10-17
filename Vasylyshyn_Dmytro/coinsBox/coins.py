class MoneyBox:
    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self.capacity = capacity
        self.coins = 0
#k
    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.coins += v
        else:
            raise ValueError("Cannot add more coins, capacity exceeded")

try:
    n = int(input("Введіть місткість скарбнички: "))
    m = int(input("Скільки монет вже в скарбничці: "))
    k = int(input("Скільки монет ви хочете додати: "))

    if k < 0 or m<0 or n<0:
        raise ValueError("Кількість монет не може бути від'ємною")

    box = MoneyBox(n)

    if  m + k > n:
        print("False")
    else:
        box.add(k)
        print("True")

except ValueError as e:
    print(f"Помилка: {e}")
