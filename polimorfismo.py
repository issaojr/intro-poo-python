"""
Arquivo que demonstra POLIMORFISMO.
Polimorfismo permite que objetos de diferentes classes respondam 
de forma diferente à mesma chamada de método.
"""

def acionar_poder(superheroi):
    """
    Função que demonstra polimorfismo:
    - Recebe qualquer objeto que tenha o método usar_poder()
    - Cada objeto executa sua própria versão do método
    - Mesmo código, comportamentos diferentes!
    """
    print(f"Acionando poder de {superheroi.__class__.__name__}:")
    superheroi.usar_poder()
    print()  # Linha em branco para melhor visualização