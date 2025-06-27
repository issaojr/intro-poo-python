class SuperHeroi:
    """
    Classe base que representa um super-herói.
    Demonstra o conceito de ENCAPSULAMENTO - os atributos são privados (__) 
    e só podem ser acessados por métodos específicos (getters/setters).
    """
    
    def __init__(self, nome, identidade_secreta, nivel_poder):
        # Atributos privados (encapsulados) - convenção Python usa __
        self.__nome = nome
        self.__identidade_secreta = identidade_secreta
        self.__nivel_poder = nivel_poder

    def apresentar(self):
        """Método público para apresentar o herói"""
        print(f"Eu sou o {self.__nome}!")

    def revelar_identidade(self):
        """Método público para revelar identidade secreta"""
        print(f"A identidade secreta de {self.__nome} é {self.__identidade_secreta}.")

    def get_nivel_poder(self):
        """Getter - método para acessar atributo privado de forma controlada"""
        return self.__nivel_poder

    def set_nivel_poder(self, novo_nivel):
        """Setter - método para modificar atributo privado com validação"""
        if 0 <= novo_nivel <= 100:
            self.__nivel_poder = novo_nivel
        else:
            print("Nível de poder deve estar entre 0 e 100!")
    
    def usar_poder(self):
        """Método base que será sobrescrito pelas classes filhas (polimorfismo)"""
        print(f"{self.__nome} usa um poder genérico!")
