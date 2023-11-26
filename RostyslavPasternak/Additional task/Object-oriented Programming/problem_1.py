from Backpack import Backpack
def test_backpack():
    testpack = Backpack("Barry", "black")
    if testpack.name != "Barry":
        print("Backpack.name assigned incorrectly")

    if testpack.color != "black":
        print("Backpack.color assigned incorrectly")
    if testpack.max_size != 5:
        print("Backpack.max_size assigned incorrectly")

    for item in ["pencil", "pen", "paper", "computer"]:
        testpack.put(item)

    print("Contents:", testpack.contents)

    testpack.dump()
    print("Contents after dump:", testpack.contents)

if __name__ == "__main__":
    test_backpack()
