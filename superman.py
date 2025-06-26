from superheroi import SuperHeroi

class Superman(SuperHeroi):
    def __init__(self, identidade_secreta):
        super().__init__("Superman", identidade_secreta, 95)

    def usar_poder(self):
        print("Superman usa visão de calor!")