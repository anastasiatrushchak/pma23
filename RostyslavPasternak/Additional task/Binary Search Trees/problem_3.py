from BST import BST

if __name__ == "__main__":
    bst = BST()
    bst.insert(15)
    bst.insert(6)
    bst.insert(18)
    bst.insert(3)
    bst.insert(7)
    bst.insert(17)
    bst.insert(20)
    # bst.draw()
    print(bst)
    bst.remove(18)
    bst.draw()