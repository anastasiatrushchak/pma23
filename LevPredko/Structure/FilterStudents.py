import json
import Constants
try:
    with open(Constants.JsonFile, 'r') as file:
        data = json.load(file)
except FileNotFoundError as e:
    print("Error: File not found", e)
except EOFError as e:
    print("Error: Empty file", e)
except Exception as e:
    print("An unexpected error occurred", e)
all_students_passed = True

for student in data["Students"]:
    for grade in student["grades"].values():
        if int(grade) < 0 or int(grade) > 100:
            raise ValueError("The grade can't be less than 0 or greater than 100")
        if int(grade) >= 51:
            print("\u001B[32m"+f"{student['firstName']} {student['secondName']} complete the session"+"\u001B[0m")
            break
        elif int(grade) < 51:
            all_students_passed = False
            print("\u001B[31m"+f"{student['firstName']} {student['secondName']} didn't complete the session"+"\u001B[0m")
            break
if all_students_passed:
    print("\u001B[34;3m"+"All students passed the session"+"\u001B[0m")