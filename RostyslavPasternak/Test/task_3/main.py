import xml.etree.ElementTree as ET
import xml.sax
import xml.dom.minidom

class Balance:
    def __init__(self,amount,unit):
        self.amount = amount
        self.unit = unit

class Card:
    def __init__(self,card_number,cvv):
        self.card_number =card_number
        self.cvv =cvv
        self.expire_date = expire_date
class Bank:
    def __init__(self,balance,card,issuance_day):
        self.balance =balance
        self.card =card
        self.issuance_day =issuance_day
class Data:
    def __init__(self,age,name, surname):
        self.age = age
        self.name = name
        surname = surname
class Client:
    def __init__(self,id,data,bank):
        self.id =id
        self.data =data
        self.bank =bank


import xml.etree.ElementTree as ET
tree = ET.parse('data.xml')
root = tree.getroot()

# root = ET.fromstring("clients")


for child in root:
    for i in child.attrib:
        for j in i.attrib:
            for k in j.attrib:
                print(k.child.attrib)
