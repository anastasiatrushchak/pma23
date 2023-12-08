import itertools
import string
import time

def format_execution_time(execution_time):
    days, remainder = divmod(execution_time, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)

    formatted_time = ""
    if days > 0:
        formatted_time += f"{int(days)} днів "
    if hours > 0:
        formatted_time += f"{int(hours)} годин "
    if minutes > 0:
        formatted_time += f"{int(minutes)} хвилин "
    formatted_time += f"{seconds:.3f} секунд"

    return formatted_time


def generate_passwords(password):
    start_time = time.time()
    attempt_count = 0
    for length in range(8, len(password) + 1):
        combinations = itertools.product(string.ascii_letters + string.digits, repeat=length)
        for combo in combinations:
            attempt = ''.join(combo)
            attempt_count += 1
            print(attempt)
            if attempt == password:
                end_time = time.time()
                elapsed_time = end_time - start_time
                return attempt, elapsed_time, attempt_count
    return None, time.time() - start_time, attempt_count


password_to_find = "abcdzdD1"
found_password, elapsed_time, attempt_count = generate_passwords(password_to_find)

if found_password:
    print(f"Пароль знайдено: {found_password}")
    print(f"Час виконання: {format_execution_time(elapsed_time)} .")
    print(f"Кількість спроб: {attempt_count}")
else:
    print("Пароль не знайдено.")
    print(f"Час виконання: {elapsed_time} сек.")
    print(f"Кількість спроб: {attempt_count}")