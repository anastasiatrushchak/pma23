from abstract import TechDeviceFactory, TechPhone, TechTab, TechBook

class AppleTechDeviceFactory(TechDeviceFactory):
    def create_smartphone(self):
        return iPhone()

    def create_tablet(self):
        return iPad()

    def create_laptop(self):
        return MacBook()

class SamsungTechDeviceFactory(TechDeviceFactory):
    def create_smartphone(self):
        return GalaxyPhone()

    def create_tablet(self):
        return GalaxyTab()

    def create_laptop(self):
        return GalaxyBook()
class iPhone(TechPhone):
    def info(self):
        return "Apple iPhone - смартфон"

class iPad(TechTab):
    def info(self):
        return "Apple iPad - планшет"

class MacBook(TechBook):
    def info(self):
        return "Apple MacBook - ноутбук"

class GalaxyPhone(TechPhone):
    def info(self):
        return "Samsung Galaxy - смартфон"

class GalaxyTab(TechTab):
    def info(self):
        return "Samsung Galaxy Tab - планшет"

class GalaxyBook(TechBook):
    def info(self):
        return "Samsung Galaxy Book - ноутбук"
