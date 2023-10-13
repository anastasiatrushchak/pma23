import Constants, Class

myList = Class.LinkedList()
myList.load_from_file(Constants.INPUT_FILE)
myList.print()
print("\nDelete element:")
myList.delete(3)
myList.print()
print("\nInsert value:")
myList.insert(1, 51)
myList.print()
print("\nInsert none:")
myList.insert(0, None)
myList.print()
print("\nClear list:")
myList.clear()
myList.print()
