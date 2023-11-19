class MoneyBox:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__coins = 0

    def can_add(self, numb):
        try:
            if numb < 0:
                raise Exception("Error! Number of coins can't be <0")
            if numb > self.__capacity - self.__coins:
                raise Exception("Oh no, there isn't enough space.")
            else:
                print("There is enough space")
                return True
        except Exception as err:
            print(err)
            return False

    def add(self, coins):
        try:
            if coins < 0:
                raise Exception("Error! Number of coins can't be minus.")
            if self.can_add(coins):
                self.__coins += coins
                print("Coins added")
            else:
                raise Exception("Oh no, there isn't enough space.")
        except Exception as err:
            print(err)


box = MoneyBox(5)
box.can_add(7)
box.add(3)
box.can_add(3)
box.add(2)
box.add(1)