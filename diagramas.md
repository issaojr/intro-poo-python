# Diagramas UML - POO com Python (Liga da Justiça)

## 📊 Diagrama Geral - Relacionamentos

```mermaid
classDiagram
    class SuperHeroi {
        -string __nome
        -string __identidade_secreta
        -int __nivel_poder
        +apresentar()
        +revelar_identidade()
        +get_nivel_poder() int
        +set_nivel_poder(novo_nivel)
        +usar_poder()
    }
    
    class Superman {
        +usar_poder()
        +voar()
    }
    
    class MulherMaravilha {
        +usar_poder()
        +usar_escudo()
    }
    
    class MembroLiga {
        <<abstract>>
        +string nome
        +convocar()* 
        +entrar_na_liga()
    }
    
    class Batman {
        +convocar()
        +usar_gadgets()
    }
    
    class Flash {
        +convocar()
        +correr_no_tempo()
    }
    
    SuperHeroi <|-- Superman : Herança
    SuperHeroi <|-- MulherMaravilha : Herança
    MembroLiga <|-- Batman : Implementa
    MembroLiga <|-- Flash : Implementa
    
    note for SuperHeroi "ENCAPSULAMENTO"
    note for Superman "HERANÇA + POLIMORFISMO"
    note for MembroLiga "ABSTRAÇÃO"
```

## 🔒 1. Encapsulamento

```mermaid
classDiagram
    class SuperHeroi {
        🔒 -string __nome
        🔒 -string __identidade_secreta  
        🔒 -int __nivel_poder
        ────────────────────
        🌐 +apresentar()
        🌐 +revelar_identidade()
        🌐 +get_nivel_poder() int
        🌐 +set_nivel_poder(novo_nivel)
        🌐 +usar_poder()
    }
    
    note for SuperHeroi "ENCAPSULAMENTO:\n🔒 Dados PROTEGIDOS\n🌐 Acesso CONTROLADO\n✅ Validação nos setters"
```

## 👨‍👩‍👧‍👦 2. Herança

```mermaid
classDiagram
    class SuperHeroi {
        <<Classe Pai>>
        -string __nome
        -string __identidade_secreta
        -int __nivel_poder
        +apresentar()
        +revelar_identidade()
        +get_nivel_poder()
        +set_nivel_poder()
        +usar_poder()
    }
    
    class Superman {
        <<Classe Filha>>
        +usar_poder() ⚡
        +voar() ✈️
    }
    
    class MulherMaravilha {
        <<Classe Filha>>
        +usar_poder() 🏹
        +usar_escudo() 🛡️
    }
    
    SuperHeroi <|-- Superman : herda tudo +
    SuperHeroi <|-- MulherMaravilha : herda tudo +
    
    note for SuperHeroi "CLASSE PAI:\nEstrutura comum"
    note for Superman "HERDA + ADICIONA:\nvoar()"
    note for MulherMaravilha "HERDA + ADICIONA:\nusar_escudo()"
```

## 🎭 3. Polimorfismo

```mermaid
sequenceDiagram
    participant Main as 🎬 main.py
    participant Func as 🎯 acionar_poder()
    participant Sup as 🦸‍♂️ Superman
    participant WW as 🦸‍♀️ MulherMaravilha
    participant SH as 🦸 SuperHeroi
    
    Note over Main, SH: 🎭 POLIMORFISMO: Mesmo método, comportamentos diferentes
    
    Main->>Func: acionar_poder(superman)
    Func->>Sup: usar_poder()
    Sup-->>Func: ⚡ "visão de calor!"
    
    Main->>Func: acionar_poder(mulher_maravilha)
    Func->>WW: usar_poder()
    WW-->>Func: 🏹 "laço da verdade!"
    
    Main->>Func: acionar_poder(superheroi_generico)
    Func->>SH: usar_poder()
    SH-->>Func: ⭐ "poder genérico!"
    
    Note over Func: 🎯 MESMA FUNÇÃO, COMPORTAMENTOS DIFERENTES!
```

## 🎯 4. Abstração

```mermaid
classDiagram
    class MembroLiga {
        <<abstract>>
        🎯 CONTRATO OBRIGATÓRIO
        ────────────────────
        +string nome
        +convocar()* 
        +entrar_na_liga()
    }
    
    class Batman {
        ✅ IMPLEMENTA CONTRATO
        ────────────────────
        +convocar() 🦇
        +usar_gadgets()
    }
    
    class Flash {
        ✅ IMPLEMENTA CONTRATO  
        ────────────────────
        +convocar() ⚡
        +correr_no_tempo()
    }
    
    MembroLiga <|-- Batman : deve implementar*
    MembroLiga <|-- Flash : deve implementar*
    
    note for MembroLiga "🎯 DEFINE CONTRATO\n* método obrigatório"
    note for Batman "✅ IMPLEMENTA\nconvocar()"
    note for Flash "✅ IMPLEMENTA\nconvocar()"
```

## 🔄 Fluxo de Execução

```mermaid
flowchart TD
    A[🎬 Execução main.py] --> B[🔒 Demonstra ENCAPSULAMENTO]
    B --> C[👨‍👩‍👧‍👦 Demonstra HERANÇA]
    C --> D[🎭 Demonstra POLIMORFISMO]
    D --> E[🎯 Demonstra ABSTRAÇÃO]
    E --> F[✅ Tutorial Concluído]
    
    B --> B1[SuperHeroi com atributos privados]
    C --> C1[Superman e MulherMaravilha herdam]
    D --> D1[Mesma função, comportamentos diferentes]
    E --> E1[Batman e Flash implementam contrato]
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#e0f2f1
```

---

**💡 Como usar durante a gravação:**

1. **Prepare os diagramas com antecedência** - teste a visualização
2. **Mostre o diagrama ANTES de codificar** - contexto visual primeiro
3. **Conecte código com diagrama** - aponte elementos enquanto explica
4. **Use como referência** - volte ao diagrama para recapitular
5. **Destaque as diferenças** - compare os diagramas entre si
