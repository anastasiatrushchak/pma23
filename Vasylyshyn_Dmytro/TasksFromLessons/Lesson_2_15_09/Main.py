from typing import Final

from Vasylyshyn_Dmytro.TasksFromLessons.Lesson_2_15_09.Fibonaci import Fibonacci

name_input_limit_file: Final[str] = 'fileLimit.txt'
name_input_numbers_file: Final[str] = 'file.txt'
name_output_file: Final[str] = 'output.txt'

try:
    with open(name_input_limit_file, 'r') as data:
        limit = data.readline()

    with open(name_input_numbers_file, 'r') as data:
         fibonacci= data.readline().split()

    fibonacci = [int(num) for num in fibonacci]
    lambda limit:float(limit)


except FileNotFoundError:
    print(f"Error:File'{name_input_numbers_file}'or '{name_input_limit_file}'not found.")
except ValueError:
    print(f"Oops, sorry, but you must write a number not'{fibonacci, limit}'")

try:
    result = Fibonacci(fibonacci,limit)
    with open(name_output_file, 'a') as file:
        file.write(str(result.fibonacci()))
        file.write('\n')

except FileNotFoundError:
    print(f"Error:File'{name_output_file}'not found")


# if file is empty, how should I do except?
# how to do constructors without parameters?

