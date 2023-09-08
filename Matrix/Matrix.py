def read_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix

X = read_matrix('inputM.txt')
Y = read_matrix('inputM2.txt')

result_add = [[0 for _ in range(len(X[0]))] for _ in range(len(X))]

for i in range(len(X)):
    for j in range(len(X[0])):
        result_add[i][j] = X[i][j] + Y[i][j]

with open('outputM.txt', 'w') as f:
    print("add:", file=f)
    for r in result_add:
        print(r, file=f)

result_sub = [[0 for _ in range(len(X[0]))] for _ in range(len(X))]

for i in range(len(X)):
    for j in range(len(X[0])):
        result_sub[i][j] = X[i][j] - Y[i][j]

with open('outputM.txt', 'a') as f:
    print("sub:", file=f)
    for r in result_sub:
        print(r, file=f)

