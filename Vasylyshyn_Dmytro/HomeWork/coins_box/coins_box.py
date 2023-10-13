class MoneyBox:
    def __init__(self, capacity):
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")
        self.capacity = capacity
        self.coins = 0

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

    box = MoneyBox(n)

    if m > n:
        raise ValueError("Кількість монет вже в скарбничці більша, ніж її місткість")

    if box.can_add(k):
        box.add(k)
        print("True")
    else:
        print("False")

except ValueError as e:
    print(f"Помилка: {e}")
except KeyboardInterrupt:
    print("\nВведення перервано користувачем.")
