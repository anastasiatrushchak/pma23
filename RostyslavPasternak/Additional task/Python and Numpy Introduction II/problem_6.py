import numpy as np
class InvalidSize(ValueError):
    def __init__(self):
        super().__init__("Size error")
def create_block_matrix(A,B,C):
    if A.shape[1] != C.shape[1] != B.shape[1] or B.shape[0] != C.shape[0]:
        raise InvalidSize()
    I = np.eye(C.shape[1])
    block_matrix = np.block([[np.zeros((A.shape[1], C.shape[1])), A.T, I],
                             [A, np.zeros((A.shape[0], A.shape[0])), np.zeros((A.shape[0], C.shape[1]))],
                             [B, np.zeros((C.shape[0], A.shape[0])), C]])
    return block_matrix




A = np.array([[0, 2, 4],
              [1, 3, 5]])

B = np.array([[3, 0, 0],
              [3, 3, 0],
              [3, 3, 3]])

C = np.array([[-2, 0, 0],
              [0, -2, 0],
              [0, 0, -2]])

try:
    result_matrix = create_block_matrix(A,B,C)
    print(result_matrix)
except InvalidSize as e:
    print(e)

