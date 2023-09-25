INPUT_VECTOR_A = 'input_vector_a.txt'
INPUT_VECTOR_B = 'input_vector_b.txt'
OUT_VECTOR = 'out_vector.txt'
from class_vector import Vector
vector_a = Vector.read(INPUT_VECTOR_A)
vector_b = Vector.read(INPUT_VECTOR_B)
Vector.write(OUT_VECTOR, 'Sum of vectors: ', vector_a.__add__(vector_b))
Vector.write(OUT_VECTOR, 'Difference of vectors: ', vector_a.__sub__(vector_b))
Vector.write(OUT_VECTOR, 'Multiplication of vectors: ', vector_a.__mul__(vector_b))
Vector.write(OUT_VECTOR, 'Division of vectors: ', vector_a.__truediv__(vector_b))
