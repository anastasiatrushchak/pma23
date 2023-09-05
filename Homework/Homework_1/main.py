from Matrix import Matrix


mat = Matrix(3, 3)
mat2 = Matrix(3, 3)


print("Перша матриця:")
mat.print()
print("Друга матриця:")
mat2.print()


matRes = mat.division(mat2)
if matRes:
    print("Результат віднімання:")
    matRes.print()