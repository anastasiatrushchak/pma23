import Exception


class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, x):
        return self.coins + x <= self.capacity

    def add(self, x):
        if self.can_add(x):
            self.coins += x
            return True
        else:
            raise Exception.PiggyBankCapacityExceeded(self.capacity, self.coins, x)
