import adivinhacao
import forca

print("*********************************")
print("Seleção de jogos")
print("*********************************")

print("Escolhe seu jogo: (1) Forca / (2) Adivinhação: ")
jogo_escolhido = int(input())

if(jogo_escolhido == 1):
    print("Forca")
    forca.jogar()
elif(jogo_escolhido == 2):
    print("Adivinhacao")
    adivinhacao.jogar()