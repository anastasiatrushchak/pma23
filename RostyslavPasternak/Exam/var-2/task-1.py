import numpy as np
def get_list_special_items(matrix):
    matrix = matrix.transpose()
    my_list=[]
    for col in matrix:
        i = 0
        for element in col:
            if element > sum(np.delete(col, i)):
                my_list.append(element)
            i += 1
    return my_list
if __name__ =="__main__":
    matrix = np.array([[1,1,1,100],[1,1,999,1],[1,1,1,1]])
    print(matrix)
    my_list = get_list_special_items(matrix)
    print(my_list)