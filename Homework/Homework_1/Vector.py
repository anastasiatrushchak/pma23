import numpy as np
class Vector:
    def __init__(self, vector):
        self.vector = vector
        self.size = vector.size
    @classmethod
    def random(cls,size):
        vector = np.random.randint(1, 11, size = size)
        return cls(vector)
    def append(self, new_element):
        self.vector.append(new_element)