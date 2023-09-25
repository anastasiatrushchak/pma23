INPUT_FILE = "input.txt"
INPUT_FILE_SECOND = "input_second.txt"
OUTPUT_FILE = "output.txt"

A_vector = [float]
B_vector = [float]

try:
    with open(INPUT_FILE, "r") as file:
        A = list(map(float, file.readline().split()))
    with open(INPUT_FILE_SECOND, "r") as file:
        B = list(map(float, file.readline().split()))
    with open('output.txt', 'w') as output_file:
        output_file.write("First vector: {}\n".format(A))
        output_file.write("Second vector: {}\n".format(B))
        addition = [A_vector + B_vector for A_vector, B_vector in zip(A, B)]
        subtraction = [A_vector - B_vector for A_vector, B_vector in zip(A, B)]
        multiplication = [A_vector * B_vector for A_vector, B_vector in zip(A, B)]
        division = [A_vector / B_vector for A_vector, B_vector in zip(A, B)]
        output_file.write("Addition vectors: {}\n".format(addition))
        output_file.write("Subtraction vectors: {}\n".format(subtraction))
        output_file.write("Multiplication vectors: {}\n".format(multiplication))
        output_file.write("Division vectors: {}\n".format(division))
except FileNotFoundError:
    print('File not found.')





