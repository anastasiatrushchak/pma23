from Backpack import Backpack
from Jetpack import Jetpack

def test_backpack():
    testpack = Jetpack("Barry", "black")
    if testpack.name != "Barry":
        print("Backpack.name assigned incorrectly")

    if testpack.color != "black":
        print("Backpack.color assigned incorrectly")
    if testpack.max_size != 5:
        print("Backpack.max_size assigned incorrectly")

    for item in ["pencil", "pen"]:
        testpack.put(item)


    print("Contents:", testpack.contents)

    testpack.fly(4)
    print("Amount of fuel after fly:", testpack.amount_of_fuel)

    testpack.dump()
    print("Contents after dump:", testpack.contents)

if __name__ == "__main__":
    test_backpack()
