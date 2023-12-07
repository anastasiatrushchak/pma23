from arraylist import ArrayList
try:
    my_list = ArrayList()
    my_list.add(0)
    my_list.add(200)
    print("List: ", my_list)
    my_list.remove(200)
    print("List after removing \'200\'", my_list)
    my_list.insert(0, 100)
    print(my_list)
    print("Get number by index: ", my_list.get(-1))
    print(my_list.size())
except Exception as e:
    print(e)

