contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Контакт '{name}' доданий з номером {phone}")

def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"Контакт '{name}' видалений")
    else:
        print(f"Контакт '{name}' не знайдений")

def view_contacts():
    print("Список контактів:")
    for name, phone in contacts.items():
        print(f"Ім'я: {name}, Телефон: {phone}")

while True:
    print("\nОберіть дію:")
    print("1. Додати контакт")
    print("2. Видалити контакт")
    print("3. Переглянути контакти")
    print("4. Вийти")
    choice = input("Ваш вибір: ")

    if choice == '1':
        name = input("Введіть ім'я контакту: ")
        phone = input("Введіть номер телефону: ")
        add_contact(name, phone)
    elif choice == '2':
        name = input("Введіть ім'я контакту для видалення: ")
        delete_contact(name)
    elif choice == '3':
        view_contacts()
    elif choice == '4':
        print("Вихід з програми!")
        break
    else:
        print("Неправильний вибір. Будь ласка, виберіть з доступних опцій.")
