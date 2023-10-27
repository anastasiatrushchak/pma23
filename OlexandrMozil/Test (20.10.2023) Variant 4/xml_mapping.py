import xml.etree.ElementTree as ET


class Bank:
    def __init__(self, amount, unit, issuance_date):
        self.amount = amount
        self.unit = unit
        self.issuance_date = issuance_date


class Card:
    def __init__(self, number, cvv, date, bank: Bank):
        self.number = number
        self.cvv = cvv
        self.date = date
        self.bank = bank

    def __str__(self):
        return f"Number: {self.number}, CVV: {self.cvv}, Date: {self.date}"


class User:
    def __init__(self, name, surname, age, card: Card):
        self.name = name
        self.surname = surname
        self.age = age
        self.card = card


class Client:
    def __init__(self, user: User, id):
        self.user = user
        self.id = id


def read_xml(filename):
    tree = ET.parse(filename + '.xml')
    root = tree.getroot()
    clients = []
    for client in root:
        for bank in client:
            for balance in bank:
                bank = Bank(balance.attrib['amount'], balance.attrib['unit'])
            for card in client:
                card = Card(card.attrib['number'], card.attrib['cvv'], card.attrib['date'], bank)
            for issence_date in client:
                issence_date = issence_date.attrib['issuence_date']
        for data in client:
            for

    clients.append(Client(user, id))
    return clients


file = input("Name of file to read (no .xml): ")
read_xml(file)
