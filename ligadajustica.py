"""
Arquivo que demonstra ABSTRAÇÃO usando classe abstrata.
Uma classe abstrata define um 'contrato' que as classes filhas devem seguir.
"""

from abc import ABC, abstractmethod

class MembroLiga(ABC):
    """
    Classe abstrata que representa um membro da Liga da Justiça.
    
    ABSTRAÇÃO: Define a estrutura geral sem implementar todos os detalhes.
    Classes filhas DEVEM implementar os métodos abstratos.
    """
    
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def convocar(self):
        """
        Método abstrato - DEVE ser implementado pelas classes filhas.
        Cada herói tem sua forma específica de ser convocado.
        """
        pass
    
    def entrar_na_liga(self):
        """
        Método concreto - disponível para todas as classes filhas.
        Demonstra que classes abstratas podem ter métodos implementados.
        """
        print(f"{self.nome} agora faz parte da Liga da Justiça!")
