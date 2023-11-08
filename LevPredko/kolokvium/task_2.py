def find_copy_elements(arr):
    non_unique_elements = []

    for item in arr:
        if arr.count(item) > 1:
            non_unique_elements.append(item)
    return non_unique_elements


input_array = [1, 2, 3, 1, 3]
result = find_copy_elements(input_array)
print(result)
