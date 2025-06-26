from mulhermaravilha import MulherMaravilha
from superman import Superman


def acionar_poder(superheroi):
    superheroi.usar_poder()

clark = Superman("Clark Kent")
diana = MulherMaravilha("Diana Prince")

acionar_poder(clark)
acionar_poder(diana)