class Matrix:
    def __init__(self, first_matrix, second_matrix):
        self.first_matrix = first_matrix
        self.second_matrix = second_matrix

    def __add__(self,other):

        result = [[0 for _ in range(len(self.first_matrix[0]))] for _ in range(len(self.first_matrix))]

        for i in range(len(self.first_matrix)):
            for j in range(len(self.first_matrix[0])):
                result[i][j] = self.first_matrix[i][j] + other.second_matrix[i][j]

        return result

    def __sub__(self, other):
        result = [[0 for _ in range(len(self.first_matrix[0]))] for _ in range(len(self.first_matrix))]

        for i in range(len(self.first_matrix)):
            for j in range(len(self.first_matrix[0])):
                result[i][j] = self.first_matrix[i][j] - other.second_matrix[i][j]

        return result

    def __mul__(self, other):
        result = [[0 for _ in range(len(self.second_matrix[0]))] for _ in range(len(self.first_matrix))]

        for i in range(len(self.first_matrix)):
            for j in range(len(self.second_matrix[0])):
                for k in range(len(self.second_matrix)):
                    result[i][j] += self.first_matrix[i][k] * other.second_matrix[k][j]

        return result


    def __truediv__(self, other):
        result = [[0 for _ in range(len(other.second_matrix[0]))] for _ in range(len(self.first_matrix))]

        for i in range(len(self.first_matrix)):
            for j in range(len(self.first_matrix[0])):
                for k in range(len(other.second_matrix)):
                    result[i][j] += self.first_matrix[i][k] / other.second_matrix[k][j]

        return result



