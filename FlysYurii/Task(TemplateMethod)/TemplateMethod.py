from abc import ABC, abstractmethod
class OperatingSystem(ABC):
    def prepareenvironment(self):
        self.operatingsystem()
        self.setup_hardware()
        self.install_software()
        self.update_settings()

    @abstractmethod
    def operatingsystem(self):
        pass

    @abstractmethod
    def update_settings(self):
        pass
    def setup_hardware(self):
        print("Setting up hardware")
    def install_software(self):
        print("Installing software")


class Windows(OperatingSystem):
    def operatingsystem(self):
        print("Using Windows...")
    def update_settings(self):
        print("Update settings for Windows")
class MacOS(OperatingSystem):
    def operatingsystem(self):
        print("Using MacOS...")
    def update_settings(self):
        print("Update settings for MacOS")

class Linux(OperatingSystem):
    def operatingsystem(self):
        print("Using Linux...")
    def update_settings(self):
        print("Update settings for Linux")

Windows=Windows()
Windows.prepareenvironment()
print('\n')
MacOS=MacOS()
MacOS.prepareenvironment()
print('\n')
Linux=Linux()
Linux.prepareenvironment()