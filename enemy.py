class Enemy:
    def __init__(self, nome, forca, agilidade, inteligencia, constituicao, carisma, velocidade, habilidades_especiais=None):
        self._nome = nome
        self._forca = forca
        self._agilidade = agilidade
        self._inteligencia = inteligencia
        self._constituicao = constituicao
        self._carisma = carisma
        self._velocidade = velocidade
        self._habilidades_especiais = habilidades_especiais or []
    
    @property
    def name(self):
        """Retorna o nome do inimigo."""
        return self._nome

    def attack(self):
        """Simula um ataque básico baseado na força."""
        print(f"{self._nome} ataca com um golpe devastador!")

    def use_habilidade(self, habilidade):
        """Usa uma habilidade especial, se disponível."""
        if habilidade in self._habilidades_especiais:
            print(f"{self._nome} usa {habilidade}!")
        else:
            print(f"{self._nome} não possui a habilidade {habilidade}.")

    def description(self):
        """Exibe uma descrição breve do inimigo."""
        return f"{self._nome} está pronto para a batalha! Cuidado com sua velocidade e habilidades especiais."

# Instâncias dos inimigos
goblin = Enemy(
    nome="Goblin",
    forca=4,
    agilidade=7,
    inteligencia=3,
    constituicao=5,
    carisma=2,
    velocidade=8
)

minotaur = Enemy(
    nome="Minotauro",
    forca=9,
    agilidade=5,
    inteligencia=4,
    constituicao=8,
    carisma=3,
    velocidade=6
)

zarathor = Enemy(
    nome="Espírito de Zarathor",
    forca=6,
    agilidade=7,
    inteligencia=10,
    constituicao=5,
    carisma=9,
    velocidade=8,
    habilidades_especiais=[
        "Chamas Profanas",
        "Contrato da Ruína",
        "Invocação de Servos Sombrios",
        "Desvanecer",
        "Grito do Abismo",
        "Chama do Pacto"
    ]
)

fire_beetle = Enemy(
    nome="Besouro de Fogo Gigante",
    forca=6,
    agilidade=4,
    inteligencia=2,
    constituicao=8,
    carisma=1,
    velocidade=5
)

stone_golem = Enemy(
    nome="Golem de Pedra",
    forca=9,
    agilidade=3,
    inteligencia=1,
    constituicao=10,
    carisma=0,
    velocidade=2
)
