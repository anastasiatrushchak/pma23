class OutOfListBound(Exception):
    def __init__(self):
        self.message = "Index is out of list size!"
        super().__init__(self.message)
