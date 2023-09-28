import random
def jogar():
    print("Bem vindos ao jogo de adivinhação!")

numero_secreto = random.randrange(1, 101) * 100
total_de_tentativas = 0
pontos = 1000

print("Qual o nível de dificuldade que você quer?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Define o nível:"))

if (nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5

for rodada in range(1, total_de_tentativas + 1):
    print("tentativas {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100:")
    print("Você digitou:", chute_str)
    chute = int(chute_str)
    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100!")
        continue
    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print("Você acertou! Você ganhou {} de pontos.".format(pontos))
        break
    else:
        if(maior):
            print("Você errou! Seu chute foi maior que o número secreto, tente novamente.")
        elif(menor):
            print("Você errou! Seu chute foi menor que o número secreto, tente novamente.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos


print("Fim de jogo")


jogar()