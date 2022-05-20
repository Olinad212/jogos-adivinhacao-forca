import random

def imprimir_mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("*********************************")

def obter_intervalo_para_numero():
    print("Informe o valor mínimo para o número aleatório: ")
    valor_minimo = int(input())

    # Garante que o valor máximo é maior que o valor mínimo
    while(True):
        print("Informe o valor máximo para o número aleatório: ")
        valor_maximo = int(input())
        if(valor_maximo > valor_minimo):
            break
        else:
            print("O valor máximo deve ser maior do que o valor mínimo!")

    valores_minimo_maximo = (valor_minimo, valor_maximo)
    return valores_minimo_maximo

def gerar_numero_pra_adivinhacao(valor_minimo, valor_maximo):
    return random.randrange(valor_minimo, valor_maximo+1)  # O ultimo valor é não inclusivo

def obter_total_tentativas():
    print("Qual o nível de dificuldade: (1) Fácil / (2) Médio / (3) Difícil: ")
    nivel = int(input())
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5
    return total_tentativas

def solicitar_chute(rodada, total_tentativas, valores_minimo_maximo):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = int(input("Digite um numero entre {} e {}: ".format(valores_minimo_maximo[0], valores_minimo_maximo[1])))
    return chute

def marcar_chute_errado(chute_errado_menor, chute_errado_maior, pontos, numero_secreto, chute_numero):
    if (chute_errado_menor):
        print("Você errou. O chute é menor que o valor secreto...")
    elif (chute_errado_maior):
        print("Você errou. O chute é maior que o valor secreto...")
    pontos = pontos - abs((numero_secreto - chute_numero))
    return pontos

def jogar():

    imprimir_mensagem_abertura()

    # Inicializando variáveis
    valores_minimo_maximo = obter_intervalo_para_numero()
    numero_secreto = gerar_numero_pra_adivinhacao(valores_minimo_maximo[0], valores_minimo_maximo[1])
    total_tentativas = obter_total_tentativas()
    pontos = 1000

    #print("Numero secreto: {}".format(numero_secreto))

    for rodada in range(1, total_tentativas+1):

        chute_numero = solicitar_chute(rodada, total_tentativas, valores_minimo_maximo)

        # Criação de variáveis para uso nas condicionais
        chute_certo        = chute_numero == numero_secreto
        chute_errado_maior = chute_numero > numero_secreto
        chute_errado_menor = chute_numero < numero_secreto

        if(chute_certo):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            pontos = marcar_chute_errado(chute_errado_menor, chute_errado_maior, pontos, numero_secreto, chute_numero)

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()
