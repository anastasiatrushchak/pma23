dictionary = {
    "hahaha@gmail.com": "Ivan",
    "hahaha1@gmail.com": "Petro",
    "hahaha2@gmail.com": "Denys",
    "hahaha3@gmail.com": "Taras",
}
print("Значення:", dictionary.values())
print("Ключі:", dictionary.keys())

dictionary.pop("hahaha@gmail.com")
print("\nВидаляємо значення за ключем hahaha@gmail.com")
print("hahaha@gmail.com зник з словника:", dictionary)

print("\nІм'я користувача з поштою hahaha1@gmail.com:", dictionary.get("hahaha1@gmail.com"))

dictionary["hahaha@gmail.com"] = "Ivan"
print("\nДодаємо користувача hahaha@gmail.com", dictionary)

dictionary["hahaha1@gmail.com"] = "Changed"
print("\nЗмінюємо користувача hahaha1@gmail.com", dictionary)
