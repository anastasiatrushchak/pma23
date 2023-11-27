class Node:
    def __init__(self, data):
        if not isinstance(data, (int, float, str)):
            raise TypeError("Data must be of type int, float, or str.")
        self.value = data
    def __str__(self):
        return str(self.value)



if __name__ == "__main__":
    try:
        node1 = Node(12)
        node2 = Node(12.01)
        node3 = Node("sad")
    except Exception as e:
        print(e)
    else:
        print("All data has been added successfully")