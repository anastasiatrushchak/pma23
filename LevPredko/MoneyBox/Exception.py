class PiggyBankCapacityExceeded(Exception):
    def __init__(self, capacity, current, additional):
        self.capacity = capacity
        self.current = current
        self.additional = additional
