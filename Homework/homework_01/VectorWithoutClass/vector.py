import Constants
def read_vector_from_file(file_path):
    vector = []
    try:
        with open (file_path,'r') as readFile:
            for line in readFile:
                line = line.strip()
                num = [int(i) for i in line.split(Constants.SEPARATOR)]
                vector.append(num)
        return vector
    except ValueError as e:
        print("Error: Different sizes are specified in the file", e)
    except FileNotFoundError as e:
        print("Error: File not found", e)
        return None
    except Exception as e:
        print("An unexpected error occurred", e)
        return None
def add_vectors(vector1, vector2):
    add_vector = []
    for i in range(len(vector1)):
        result_row = []
        for j in range(len(vector1[i])):
            result_row.append(vector1[i][j] + vector2[i][j])
        add_vector.append(result_row)
    return add_vector
def subtract_vectors(vector1, vector2):
    sub_vector = []
    for i in range(len(vector1)):
        result_row = []
        for j in range(len(vector1[i])):
            result_row.append(vector1[i][j] - vector2[i][j])
        sub_vector.append(result_row)
    return sub_vector

def multiply_vectors(vector1, vector2):
    mul_vector = []
    for i in range(len(vector1)):
        result_row = []
        for j in range(len(vector1[i])):
            result_row.append(vector1[i][j] * vector2[i][j])
        mul_vector.append(result_row)
    return mul_vector

def divide_vectors(vector1, vector2):
    try:
        div_vector = []
        for i in range(len(vector1)):
            result_row = []
            for j in range(len(vector1[i])):
                if vector2[i][j] == 0:
                    print("Error: Division by zero is not allowed")
                    return None
                result_row.append(vector1[i][j] / vector2[i][j])
            div_vector.append(result_row)
        return div_vector
    except ZeroDivisionError as e:
        print("Error: Division by zero is not allowed", e)

vector1 = read_vector_from_file(Constants.InputVECTOR1)
vector2 = read_vector_from_file(Constants.InputVECTOR2)

with open(Constants.OutputVECTOR, "w") as file:
    operation = input("Enter the operation (+, -, *, /): ")
    result = []
    if len(vector1) != len(vector2):
        print("Error: Vectors must have the same dimensions")
    if operation == "+":
        result = add_vectors(vector1, vector2)
    elif operation == "-":
        result = subtract_vectors(vector1, vector2)
    elif operation == "*":
        result = multiply_vectors(vector1, vector2)
    elif operation == "/":
        result = divide_vectors(vector1, vector2)
    else:
        print("Error: There is no such operator for vectors")
    if result:
        for item in result:
            file.write(str(item) + '\n')