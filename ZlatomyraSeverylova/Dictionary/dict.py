KEYERROR = 'No such element exists'
dict = { 'car_a': 'Audi',
         'car_t': 'Toyota',
         'car_m': 'Mers',
         'car_b': 'BMW'}

print(dict)
for key, value in dict.items():
    print(f'{key}: {value}')

print("\nKey:", dict.keys())
print("Value:", dict.values())

try:
    dict.pop('car_')
    print('\nDelete car_a = ',dict)
except KeyError:
    print(KEYERROR)

del dict['car_t']
print('Delete car_t = ',dict)

dict['car_m'] = 'Mitsubishi'
print('\nChange car_m = ', dict )


dict['car_s'] = 'Skoda'
print('\nAdd element car_s: ', dict)

