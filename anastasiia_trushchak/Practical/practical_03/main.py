class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins_inside = 0

    def can_add(self, v):
        return self.coins_inside + v <= self.capacity

    def add(self, v):
        if self.can_add(v):
            self.coins_inside += v


try:
    n = int(input("Введіть місткість скарбнички: "))
    if n < 0:
        raise ValueError("Місткість скарбнички не може бути від'ємною")

    m = int(input("Скільки монет поклали в скарбничку: "))
    if m < 0:
        raise ValueError("Кількість монет, яку поклали, не може бути від'ємною")

    k = int(input("Кількість монет, які хочуть покласти в скарбничку: "))
    if k < 0:
        raise ValueError("Кількість монет для додавання не може бути від'ємною")

    money_box = MoneyBox(n)
    money_box.add(m)
    print("Кількість монет у скарбничці після додавання:", money_box.coins_inside)
    print("Можна додати ще монет:", money_box.can_add(k))

except ValueError as ve:
    print("Помилка:", str(ve))
except FileNotFoundError:
    print("Файл не знайдено.")
except Exception as e:
    print("Виникла невідома помилка:", str(e))
