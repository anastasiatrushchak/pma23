def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True


number = 17
result = is_prime(number)
if result:
    print(f"{number} є простим числом.")
else:
    print(f"{number} не є простим числом.")


