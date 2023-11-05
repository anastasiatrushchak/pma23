def base_to_decimal(num_str, base):
    if not (2 <= base <= 36):
        return -1

    try:
        decimal_value = int(num_str, base)
        return decimal_value
    except ValueError:
        return -1


num_str = "1A"
base = 9
result = base_to_decimal(num_str, base)
if result == -1:
    print(f"Неможливо перетворити {num_str} на основі {base} до десяткової системи.")
else:
    print(f"Результат: {result}")
