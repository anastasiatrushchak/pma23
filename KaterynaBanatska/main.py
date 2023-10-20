class Client:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Ім'я: {self.name}, Email: {self.email}, Телефон: {self.phone}"

c1 = Client("Ivan Moroz", "ivan@example.com", "+1234567890")
c2 = Client("Maria Havrylova", "maria@example.com", "+9876543210")
c3 = Client("Petro Hashchuk", "petro@example.com", "+1112233445")
c4= Client("Ivan Hashchuk", "petro@example.com", "+1112233445")

clients = {
    1: c1,
    2: c2,
    3: c3,
    3: c4
}

for client_id, client in clients.items():
    print(f"Client {client_id}: {client}")

try:
    new_client = Client("Olena Lachynska", "olena@example.com", "+5555555555")
    clients[4] = new_client
except ValueError:
    print("Error: Invalid data for a new client. Client not added.")

if 2 in clients:
    del clients[2]

if 1 in clients:
    try:
        clients[1]=c3
    except ValueError:
        print("Error: Invalid phone number format for client 1.")

print("\n")
for client_id, client_obj in clients.items():
    print(f"Client {client_id}: {client_obj}")
