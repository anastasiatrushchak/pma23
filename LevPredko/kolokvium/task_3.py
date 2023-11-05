def multiplication_without_zero(number):
    multiplication = 1
    num_string = str(number)

    for num in num_string:
        if num != '0':
            multiplication *= int(num)
    return multiplication


result = multiplication_without_zero(2501)
print(result)
