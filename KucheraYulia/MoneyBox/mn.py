class MoneyBox:
    def __init__(self, capacity):
        # Конструктор з аргументом - місткість скарбнички
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        # True, якщо можна додати v монет, False інакше
        return self.coins + v <= self.capacity

    def add(self, v):
        # Покласти v монет в скарбничку
        if self.can_add(v):
            self.coins += v

# Введення даних від користувача
n = int(input("Введіть місткість скарбнички: "))
m = int(input("Скільки разів клали в скарбничку: "))

# Створення об'єкта MoneyBox
money_box = MoneyBox(n)
money_box.add(m)

# Додавання монет в скарбничку
for i in range(m):
    k = int(input("Введіть кількість монет, які хочуть покласти в скарбничку: "))
    if money_box.can_add(k):
        money_box.add(k)
        print("True")
    else:
        print("False")