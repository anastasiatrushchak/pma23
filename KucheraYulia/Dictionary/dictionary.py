
contacts = {
    'John Doe': {
        'phone': '123-456-7890',
        'email': 'john@example.com'
    },
    'Jane Smith': {
        'phone': '987-654-3210',
        'email': 'jane@example.com'
    },
    'Alice Johnson': {
        'phone': '555-123-4567',
        'email': 'alice@example.com'
    }
}

print("Контактна книга:")
for name, info in contacts.items():
    print(f"Ім'я: {name}")
    print(f"Телефон: {info['phone']}")
    print(f"Електронна пошта: {info['email']}")
    print()

new_contact = {
    'phone': '111-222-3333',
    'email': 'new@example.com'
}
contacts['Bob Brown'] = new_contact

print("Контактна книга після додавання:")
for name, info in contacts.items():
    print(f"Ім'я: {name}")
    print(f"Телефон: {info['phone']}")
    print(f"Електронна пошта: {info['email']}")
    print()

contacts['John Doe']['phone'] = '999-999-9999'
contacts['John Doe']['email'] = 'john_doe@example.com'

print("Контактна книга після змін:")
for name, info in contacts.items():
    print(f"Ім'я: {name}")
    print(f"Телефон: {info['phone']}")
    print(f"Електронна пошта: {info['email']}")
    print()


del contacts['Alice Johnson']

print("Контактна книга після видалення:")
for name, info in contacts.items():
    print(f"Ім'я: {name}")
    print(f"Телефон: {info['phone']}")
    print(f"Електронна пошта: {info['email']}")
    print()
