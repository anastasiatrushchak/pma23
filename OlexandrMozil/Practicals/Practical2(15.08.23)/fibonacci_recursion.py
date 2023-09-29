with open("fibonachi2.txt", "r") as inputStart:
    input_numbers = [float(number) for line in inputStart for number in line.split(",") if number.isdigit()]

with open("stopnnumber.txt", "r") as inputStop:
    stop_number = inputStop.readline()
    if stop_number.isdigit():
        stop_number = float(stop_number)

print(input_numbers, " ", stop_number)


def count_fibonacci(start_parameters, stop):
    last_number = start_parameters[-1]
    if last_number >= stop:
        return start_parameters
    else:
        next_number = (start_parameters[-2] + start_parameters[-1])
        start_parameters.append(next_number)
        return count_fibonacci(start_parameters, stop)


result = count_fibonacci(input_numbers, stop_number)

with open("fibonacci_output.txt", "w") as writeResult:
    writeResult.write(str(result))