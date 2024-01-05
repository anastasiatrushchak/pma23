import pandas as pd
import json

# Зчитуємо дані з JSON-файлу
with open('var-1-1/file.json', 'r') as json_file:
    data = json.load(json_file)

# Створюємо DataFrame з даних JSON
df = pd.DataFrame(data)

# Записуємо DataFrame у CSV-файл
df.to_csv('output_table.csv', index=False)