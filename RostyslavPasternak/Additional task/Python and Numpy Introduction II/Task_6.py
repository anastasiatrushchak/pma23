# import numpy as np
#
# A = np.array([[0,2,4],
#      [1,3,5]])
# B = np.array([[3,0,0],
#      [3,3,0],
#      [3,3,3]])
# C = np.array([[-2,0,0],
#      [0,-2,0],
#      [0,0,-2]])
# I = np.eye(3)
#
# block_mat = np.block([[0, A.T, I],[A,0,0],[B,0,C]])


import numpy as np

def create_block_matrix():
    A = np.array([[0, 2, 4],
                  [1, 3, 5]])

    B = np.array([[3, 0, 0],
                  [3, 3, 0],
                  [3, 3, 3]])

    C = np.array([[-2, 0, 0],
                  [0, -2, 0],
                  [0, 0, -2]])

    I = np.eye(3)

    # Create the block matrix using numpy.block()
    block_matrix = np.block([[0, A.T, I],
                             [A, 0, np.zeros_like(A)],
                             [B, np.zeros_like(B), C]])

    return block_matrix

# Call the function to create the block matrix
result_matrix = create_block_matrix()

# Print the resulting block matrix
print(result_matrix)
