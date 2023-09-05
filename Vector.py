import numpy as np

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])
skalar = 2

result = vector1 + vector2
print(result)

result1 = vector1 - vector2
print(result1)

result2 = np.dot(vector1, vector2)  #скалярний добуток
print(result2)

result3 = np.cross(vector1, vector2) #векторний добуток
print(result3)

result4 = vector1 * skalar
print(result4)

result5 = vector1 / vector2
print(result5)

result6 = vector1 / skalar
print(result6)