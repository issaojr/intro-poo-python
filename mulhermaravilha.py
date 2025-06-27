from superheroi import SuperHeroi

class MulherMaravilha(SuperHeroi):
    """
    Outra classe que demonstra HERANÇA - herda de SuperHeroi.
    Cada classe filha pode ter implementações diferentes dos métodos.
    """
    
    def __init__(self, identidade_secreta):
        # Chama construtor da classe pai com valores específicos da Mulher-Maravilha
        super().__init__("Mulher-Maravilha", identidade_secreta, 90)

    def usar_poder(self):
        """Sobrescreve o método da classe pai - demonstra POLIMORFISMO"""
        print("Mulher-Maravilha usa o laço da verdade!")
        
    def usar_escudo(self):
        """Método específico da Mulher-Maravilha"""
        print("Mulher-Maravilha bloqueia ataques com suas braceletes!")

