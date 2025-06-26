from superheroi import SuperHeroi

class MulherMaravilha(SuperHeroi):
    def __init__(self, identidade_secreta):
        super().__init__("Mulher-Maravilha", identidade_secreta, 90)

    def usar_poder(self):
        print("Mulher-Maravilha usa o laço da verdade!")

