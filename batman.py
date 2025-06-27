from ligadajustica import MembroLiga

class Batman(MembroLiga):
    """
    Batman herda de MembroLiga (classe abstrata).
    DEVE implementar o método abstrato convocar().
    """
    
    def convocar(self):
        """Implementação específica do Batman para o método abstrato"""
        print(f"{self.nome} aparece das sombras...")
        
    def usar_gadgets(self):
        """Método específico do Batman"""
        print(f"{self.nome} usa seus gadgets high-tech!")