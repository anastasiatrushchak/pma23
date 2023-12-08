from Jetpack import Jetpack
from Backpack import Backpack

if __name__ == "__main__":
    first_jetpack = Jetpack("Barry", "black")
    second_jetpack = Jetpack("Barry", "black")

    if first_jetpack == second_jetpack:
        print("The first jetpack and the second jetpack are equal")
    else:
        print("The first jetpack and the second jetpack are not equal")

    first_backpack = Backpack("Barry", "black",max_size=7)
    second_backpack = Backpack("Barry", "black")

    if first_backpack == second_backpack:
        print("The first backpack and the second backpack are equal")
    else:
        print("The first backpack and the second backpack are not equal")

    print("Print first backpack:")
    print(first_backpack)
    print("Print first jetpack:")
    print(first_jetpack)