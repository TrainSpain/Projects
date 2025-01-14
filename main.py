from personagens import personagens
import enemy
from eventos import evento_labirinto
from labirinto import Labirinto
from time import sleep

print(150 * "=")
print(55 * " " + "\033[1;35mBem-Vindo ao Labirinto de Tenebris!!\033[m" + 30 * " ")
print("\033[3;35mHá muitos séculos, um poderoso mago conhecido como Zarathor governava a terra com sabedoria, até ser traído por seus aliados mais próximos.\nA traição resultou em uma maldição que transformou o mago em um espírito vingativo, aprisionado em um vasto labirinto mágico criado por ele mesmo.\nDesde então, o labirinto é conhecido por atrair guerreiros corajosos, magos sábios e aventureiros determinados, prometendo recompensas inimagináveis\npara aqueles que conseguirem escapar.\033[m")
print(150 * "=")
print()
sleep(4)
def escolher_personagem():
    while True:
        print("\nEscolha seu personagem: ")
        for i, personagem in enumerate(personagens, start=1):
            print(f"{i}. {personagem.nome}")
        try:
            escolha = int(input("\nDigite o número do personagem que você deseja (ou 0 para poder ver a historia do seu personagem): "))

            if escolha == 0:
                print("\nHistórias dos personagens:")
                for personagem in personagens:
                    personagem.mostrar_backstory()
            elif 1 <= escolha <= len(personagens):
                return personagens[escolha - 1]
            else:
                print("Escolha inválida! Tente novamente.")
        except ValueError:
            print("Digite um número válido.")

def continuar_jogo(personagem):
    print(f"\nVocê escolheu o personagem: {personagem.nome}")
    personagem.mostrar_status()
    labirinto = Labirinto(tempo_real_minutos=30, tempo_jogo_horas=3)
    labirinto.iniciar_tempo()
    for _ in range(5):
        evento_labirinto(personagem)
        if personagem.constituicao <= 0:
            print("\n\033[1;91mVocê não sobreviveu ao desafio do labirinto...\033[m")
            return

# Iniciar o jogo
personagem_escolhido = escolher_personagem()
continuar_jogo(personagem_escolhido)
