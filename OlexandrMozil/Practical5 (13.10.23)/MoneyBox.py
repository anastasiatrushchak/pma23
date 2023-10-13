class MoneyBox:
    def __init__(self, capacity):
        try:
            if capacity > 0:
                self.__capacity = capacity
            else:
                raise PermissionError
        except PermissionError:
            print("Can't make such money box!")
            quit(9)
        self.__coins_counter = 0

    def can_add(self, v):
        return self.__coins_counter + v < self.__capacity

    def add(self, v):
        try:
            if self.can_add(v):
                self.__coins_counter += v
            else:
                raise InterruptedError
        except InterruptedError:
            print(f"Not enough space in money box! Can't add {v} coins.")


n = int(input("Input capacity: "))
m = int(input("How many coins put into the money box: "))
k = int(input("How many coins are you trying to put more: "))
mb = MoneyBox(n)
mb.add(m)
print(mb.can_add(k))
