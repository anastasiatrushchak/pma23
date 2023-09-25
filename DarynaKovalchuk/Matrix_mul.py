class DetIsZero(Exception):

    def init(self, message="Determinant is zero!"):
        self.message = message
        super().init(self.message)

def read_matrix(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    matrix = []
    for line in lines:
        rows = [int(x) for x in line.split()]
        matrix.append(rows)
    return matrix

def write_matrix(matrix, filename):
    with open(filename, 'a') as file:
        file.write("matrix result:\n")
        for rows in range(len(matrix)):
            file.write(' '.join(map(str, matrix[rows])) + '\n')

try:
    first_matrix = read_matrix('first_matrix.txt')
    second_matrix = read_matrix('second_matrix.txt')
except FileNotFoundError:
    print("One or both files do not exist.")
    exit()

# Перевірка чи файли пусті
if not first_matrix or not second_matrix:
    print("One or both files are empty.")
    exit()

if len(first_matrix) != len(second_matrix) or len(first_matrix[0]) != len(second_matrix[0]):
    print("The sizes don't match.")
else:
    result_multiply = []
    result_devide = []

    # Множення матриць
    def multiply_matrices(first_matrix, second_matrix):
        result = []
        for i in range(len(first_matrix)):
            row = []
            for j in range(len(second_matrix[0])):
                sum_element = 0
                for k in range(len(second_matrix)):
                    sum_element += first_matrix[i][k] * second_matrix[k][j]
                row.append(sum_element)
            result.append(row)
        return result

    # Ділення матриць
    def pow_matrix(first_matrix, second_matrix):
        try:
            transposed = [
                [second_matrix[1][1], -second_matrix[1][0]],
                [-second_matrix[0][1], second_matrix[0][0]]
            ]
            det = second_matrix[0][0] * second_matrix[1][1] - second_matrix[0][1] * second_matrix[1][0]

            if det == 0:
                raise DetIsZero

            inverse = []
            for i in range(len(transposed)):
                inverse.append([])
                for j in range(len(transposed[0])):
                    inverse[i].append(transposed[j][i] / det)
            result = multiply_matrices(first_matrix, inverse)
            return result

        except DetIsZero as e:
            print("Det can't be zero!")
            return []

    result_multiply = multiply_matrices(first_matrix, second_matrix)
    result_devide = pow_matrix(first_matrix, second_matrix)

    write_matrix(result_multiply, 'result_multiply.txt')
    write_matrix(result_devide, 'result_divide.txt')

    print("Result multiply:")
    for rows in result_multiply:
        print(rows)

    print("Result divide:")
    for rows in result_devide:
        print(rows)
