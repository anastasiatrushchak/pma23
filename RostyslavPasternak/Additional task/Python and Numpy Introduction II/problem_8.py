import numpy as np
def greatest_product(grid):
    grid = np.load(grid)

    def find_max_product(arr):
        max_product = 0
        for i in range(len(arr) - 3):
            product = np.prod(arr[i:i+4])
            max_product = max(max_product, product)
        return max_product
    max_horizontal = np.max([find_max_product(row) for row in grid])
    max_vertical = np.max([find_max_product(column) for column in grid.T])
    max_diagonal_right = np.max([find_max_product(np.diagonal(grid, offset=i)) for i in range(len(grid)-3)])
    max_diagonal_left = np.max([find_max_product(np.diagonal(np.flip(grid, axis=1), offset=i)) for i in range(len(grid)-3)])

    return max(max_horizontal, max_vertical, max_diagonal_right, max_diagonal_left)

result = greatest_product("grid.npy")
print("The greatest product of four adjacent numbers is:", result)
