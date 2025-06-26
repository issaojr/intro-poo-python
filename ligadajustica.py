from abc import ABC, abstractmethod

class MembroLiga(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def convocar(self):
        pass
