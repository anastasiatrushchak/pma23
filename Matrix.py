X = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]

Y = [[5, 8, 1],
    [6, 7, 3],
    [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] + Y[i][j]
print("add")
for r in result:
   print(r)

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

for i in range(len(X)):
   for j in range(len(X[0])):
       result[i][j] = X[i][j] - Y[i][j]
print("min")
for r in result:
   print(r)

result = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

for i in range(len(X)):
   for j in range(len(Y[0])):
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]
print("mult")
for r in result:
    print(r)
