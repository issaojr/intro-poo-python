from superheroi import SuperHeroi

class Superman(SuperHeroi):
    """
    Classe que demonstra HERANÇA - Superman herda de SuperHeroi.
    Reutiliza código da classe pai e adiciona comportamentos específicos.
    """
    
    def __init__(self, identidade_secreta):
        # super() chama o construtor da classe pai (SuperHeroi)
        # Demonstra como reutilizar código da classe base
        super().__init__("Superman", identidade_secreta, 95)

    def usar_poder(self):
        """Sobrescreve o método da classe pai - demonstra POLIMORFISMO"""
        print("Superman usa visão de calor!")
        
    def voar(self):
        """Método específico do Superman - não existe na classe pai"""
        print("Superman voa pelos céus!")