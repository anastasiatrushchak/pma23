
student_dict = {
    'id': 1,
    'first_name': 'John',
    'last_name': 'Doe',
    'birth_date': '1990-01-01',
    'grades': [85, 90, 78, 92]
}


print("Student Information:")
print(f"ID: {student_dict['id']}")
print(f"Name: {student_dict['first_name']} {student_dict['last_name']}")
print(f"Birth Date: {student_dict['birth_date']}")
print(f"Grades: {student_dict['grades']}")


student_dict['grades'].append(95)
print("\nUpdated Grades:", student_dict['grades'])


del student_dict['birth_date']
print("\nStudent Information (after removing birth date):", student_dict)


student_dict['last_name'] = 'Smith'
print("\nUpdated Last Name:", student_dict['last_name'])