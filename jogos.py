import foca
import  adivinhacao2

print("Escolha seu jogo!")
print("(1)Forca (2) Adivinhação")

jogo = int (input("Qual é o jogo?"))

if (jogo == 1):
    print("Jogando forca")
    forca.jogar()
elif (jogo == 1):
    print("Jogando Adivinhação")
    adivinhacao.jogar()