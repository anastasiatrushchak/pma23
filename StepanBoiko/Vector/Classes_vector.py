class Vector:
    def __init__(self, filename):
        self.vector = []
        self.filename = filename

    def load_vector(self):
        try:
            with open(self.filename, 'r') as vector_file:
                for line in vector_file:
                    values = [int(x) for x in line.split()]
                    self.vector.extend(values)
        except Exception as e:
            print("Error:", e)

    def __len__(self):
        return len(self.vector)
    try:
        def __add__(self, other):
            result = []
            for i in range(len(self)):
                result.append(self.vector[i] + other.vector[i])
            return result

        def __sub__(self, other):
            result = []
            for i in range(len(self)):
                result.append(self.vector[i] - other.vector[i])
            return result


        def __mul__(self, other):
            result = []
            for i in range(len(self)):
                result.append(self.vector[i] * other.vector[i])
            return result

        def __truediv__(self, other):
            try:
                result = []
                for i in range(len(self)):
                    result.append(self.vector[i] / other.vector[i])
                return result
            except ZeroDivisionError:
                print("error zero division")
                exit()
    except Exception:
        print("")
    def save_result(self, output_filename, other_vector):
        vector_sum = self + other_vector
        vector_sub = self - other_vector
        vector_dot = self * other_vector
        vector_div = self / other_vector


        with open(output_filename, 'w') as file:

            file.write("Vector Sum:\n")
            file.write(str(vector_sum) + '\n')

            file.write("Vector Subtract:\n")
            file.write(str(vector_sub) + '\n')

            file.write("Vector Mult:\n")
            file.write(str(vector_dot) + '\n')

            file.write("Vector Division :\n")
            file.write(str(vector_div) + '\n')





filename1 = 'Fvector.txt'
filename2 = 'Svector.txt'
output_filename = '../../Home1/OutputVector.txt'

vector_ops1 = Vector(filename1)
vector_ops1.load_vector()
vector_ops2 = Vector(filename2)
vector_ops2.load_vector()
vector_ops1.save_result(output_filename, vector_ops2)
