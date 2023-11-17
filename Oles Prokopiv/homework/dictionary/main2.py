phone_dictionary = {
    1: {"brand": "Iphone", "model": "15", "year_realise": "2023"},
    2: {"brand": "Xiaomi", "model": "Mi 9", "year_realise": "2019"},
    3: {"brand": "Huawei", "model": "Smart", "year_realise": "2020"},
    4: {"brand": "Samsung", "model": "S22", "year_realise": "2022"},
}

def print_phones(phone_dictionary):
    for key, brand in phone_dictionary.items():
        print(f"{key}:",f"brand: {brand['brand']}",f", model: {brand['model']}",f", year_realise: {brand['year_realise']}")

def add_phone(phone_dictionary, brand, model, year_realise):
    new_key = len(phone_dictionary) + 1
    phone_dictionary[new_key] = {"brand": brand, "model": model, "year_realise": year_realise}
    print(f"The phone {brand} successfully added dictionary")

def delete_phone(phone_dictionary, key):
    if key in phone_dictionary:
        deleted_phone = phone_dictionary[key]["brand"]
        del phone_dictionary[key]
        print(f"The phone {deleted_phone} has been removed." )
    else:
        print(f"Phone with key {key} was not found." )

def replacement(phone_dictionary, key, brand, model, year_realise):
    if key in phone_dictionary:
        phone_dictionary[key] = {"brand": brand, "model": model, "year_realise": year_realise}
        print(f"The phone {key} has been successfully changed.")
    else:
        print(f"Phone with key {key} was not found." )

print_phones(phone_dictionary)
print("\n")
add_phone(phone_dictionary,"Iphone","14","2022")
print("\n")
print_phones(phone_dictionary)
print("\n")
delete_phone(phone_dictionary,5)
print("\n")
print_phones(phone_dictionary)
print("\n")
replacement(phone_dictionary, 3,"Huawei","Smart ultra pro plus","2026")
print("\n")
print_phones(phone_dictionary)
