class MoneyBox:
    def __init__(self, capacity):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Місткість скарбнички повинна бути додатнім цілим числом.")
        self.capacity = capacity
        self.coins = 0
    def add(self, v):
        if self.can_add(v):
            self.coins += v
            return True
        else:
            return False
    def can_add(self, v):
        if not isinstance(v, int) or v <= 0:
            raise ValueError("Кількість монет повинна бути додатнім цілим числом.")
        return self.coins + v <= self.capacity
try:
    n = int(input("Введіть місткість скарбнички: "))
    m = int(input("Скільки монет поклали в скарбничку: "))
    k = int(input("Кількість монет, які хочуть покласти в скарбничку: "))

    if m > n:
        print("Неможливо покласти вказану кількість монет. Початкова кількість монет перевищує місткість скарбнички.")
    else:

        box = MoneyBox(n)

        can_add_result = box.can_add(k)

        print(can_add_result)

        if can_add_result:
            add_result = box.add(k)
            print(f"Успішно додано {k} монет до скарбнички. Загальна кількість монет: {box.coins}")
        else:
            print("Неможливо додати вказану кількість монет. Скарбничка переповнена.")

except ValueError as e:
    print(f"error: {e}")
