def sort_by_absolute_values(arr):
    sorted_arr = sorted(arr, key=lambda x: abs(x))
    return sorted_arr


original_list = [-20, -5, 10, 15]
sorted_list = sort_by_absolute_values(original_list)
print(sorted_list)