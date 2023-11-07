def list_ops():
    my_list = ["bear", "ant", "cat", "dog"]

# 1. Append "eagle".
    my_list.append("eagle")

    print("Append 'eagle': ", my_list)
# 2. Replace the entry at index 2 with "fox".
    my_list[2] = "fox"
    print("Replace at index 2: ", my_list)

# 3. Remove (or pop) the entry at index 1.
    my_list.pop(1)
    print("Remove at index 1: ", my_list)

# 4. Sort the list in reverse alphabetical order.
    my_list.sort(reverse=True)
    print("Sort: ", my_list)

# 5. Replace "eagle" with "hawk".
    my_list[my_list.index("eagle")] = "hawk"
    print("Replace 'eagle' with 'hawk'", my_list)

# 6. Add the string "hunter" to the last entry in the list.
    my_list[-1] += " hunter"
    print("Add  'hunter'", my_list)


    return my_list


print("End result: ", list_ops())
