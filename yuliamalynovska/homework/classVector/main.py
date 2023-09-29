from Vector import Vector
import const
vectorA = Vector.read(const.INPUT_FILE1)
vectorB = Vector.read(const.INPUT_FILE2)
Vector.write(vectorA, vectorB, const.OUTPUT_FILE)
# try:
#     with open(const.INPUT_FILE1, 'r') as inpV:
#         vectA = inpV.readline().split()
#         vectA = [float(i) for i in vectA if i.isdigit()]
#     with open(const.INPUT_FILE2, 'r') as inpV2:
#         vectB = inpV2.readline().split()
#         vectB = [float(i) for i in vectB if i.isdigit()]
# except FileNotFoundError:
#     print(const.FILE_NOT_FOUND)
#     exit(-1)
# vectorA = Vector(vectA)
# vectorB = Vector(vectB)
#
# with open(const.OUTPUT_FILE, 'w') as out:
#     out.write("Addition:\n")
#     out.write(str(vectorA + vectorB)+'\n')
#
#     out.write("Subtraction:\n")
#     out.write(str(vectorA - vectorB) + '\n')
#
#     out.write("Multiplication:\n")
#     out.write(str(vectorA * vectorB) + '\n')
#
#     out.write("Division:\n")
#     out.write(str(vectorA / vectorB) + '\n')
#