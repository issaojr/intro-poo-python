from batman import Batman
from flash import Flash
from mulhermaravilha import MulherMaravilha
from polimorfismo import acionar_poder
from superheroi import SuperHeroi
from superman import Superman


if __name__ == "__main__":
    # Início da demonstração de encapsulamento
    print("== Encapsulamento ==")
    superheroi = SuperHeroi("Lanterna Verde", "Hal Jordan", 80)

    # Acesso indireto aos atributos
    superheroi.apresentar()
    superheroi.revelar_identidade()

    print("Nível de poder atual:", superheroi.get_nivel_poder())
    superheroi.set_nivel_poder(85)
    print("Novo nível de poder:", superheroi.get_nivel_poder())

    # Fim da demonstração de encapsulamento
    print("\n== Fim da demonstração de encapsulamento ==")

    # Início da demonstração de herança
    print("\n== Herança ==")

    clark = Superman("Clark Kent")
    diana = MulherMaravilha("Diana Prince")

    clark.apresentar()
    clark.usar_poder()

    diana.apresentar()
    diana.usar_poder()

    # Fim da demonstração de herança
    print("\n== Fim da demonstração de herança ==")

    # Início da demonstração de polimorfismo
    print("== Polimorfismo ==")
    superherois = [
        Superman("Clark Kent"),
        MulherMaravilha("Diana Prince")
    ]

    for heroi in superherois:
        acionar_poder(heroi)

    # Fim da demonstração de polimorfismo
    print("\n== Fim da demonstração de polimorfismo ==")

    # Início da demonstração de abstração
    print("== Abstração ==")
    batman = Batman("Batman")
    flash = Flash("Flash")

    batman.convocar()
    flash.convocar()

    # Fim da demonstração de abstração
    print("\n== Fim da demonstração de abstração ==")
