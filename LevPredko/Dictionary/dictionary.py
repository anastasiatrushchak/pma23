
country_dictionary = {
    1: {"country": "United States", "capital": "Washington D.C", "population": "331.9 million"},
    2: {"country": "Italy", "capital": "Rome", "population": "59.11 million"},
    3: {"country": "England", "capital": "London", "population": "55.98 million"},
    4: {"country": "Ukraine", "capital": "Kyiv", "population": "43.79 million"},
    5: {"country": "Portugal", "capital": "Lisbon", "population": "10.33 million"}
}


def print_country(country_dictionary):
    for key, country in country_dictionary.items():
        print(f"{key}:")
        print(f"country: {country['country']}")
        print(f"capital: {country['capital']}")
        print(f"population: {country['population']}")


def add_country(country_dictionary, country, capital, population):
    new_key = len(country_dictionary) + 1
    country_dictionary[new_key] = {"country": country, "capital": capital, "population": population}
    print("\u001B[32m"+f"The country {country} successfully added dictionary"+"\u001B[0m")


def delete_book(country_dictionary, key):
    if key in country_dictionary:
        deleted_country = country_dictionary[key]["country"]
        del country_dictionary[key]
        print("\u001B[32m" + f"The country {deleted_country} has been removed." + "\u001B[0m")
    else:
        print("\u001B[31m" + f"Country with key {key} was not found." + "\u001B[0m")


def replacement(country_dictionary, key, country, capital, population):
    if key in country_dictionary:
        country_dictionary[key] = {"country": country, "capital": capital, "population": population}
        print("\u001B[32m" + f"The country {key} has been successfully changed." + "\u001B[0m")
    else:
        print("\u001B[31m" + f"Country with key {key} was not found." + "\u001B[0m")



print_country(country_dictionary)
print("\n")
add_country(country_dictionary,"Brazil", "Brasília", "214.3 million")
print_country(country_dictionary)
print("\n")
delete_book(country_dictionary, 2)
print_country(country_dictionary)
print("\n")
replacement(country_dictionary, 1, "Australia", "Canberra", "25.69 million")
print_country(country_dictionary)


