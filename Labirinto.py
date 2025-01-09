import time
print("Bem-vindo ao Labirinto de Tenebris!!")
nome = input("Por favor entre seu nome aventureiro: ")
idade = int(input("Por favor entre sua idade: "))
class Clase:
    Assasino = ("Status:\nForca: 7/10\nDestreza: 10/10\nInteligencia: 8/10\nConstituicao: 5/10\nCarisma: 6/10\nVelocidade: 10/10")
    print()
    Tank = ("Status:\nForca: 9/10\nDestreza: 5/10\nInteligencia: 6/10\nConstituicao: 10/10\nCarisma: 7/10\nVelocidade: 4/10")
    print()
    Cavaleiro = ("Status:\nForca: 8/10\nDestreza: 6/10\nInteligencia: 7/10\nConstituicao: 8/10\nCarisma: 8/10\nVelocidade: 6/10")
    print()
    Mago = ("Status:\nForca: 3/10\nDestreza: 6/10\nInteligencia: 10/10\nConstituicao: 4/10\nCarisma: 7/10\nVelocidade: 5/10")
    print()
print(Clase)
classe = input("Escreva o nome da sua classe de escolha: ").lowercase()
if classe == "assasino":
    aventura = input(f"{nome}, voce agora faz parte da classe assasino. Esta pronto para comecar sua aventura ?")
    inicio = input("[Sim ou Nao]: ").lowercase()
elif classe == "tank":
      aventura = input(f"{nome}, voce agora faz parte da classe assasino. Esta pronto para comecar sua aventura ?")
      inicio = input("[Sim ou Nao]: ").lowercase()
elif classe == "cavaleiro":
    aventura = input(f"{nome}, voce agora faz parte da classe assasino. Esta pronto para comecar sua aventura ?")
    inicio = input("[Sim ou Nao]: ").lowercase()
elif classe == "mago":
