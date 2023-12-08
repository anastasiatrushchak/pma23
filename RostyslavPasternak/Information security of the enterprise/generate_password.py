import random
import string

def generate_password(length):
    # Створюємо алфавіт, який містить 59 символів
    alphabet = string.ascii_letters + string.digits + string.punctuation
    # Повертаємо випадковий пароль заданої довжини
    return ''.join(random.choice(alphabet) for _ in range(length))

# Генеруємо пароль з 5 символами
password = generate_password(5)
print("Згенерований пароль:", password)
