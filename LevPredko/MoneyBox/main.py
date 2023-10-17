import MoneyBox, Exception

n = int(input("Enter the capacity of the piggy bank: "))
m = int(input("How many coins were put in the piggy bank: "))
k = int(input("How many coins they want to put in the piggy bank: "))

box = MoneyBox.MoneyBox(n)

try:
    if box.add(m):
        print("\u001B[32m"+f"Coins successfully added. Total number of coins: {box.coins}"+"\u001B[0m")
    else:
        print("\u001B[31m"+"Failed to add coins. The capacity of the piggy bank has been exceeded."+"\u001B[0m")
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception.PiggyBankCapacityExceeded as e:
    print("\u001B[31m"+f"The capacity of the piggy bank has been exceeded. Cannot add {e.additional} more coins. The piggy bank has a capacity of {e.capacity}, and it already contains {e.current} coins."+"\u001B[0m")
try:
    if box.can_add(k):
        print("\u001B[32m"+f"You can add another {k} coins."+"\u001B[0m")
    else:
        print("\u001B[31m"+"The capacity of the piggy bank has been exceeded. Cannot add more coins."+"\u001B[0m")
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception.PiggyBankCapacityExceeded as e:
    print("\u001B[31m"+f"The capacity of the piggy bank has been exceeded. Cannot add {e.additional} more coins. The piggy bank has a capacity of {e.capacity}, and it already contains {e.current} coins."+"\u001B[0m")
