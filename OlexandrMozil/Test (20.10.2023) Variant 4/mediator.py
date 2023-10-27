from __future__ import annotations
from abc import ABC


def Mediator(ABC):
    def send_to_client(self, client: Client):
        pass

    def receive_from_client(self, client: Client):
        pass

def

class Client(ABC):
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    def send(self):
        pass

    def receive(self):
        pass

