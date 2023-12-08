def arithmagic():
    step_1 = input("Enter a 3-digit number where the first and last digits differ by 2 or more: ")

    if not (step_1.isdigit() and len(step_1) == 3):
        raise ValueError("Invalid input. Please enter a 3-digit number.")

    first_digit = int(step_1[0])
    last_digit = int(step_1[2])

    if abs(first_digit - last_digit) < 2:
        raise ValueError("Invalid input. The first and last digits must differ by 2 or more.")


    step_2 = input("Enter the reverse of the first number, obtained "
                   "by reading it backwards: ")

    if step_2 != step_1[::-1]:
        raise ValueError("Invalid input. The second number must be the reverse of the first number.")


    step_3 = input("Enter the positive difference of these numbers: ")

    if int(step_3) != abs(int(step_1) - int(step_2)):
        raise ValueError("Invalid input. The third number must be the positive difference of the first two numbers.")


    step_4 = input("Enter the reverse of the previous result: ")

    if step_4 != str(int(step_3))[::-1]:
        raise ValueError("Invalid input. The fourth number must be the reverse of the third number.")

    print(str(step_3), "+", str(step_4), "= 1089 (ta-da!)")



if __name__ =="__main__":
    try:
        arithmagic()
    except Exception as e:
        print(e)
