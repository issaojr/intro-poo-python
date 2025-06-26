class SuperHeroi:
    def __init__(self, nome, identidade_secreta, nivel_poder):
        self.__nome = nome
        self.__identidade_secreta = identidade_secreta
        self.__nivel_poder = nivel_poder

    def apresentar(self):
        print(f"Eu sou o {self.__nome}!")

    def revelar_identidade(self):
        print(f"A identidade secreta de {self.__nome} é {self.__identidade_secreta}.")

    def get_nivel_poder(self):
        return self.__nivel_poder

    def set_nivel_poder(self, novo_nivel):
        if 0 <= novo_nivel <= 100:
            self.__nivel_poder = novo_nivel
