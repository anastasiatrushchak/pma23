import json

class CustomDictionary:
    def __init__(self, dictionary):
        self.dictionary = dictionary

    def print(self):
        print(self.dictionary)

    def delete_key(self, key):
        try:
            if key in self.dictionary:
                del self.dictionary[key]
            else:
                print(f"Key '{key}' not found in the dictionary.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def add_key_value(self, key, value):
        try:
            self.dictionary[key] = value
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def pop_delete(self, key):
        try:
            self.dictionary.pop(key)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def change_value(self, key, value):
        try:
            self.dictionary[key] = value
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def change_key(self, old_key, new_key):
        try:

            self.dictionary[new_key] = self.dictionary[old_key]
            del self.dictionary[old_key]

        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def remove_all(self):
        try:
            self.dictionary.clear()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def copy_dict(self):
        try:
            return self.dictionary.copy()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def get_values(self):
        try:
            return self.dictionary.values()
        except Exception as e:
            print(f"An error occurred: {str(e)}")

def read_dict_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{file_path}'.")
        return {}


data_dict = read_dict_from_file("data.json")
custom_dict = CustomDictionary(data_dict)
print("Dictionary: ")
custom_dict.print()
print("Copy of dict:")
copy_dict=custom_dict.copy_dict()
print(copy_dict)
print("Change first name to Bobb")
custom_dict.change_value('First Name', 'Bobb')
custom_dict.print()
print("delete first name key")
key_to_delete ='First Name'
custom_dict.delete_key(key_to_delete)
values = custom_dict.get_values()
print(values)
print("add a new key and value address")
custom_dict.add_key_value("address", "lincolna")
custom_dict.print()
print("change key ")
custom_dict.change_key("Grades","points")
custom_dict.print()
print("pop delete of copy")
custom_dict.pop_delete("Last Name")
custom_dict.print()

