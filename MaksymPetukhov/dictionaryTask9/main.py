capitals = {
    'Ukraine': 'Kyiv',
    'Poland': 'Warsaw',
    'Germany': 'Berlin',
    'France': 'Paris',
    'Spain': 'Madrid',
}


def get_capital(country):
    if capitals.get(country) is None:
        raise KeyError
    else:
        return capitals.get(country)


def delete_item(country):
    if capitals.get(country) is None:
        raise KeyError
    else:
        capitals.pop(country)
        return capitals


print("Dictionary:", end=f' {capitals}\n\n')

try:
    print("Get value by key 'Ukraine':", end=f'{get_capital("Ukraine")}\n')
except KeyError:
    print("\tError: There is no such key in the dictionary")

try:
    print("Get value by key 'Japan':", end=f'{get_capital("Japan")}\n\n')
except KeyError:
    print("\tError: There is no such key in the dictionary\n")

capitals.update({'Japan': 'Tokyo'})
print("Add Japan to dictionary:", end=f'\n{capitals}\n\n')

capitals.update({'Poland': 'Krakow'})
print("Update Poland capital from Warsaw to Krakow:", end=f'\n{capitals}\n\n')

try:
    if capitals.get('Japan') is None:
        raise KeyError
    else:
        capitals.pop('Japan')
        print("Remove Japan from dictionary:", end=f'\n{capitals}\n\n')
except KeyError:
    print("\tError: There is no such key in the dictionary\n")

capitals.pop('Spain')
print("Remove Spain from dictionary:", end=f'\n{capitals}\n\n')

try:
    delete_item('Japan')
    print("Remove Japan from dictionary:", end=f'\n{capitals}\n\n')
except KeyError:
    print("\tError: There is no such key in the dictionary\n")

capitals.popitem()
print("Remove last item from dictionary:", end=f'\n{capitals}\n\n')

print("Keys: ", end='\n')
for key in capitals.keys():
    print(key)

print("\nValues: ", end='\n')
for values in capitals.values():
    print(values)

print("\nDictionary: ", end='\n')
for key, values in capitals.items():
    print(f"Country: {key}, Capital: {values}")

capitals.clear()
print("\nClear dictionary:", end=f'\n{capitals}\n\n')
