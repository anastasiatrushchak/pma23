import json

class Key:
    def __init__(self, name):
        self.name = name

class Value:
    def __init__(self, data_type, value):
        self.data_type = data_type
        self.value = value

file_path = "data.json"
try:
    with open(file_path, 'r') as file:
        data_dict = json.load(file)
        print(data_dict)
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    data_dict = {}
except json.JSONDecodeError:
    print(f"Error: Invalid JSON format in '{file_path}'.")
    data_dict = {}

keys = {
    'First Name': Key('First Name'),
    'Last Name': Key('Last Name'),
    'Date of Birth': Key('Date of Birth'),
    'Grades': Key('Grades')
}

values = {
    'First Name': Value(str, 'Ivan'),
    'Last Name': Value(str, 'Sina'),
    'Date of Birth': Value(str, '1999-05-15'),
    'Grades': Value(list, [85, 92, 78, 95, 89])
}


print(values['First Name'].value)

key = keys['First Name']
if key.name in data_dict:
    del data_dict[key.name]
else:
    print(f"Key '{key.name}' not found in the dictionary.")

key = keys['First Name']
value = values['First Name'].value
try:
    data_dict[key.name] = value
except Exception as e:
    print(f"An error occurred: {str(e)}")

key = keys['First Name']
try:
    data_dict.pop(key.name)
except Exception as e:
    print(f"An error occurred: {str(e)}")

key = keys['First Name']
value = values['First Name'].value
try:
    data_dict[key.name] = value
except Exception as e:
    print(f"An error occurred: {str(e)}")

old_key = keys['First Name']
new_key = Key('New Name')
try:
    data_dict[new_key.name] = data_dict[old_key.name]
    del data_dict[old_key.name]
except Exception as e:
    print(f"An error occurred: {str(e)}")

try:
    copy_dict = data_dict.copy()
except Exception as e:
    print(f"An error occurred: {str(e)}")

try:
    data_dict.clear()
except Exception as e:
    print(f"An error occurred: {str(e)}")

