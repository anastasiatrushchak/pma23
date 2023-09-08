import numpy as np

with open('inputV.txt', 'r') as file:
    lines = file.readlines()
    vector1 = np.array([float(x) for x in lines[0].strip().split()])
    vector2 = np.array([float(x) for x in lines[1].strip().split()])

result = vector1 + vector2
with open('outputV.txt', 'w') as f:
    print(result, file=f)

result1 = vector1 - vector2
with open('outputV.txt', 'a') as f:
    print(result1, file=f)

result2 = vector1 * vector2
with open('outputV.txt', 'a') as f:
    print(result2, file=f)

result3 = vector1 / vector2
with open('outputV.txt', 'a') as f:
    print(result3, file=f)

