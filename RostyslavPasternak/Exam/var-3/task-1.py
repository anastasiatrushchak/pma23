import random

def get_index_min_element(matrix):
    size_matrix = len(matrix)
    row_index_min = 0
    col_index_min = 0
    min_element = matrix[row_index_min][col_index_min]
    for i in range(0, size_matrix):
        for j in range(0, size_matrix):
            if min_element > matrix[i][j]:
                min_element = matrix[i][j]
                row_index_min = i
                col_index_min = j

    return (row_index_min, col_index_min)
def sum_row(matrix, index):
    return sum(matrix[index])
def mul_col(matrix, index):
    matrix = list(map(list, zip(*matrix)))
    prod = 1
    for element in matrix[index]:
        prod *= element
    return prod


if __name__ =="__main__":
    size = 2
    matrix = [[random.randint(1,100) for _ in range(0, size)] for _ in range(0, size)]
    print("Початкова матриця")
    print(matrix)

    row_index, col_index = get_index_min_element(matrix)
    print(f"Індекси мінімального елемента: {row_index, col_index}")
    print(f"Сума: {sum_row(matrix, row_index)}")
    print(f"Добуток: {mul_col(matrix, col_index)}")


