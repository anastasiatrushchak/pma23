from Vasylyshyn_Dmytro.HomeWork.Lesson_2_Matrix_Clas.Task_matrix import Matrix
from typing import Final
name_of_file_for_first_matrix:Final[str]= 'first_matrix.txt'
name_of_file_for_second_matrix:Final[str]= 'second_maitrix.txt'
name_output_file:Final[str]= 'output_matrix.txt'
def read_data(file_name):
    try:
        first_matrix = []
        with open(file_name, 'r') as firstFileMatrix:
            for line in firstFileMatrix:
                row = [int(x) for x in line.split()]
                first_matrix.append(row)
        return first_matrix
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except ValueError as e:
        print(f"Oops, sorry, but you must write a number: {e}")

def wright_data(file_name,numbers):
    try:
        with open(file_name, 'a') as file:
            file.write(str(numbers))
            file.write('\n')

    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")


matrix = Matrix(read_data(name_of_file_for_first_matrix), read_data(name_of_file_for_second_matrix))
result_add = matrix+matrix
result_subtract = matrix-matrix
result_multiply = matrix*matrix
result_multiply_by_inverse=matrix/matrix

wright_data(name_output_file,result_add)
wright_data(name_output_file,result_subtract)
wright_data(name_output_file,result_multiply)
wright_data(name_output_file,result_multiply_by_inverse)

