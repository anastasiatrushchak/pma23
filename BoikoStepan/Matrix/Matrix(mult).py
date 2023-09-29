try:
    f_Matrix = []
    s_Matrix = []


    with open('FMatrix.txt', 'r') as firstFileMatrix:
        for line in firstFileMatrix:
            row = [int(x) for x in line.split()]
            f_Matrix.append(row)


    with open('SMatrix.txt', 'r') as secondFileMatrix:
        for line in secondFileMatrix:
            row = [int(x) for x in line.split()]
            s_Matrix.append(row)



    for row in range(len(f_Matrix)):
        print((str(f_Matrix[row])))
    print()
    for row in range(len(s_Matrix)):
        print((str(s_Matrix[row])))
    print()

    matrix_Mult = []
    for i in range(len(f_Matrix)):
            row = []
            for j in range(len(s_Matrix[0])):
                mult = 0
                for k in range(len(s_Matrix)):
                    mult += f_Matrix[i][k] * s_Matrix[k][j]
                row.append(mult)
            matrix_Mult.append(row)

    try:
        def determinant(matrix):
            size = len(matrix)
            if size == 1:
                return matrix[0][0]
            elif size == 2:
                return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            else:
                det = 0
                for col in range(size):
                    submatrix = []
                    for i in range(1, len(matrix)):
                        subrow = []
                        for j in range(len(matrix[i])):
                            if j != col:
                                subrow.append(matrix[i][j])
                        submatrix.append(subrow)
                    cofactor = matrix[0][col] * determinant(submatrix)
                    if col % 2 == 0:
                        det += cofactor
                    else:
                        det -= cofactor
                return det

        def inverse_matrix(matrix):
            size = len(matrix)
            det = determinant(matrix)
            inverse = [[0] * size for _ in range(size)]

            for i in range(size):
                for j in range(size):
                    submatrix = []
                    for row_idx in range(len(matrix)):
                        if row_idx != i:
                            subrow = []
                            for col_idx in range(len(matrix[row_idx])):
                                if col_idx != j:
                                    subrow.append(matrix[row_idx][col_idx])
                            submatrix.append(subrow)
                    cofactor = determinant(submatrix)
                    if (i + j) % 2 == 0:
                        inverse[j][i] = cofactor / det
                    else:
                        inverse[j][i] = -cofactor / det

            return inverse

        inverse_matrix2 = inverse_matrix(s_Matrix)

        matrix_Division = []
        for i in range(len(f_Matrix)):
                row = []
                for j in range(len(inverse_matrix2[0])):
                    dot_product = 0
                    for k in range(len(inverse_matrix2)):
                        dot_product += f_Matrix[i][k] * inverse_matrix2[k][j]
                    row.append(dot_product)
                matrix_Division.append(row)


        print(inverse_matrix2)
        print(matrix_Mult)
        print(matrix_Division)


        with open('OutputMatrix.txt', 'w') as file:

            file.write("Matrix Multiplication:\n")
            for row in range(len(matrix_Mult)):
                file.write(str(matrix_Mult[row]) + '\n')

            file.write("Matrix Division:\n")
            for row in range(len(matrix_Division)):
                file.write(str(matrix_Division[row]) + '\n')
    except Exception as e:
        print(e,"is unreal")
except Exception as e:
    print("error",e)