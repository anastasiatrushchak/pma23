Vector_one_file = "VectorOne.txt"
Vector_two_file = "VectorTwo.txt"


def set_vector(file_name):
    vector = []
    with open(file_name) as file:
        line = file.readline()
        vector = line.split()
        vector = [int(i) for i in vector if i.isdigit]
    return vector


def add_vector_to_file(file_name, vector):
    with open(file_name, "w") as file:
        for i in range(3):
            file.write(str(vector[i]))
            file.write(' ')


def sum_vector(vector_file_one, vector_file_two):
    try:
        vector_one = set_vector(vector_file_one)
        vector_two = set_vector(vector_file_two)
        vector_result = []
        if len(vector_one) != len(vector_two):
            raise Exception("Error! Vectors sizes are not equal")
        size = len(vector_one)
        for i in range(size):
            vector_result.append(vector_one[i]+vector_two[i])
        add_vector_to_file("SumResult.txt", vector_result)
    except Exception as err:
        print(err)


def subtract_vector(vector_file_one, vector_file_two):
    try:
        vector_one = set_vector(vector_file_one)
        vector_two = set_vector(vector_file_two)
        vector_result = []
        if len(vector_one) != len(vector_two):
            raise Exception("Error! Vectors sizes are not equal")
        size = len(vector_one)
        for i in range(size):
            vector_result.append(vector_one[i] - vector_two[i])
        add_vector_to_file("SubtractResult.txt", vector_result)
    except Exception as err:
        print(err)


def multiply_vector(vector_file_one, vector_file_two):
    try:
        vector_one = set_vector(vector_file_one)
        vector_two = set_vector(vector_file_two)
        vector_result = []
        if len(vector_one) != len(vector_two):
            raise Exception("Error! Vectors sizes are not equal")
        size = len(vector_one)
        for i in range(size):
            vector_result.append(vector_one[i] * vector_two[i])
        add_vector_to_file("MultiplyResult.txt", vector_result)
    except Exception as err:
        print(err)


def divide_vector(vector_file_one, vector_file_two):
    try:
        vector_one = set_vector(vector_file_one)
        vector_two = set_vector(vector_file_two)
        vector_result = []
        if len(vector_one) != len(vector_two):
            raise Exception("Error! Vectors sizes are not equal")
        size = len(vector_one)
        for i in range(size):
            if vector_two[i] == 0:
                raise ZeroDivisionError("Error! You can't divide by zero!")
            vector_result.append(vector_one[i] / vector_two[i])
        add_vector_to_file("DivideResult.txt", vector_result)
    except Exception as err:
        print(err)


sum_vector(Vector_one_file, Vector_two_file)
divide_vector(Vector_one_file, Vector_two_file)