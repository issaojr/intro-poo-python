"""
Tutorial: Introdução à Programação Orientada a Objetos com Python
Por: Issao Hanaoka Junior - UNIP
Tema: Liga da Justiça

Este código demonstra os 4 pilares da POO:
1. Encapsulamento
2. Herança  
3. Polimorfismo
4. Abstração
"""

from batman import Batman
from flash import Flash
from mulhermaravilha import MulherMaravilha
from polimorfismo import acionar_poder
from superheroi import SuperHeroi
from superman import Superman


def demonstrar_encapsulamento():
    """Demonstra o conceito de ENCAPSULAMENTO"""
    print("=" * 50)
    print("1. ENCAPSULAMENTO")
    print("=" * 50)
    print("Encapsulamento protege os dados e controla o acesso a eles.\n")
    
    # Criando um objeto da classe SuperHeroi
    superheroi = SuperHeroi("Lanterna Verde", "Hal Jordan", 80)

    # Acesso controlado aos atributos através de métodos
    superheroi.apresentar()
    superheroi.revelar_identidade()

    print(f"Nível de poder atual: {superheroi.get_nivel_poder()}")
    
    # Modificando atributo de forma controlada (com validação)
    superheroi.set_nivel_poder(85)
    print(f"Novo nível de poder: {superheroi.get_nivel_poder()}")
    
    # Testando validação do setter
    print("\nTentando definir nível inválido (150):")
    superheroi.set_nivel_poder(150)
    
    print(f"Nível permaneceu: {superheroi.get_nivel_poder()}")
    print("\n" + "=" * 50)


def demonstrar_heranca():
    """Demonstra o conceito de HERANÇA"""
    print("2. HERANÇA")
    print("=" * 50)
    print("Herança permite reutilizar código de uma classe pai.\n")

    # Criando objetos das classes filhas
    clark = Superman("Clark Kent")
    diana = MulherMaravilha("Diana Prince")

    print("Superman (herda de SuperHeroi):")
    clark.apresentar()  # Método herdado da classe pai
    clark.usar_poder()  # Método específico sobrescrito
    clark.voar()        # Método específico do Superman
    
    print(f"Nível de poder: {clark.get_nivel_poder()}")  # Getter herdado
    
    print("\nMulher-Maravilha (herda de SuperHeroi):")
    diana.apresentar()  # Método herdado da classe pai
    diana.usar_poder()  # Método específico sobrescrito
    diana.usar_escudo() # Método específico da Mulher-Maravilha
    
    print(f"Nível de poder: {diana.get_nivel_poder()}")  # Getter herdado
    print("\n" + "=" * 50)


def demonstrar_polimorfismo():
    """Demonstra o conceito de POLIMORFISMO"""
    print("3. POLIMORFISMO")
    print("=" * 50)
    print("Polimorfismo: mesmo método, comportamentos diferentes.\n")
    
    # Lista com objetos de diferentes classes
    superherois = [
        Superman("Clark Kent"),
        MulherMaravilha("Diana Prince"),
        SuperHeroi("Aquaman", "Arthur Curry", 85)
    ]

    print("Acionando o mesmo método para diferentes heróis:")
    for heroi in superherois:
        acionar_poder(heroi)  # Cada classe executa sua versão do método
    
    print("=" * 50)


def demonstrar_abstracao():
    """Demonstra o conceito de ABSTRAÇÃO"""
    print("4. ABSTRAÇÃO")
    print("=" * 50)
    print("Abstração define um contrato que as classes filhas devem seguir.\n")
    
    # Criando objetos que implementam a classe abstrata
    batman = Batman("Batman")
    flash = Flash("Flash")

    print("Membros da Liga da Justiça sendo convocados:")
    batman.convocar()      # Implementação específica do Batman
    batman.entrar_na_liga()  # Método concreto da classe abstrata
    batman.usar_gadgets()  # Método específico do Batman
    
    print()
    
    flash.convocar()       # Implementação específica do Flash  
    flash.entrar_na_liga()   # Método concreto da classe abstrata
    flash.correr_no_tempo()  # Método específico do Flash
    
    print("\n" + "=" * 50)


if __name__ == "__main__":
    print("TUTORIAL: PROGRAMAÇÃO ORIENTADA A OBJETOS COM PYTHON")
    print("Tema: Liga da Justiça")
    print("Por: Issao Hanaoka Junior - UNIP\n")
    
    # Demonstração dos 4 pilares da POO
    demonstrar_encapsulamento()
    demonstrar_heranca()  
    demonstrar_polimorfismo()
    demonstrar_abstracao()
    
    print("TUTORIAL CONCLUÍDO!")
    print("Você aprendeu os 4 pilares da POO: Encapsulamento, Herança, Polimorfismo e Abstração.")
    print("=" * 80)
