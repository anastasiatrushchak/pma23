import platform
import hashlib
import subprocess

def get_computer_name():
    return platform.node()

def get_registry_info():
    try:
        # Використовуємо system_profiler для отримання інформації про систему
        system_profiler_output = subprocess.check_output(["system_profiler", "SPHardwareDataType"], universal_newlines=True)
        # Знаходимо рядок, який містить серійний номер
        serial_number_line = [line for line in system_profiler_output.split('\n') if 'Serial Number' in line][0]
        # Отримуємо значення серійного номера
        serial_number = serial_number_line.split(':')[-1].strip()
        return serial_number
    except Exception as e:
        print(f"Помилка отримання інформації з реєстра: {e}")
        return None

def generate_unique_key():
    computer_name = get_computer_name()
    registry_info = get_registry_info()

    if registry_info is None:
        return None

    combined_info = f"{computer_name}-{registry_info}"
    unique_key = hashlib.md5(combined_info.encode()).hexdigest()

    return unique_key

if __name__ == "__main__":
    unique_key = generate_unique_key()

    if unique_key:
        print(f"Унікальний ключ комп'ютера: {unique_key}")
    else:
        print("Не вдалося згенерувати унікальний ключ.")

