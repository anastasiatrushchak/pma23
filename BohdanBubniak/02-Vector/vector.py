def read_vectors(filename):
    with open(filename, 'r') as f:
        vectors = [list(map(int, line.strip().split(','))) for line in f.readlines()]
    return vectors

def vector_addition(v1, v2):
    return [x + y for x, y in zip(v1, v2)]

def vector_subtraction(v1, v2):
    return [x - y for x, y in zip(v1, v2)]

def vector_multiplication(v1, v2):
    return [x * y for x, y in zip(v1, v2)]

def vector_division(v1, v2):
    return [x / y if y != 0 else float('inf') for x, y in zip(v1, v2)]

def start():
    vectors = read_vectors('vectors.txt')

    if len(vectors) % 2 != 0:
        print("Error: Expecting pairs of vectors for operations!")
        return

    results = []
    for i in range(0, len(vectors), 2):
        v1 = vectors[i]
        v2 = vectors[i+1]

        results.append(f"{v1} + {v2} = {vector_addition(v1, v2)}")
        results.append(f"{v1} - {v2} = {vector_subtraction(v1, v2)}")
        results.append(f"{v1} * {v2} = {vector_multiplication(v1, v2)}")
        results.append(f"{v1} / {v2} = {vector_division(v1, v2)}")

    with open('output.txt', 'w') as f:
        for result in results:
            f.write(result + '\n')
            
start()