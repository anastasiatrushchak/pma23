import numpy as np

def set_negative_to_zero(arr):
    copy_array = arr.copy()
    copy_array[copy_array < 0] = 0
    return copy_array

if __name__ == "__main__":
    arr = np.array([-1, 2, -3, 4, -5])
    result_array = set_negative_to_zero(arr)
    print("Original Array:", arr)
    print("Resulting Array(Replace all negative numbers):", result_array)