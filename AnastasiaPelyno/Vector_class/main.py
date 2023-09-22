VECTORS_ONE = 'vector_one.txt'
VECTORS_TWO = 'vector_two.txt'
RESULT_FILE = 'result.txt'
MODE_READ = 'r'
MODE_WRITE = 'w'
FILE_ERROR = 'File Not Found'
class Vector:
    def __init__(self, vector):
        self.vector = vector

    def __str__(self):
        return str(self.vector)

    def __add__(self, other_vector):
        result=[self.vector[i]+other_vector.vector[i] for i in range(len(self.vector))]
        return Vector(result)

    def __sub__(self, other_vector):
        result = [self.vector[i] - other_vector.vector[i] for i in range(len(self.vector))]
        return Vector(result)

    def __mul__(self, other_vector):
        result = [self.vector[i] * other_vector.vector[i] for i in range(len(self.vector))]
        return Vector(result)

    def __truediv__(self, other_vector):
        result = [self.vector[i] / other_vector.vector[i] for i in range(len(self.vector))]
        return Vector(result)

    def reading(vectors_file, mode):
        with open(vectors_file, mode) as file:
            lines = file.readlines()
            values = [int(x) for x in lines[0].split()]
        return Vector(values)
    def writing(self, vector_one, vector_two,action,sign):
        file.write(action+str(vector_one)+' '+str(sign)+' '+str(vector_two)+' '+'='+str(self.vector))
        file.write('\n')
try:
    vec_one=Vector.reading(VECTORS_ONE,MODE_READ)
except FileNotFoundError:
    print(FILE_ERROR)
    exit(-1)
try:
    vec_two = Vector.reading(VECTORS_TWO, MODE_READ)
except FileNotFoundError:
    print(FILE_ERROR)
    exit(-1)
sum_res=vec_one+vec_two
sub_res=vec_one-vec_two
mul_res=vec_one*vec_two
try:
    div_res=vec_one/vec_two
except ZeroDivisionError:
    print('Division by zero vector')
    exit(-1)
try:
    with open(RESULT_FILE,MODE_WRITE) as file:
        sum_res.writing(vec_one,vec_two,'Addition:\n','+')
        sub_res.writing(vec_one,vec_two,'Substraction:\n','-')
        mul_res.writing(vec_one,vec_two,'Multiply:\n','*')
        div_res.writing(vec_one,vec_two,'Dividing:\n','/')
except FileNotFoundError:
    print(FILE_ERROR)
