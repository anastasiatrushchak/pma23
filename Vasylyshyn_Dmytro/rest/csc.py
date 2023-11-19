import json

# Серіалізація
data = {'name': 'John', 'age': 30, 'city': 'New York'}
serialized_data = json.dumps(data)
print("Серіалізовані дані:", serialized_data)

# Десеріалізація 
deserialized_data = json.loads(serialized_data)
print("Десеріалізовані дані:", deserialized_data)
#