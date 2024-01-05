import zipfile
import itertools
import time

CHARACTERS = '0123456789'
PASSWORD_LENGTH = 3

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
def extract_zip(zip_file, password):
        try:
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall(pwd=password.encode())
            return True
        except Exception as e:
            return False

def bruteforce(file, characters, password_length):
    passwords = itertools.product(characters, repeat=password_length)

    for attempt, password in enumerate(passwords, start=1):
        password_str = ''.join(password)
        if extract_zip(file, password_str):
            return password_str, attempt

if __name__ == "__main__":
    file = "student.zip"
    start_time = time.time()
    result = bruteforce(file, CHARACTERS, PASSWORD_LENGTH)
    end_time = time.time()

    if result:
        password_found, attempt_number = result
        print(f"Password found: {password_found}")
        print(f"Attempt number: {attempt_number}")
    else:
        print("Password not found.")

    print(f"Time taken: {format_execution_time(end_time - start_time)}")
