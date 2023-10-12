import matrices_functions as funcs
import exceptions as exc
import os

firstMatrix = []
secondMatrix = []
try:
    if os.path.exists("matrices_input.txt"):
        with open("matrices_input.txt", "r") as readFile:
            if os.path.getsize("matrices_input.txt") == 0:
                raise exc.EmptyFile("File is empty!")
            temp = firstMatrix
            for line in readFile:
                line = line.strip()
                if not line:
                    temp = secondMatrix
                    continue
                row = [float(i) for i in line.split(" ")]
                temp.append(row)
    else:
        raise exc.FileDoesntExist("No input file was found!")
except exc.FileDoesntExist as FDE:
    print(FDE)
    raise SystemExit
except exc.EmptyFile as EF:
    print(EF)
    raise SystemExit

summ = funcs.summ(firstMatrix, secondMatrix)
subtraction = funcs.subtraction(firstMatrix, secondMatrix)
multiplication = funcs.multiplication(firstMatrix, secondMatrix)
division = funcs.division(firstMatrix, secondMatrix)

output_string = (f"Сума:\n{funcs.matrix_to_string(summ)}\n\n"
                 f"Різниця:\n{funcs.matrix_to_string(subtraction)}"
                 f"\n\nДобуток:\n{funcs.matrix_to_string(multiplication)}\n\n"
                 f"Частка:\n{funcs.matrix_to_string(division)}")
try:
    if os.path.exists("output_matrix.txt"):
        with open("output_matrix.txt", "w") as writeFile:
            writeFile.write(output_string)
    else:
        raise exc.FileDoesntExist("No output file was found!")
except exc.FileDoesntExist as FDE:
    print(FDE)
    raise SystemExit
