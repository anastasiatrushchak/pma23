from Matrix import Matrix
import const

matrixA = Matrix.read(const.INPUT_FILE1)
matrixB = Matrix.read(const.INPUT_FILE2)
Matrix.write(matrixA, matrixB, const.OUTPUT_FILE)
