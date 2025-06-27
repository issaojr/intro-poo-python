from ligadajustica import MembroLiga

class Flash(MembroLiga):
    """
    Flash herda de MembroLiga (classe abstrata).
    DEVE implementar o método abstrato convocar().
    """
    
    def convocar(self):
        """Implementação específica do Flash para o método abstrato"""
        print(f"{self.nome} chega em milésimos de segundo!")
        
    def correr_no_tempo(self):
        """Método específico do Flash"""
        print(f"{self.nome} corre através do tempo!")
