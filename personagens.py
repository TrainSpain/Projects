class Personagem:
    def __init__(self, nome, backstory, forca, destreza, inteligencia, constituicao, carisma, velocidade):
        self.nome = nome
        self.backstory = backstory
        self.forca = forca
        self.destreza = destreza
        self.inteligencia = inteligencia
        self.constituicao = constituicao
        self.carisma = carisma
        self.velocidade = velocidade

    def mostrar_status(self):
        print(f"\nStatus de {self.nome}:")
        print(f"Forca: {self.forca}/10")
        print(f"Destreza: {self.destreza}/10")
        print(f"Inteligencia: {self.inteligencia}/10")
        print(f"Constituicao: {self.constituicao}/10")
        print(f"Carisma: {self.carisma}/10")
        print(f"Velocidade: {self.velocidade}/10")
        print()

    def mostrar_backstory(self):
        print(f"\nHistória do {self.nome}:")
        print(self.backstory)
        print()

# Criação dos personagens
assassino = Personagem(
    "Assassino",
    "Um renegado buscando redenção por uma vida de crimes.\nA lenda diz que escapar do labirinto concede uma segunda chance na vida.",
    7, 10, 8, 5, 6, 10
)

tank = Personagem(
    "Tank",
    "Um soldado cujo reino foi destruído, buscando o poder necessário para restaurar a paz e proteger o que restou de seu povo.",
    9, 5, 6, 10, 7, 4
)

cavaleiro = Personagem(
    "Cavaleiro",
    "Um guerreiro nobre enviado em missão pelo rei para derrotar o espírito de Zarathor e recuperar um artefato sagrado perdido no centro do labirinto.",
    8, 6, 7, 8, 8, 6
)

mago = Personagem(
    "Mago",
    "Um aprendiz que deseja libertar o espírito de Zarathor para restaurar o equilíbrio do mundo mágico.",
    3, 6, 10, 4, 7, 5
)

# Lista de personagens
personagens = [assassino, tank, cavaleiro, mago]