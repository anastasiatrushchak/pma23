import numpy as np

def flip_maximum_diagonal_matrix(matrix):
    i = 0
    for row in matrix:
        index = np.argmax(row)
        temp = row[index]
        row[index] = row[i]
        row[i] = temp
        print(f"{row[i]} <-> {row[index]}")
        i += 1
    return matrix


if __name__ == "__main__":
    random_matrix = np.random.randint(0,  10, size=(3, 3))
    print("Початкова матриця: ")
    print(random_matrix)
    print("Зміни: ")
    random_matrix = flip_maximum_diagonal_matrix(random_matrix)
    print("Кінцеві зміни")
    print(random_matrix)