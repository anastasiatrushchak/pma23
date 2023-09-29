Iphones = {
    'iPhone 12': {'Price': 699},
    'iPhone 14 Pro': {'Price': 999},
    'iPhone 15 Pro': {'Price': 1099}
}
print("Start:")
for iphone, info in Iphones.items():
    print(f"Model: {iphone}, Price: ${info['Price']}")
print('\n')
Iphones.pop('iPhone 12')
print("After removing iPhone 12:")
for iphone, info in Iphones.items():
    print(f"Model: {iphone}, Price: ${info['Price']}")
print('\n')
Iphones.update({'iPhone 14 Pro': {'Price': 9999}})
print("After updating price of iPhone 14:")
for iphone, info in Iphones.items():
    print(f"Model: {iphone}, Price: ${info['Price']}")
