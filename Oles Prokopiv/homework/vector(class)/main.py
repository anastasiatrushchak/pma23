from vector_class import Vector

INPUT_VECTOR_ONE = 'input.txt'
INPUT_VECTOR_SECOND = 'input_second.txt'
OUTPUT_VECTOR = 'output.txt'

first_vector = Vector.read(INPUT_VECTOR_ONE)
second_vector = Vector.read(INPUT_VECTOR_SECOND)

Vector.write(OUTPUT_VECTOR, 'Sum of vectors: ', first_vector.__add__(second_vector))
Vector.write(OUTPUT_VECTOR, 'Difference of vectors: ', first_vector.__sub__(second_vector))
Vector.write(OUTPUT_VECTOR, 'Multiplication of vectors: ', first_vector.__mul__(second_vector))
Vector.write(OUTPUT_VECTOR, 'Division of vectors: ', first_vector.__truediv__(second_vector))