students = {
    "Ivan Ivanov": [4, 5, 3, 4],
    "Kulyk Daryna": [3, 3, 5, 4],
    "Petrov Petro": [5, 5, 5, 5],
    "Pavlyk Pavlo": [4, 4, 4, 4],
    "Kozak Oksana": [4, 5, 4, 5]
}

print("Values: ", students.values())
print("Keys: ", students.keys())


students.pop("Ivan Ivanov")
print("\nDelete entry with 'Ivan Ivanov' key")
print("Ivan Ivanov disappeared from the dictionary", students)
print("\nRatings of a user named Ivan Ivanov:", students.get("Ivan Ivanov", "User not found"))


students["Ivan Ivanov"] = [4, 5, 3, 4]
print("\nAdd user with name 'Ivan Ivanov'", students)

new_marks = [1, 2, 3, 4]
students["Ivan Ivanov"] = new_marks
print("\nChange marks for user with name 'Ivan Ivanov'")
for name, marks in students.items():
    if name == "Ivan Ivanov":
        print("New Ratings:", marks)
