import random

def imprimir_mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo da Forca")
    print("*********************************")

def carregar_palavra_secreta():
    # Lê o arquivo com os nomes das frutas
    with open("palavras.txt", "r") as arquivo_palavras:
        # Gerando uma lista com todas as linhas do arquivo
        lista_palavras = arquivo_palavras.readlines()

    # Remove a quebra de linha no final de cada palavra da lista
    lista_palavras = [palavra.rstrip() for palavra in lista_palavras]
    #print(lista_palavras)
    #print(len(lista_palavras))

    # Gera um número aleatório para definir qual será a palavra da partida
    indice_palavra_partida = random.randrange(0, len(lista_palavras))
    # print(indice_palavra_partida)

    # Seleciona a palavra a partir do indice aleatorio
    palavra_secreta = lista_palavras[indice_palavra_partida].upper()
    return palavra_secreta
    # print(palavra_secreta)

def inicializar_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def calcular_quantidade_limite_tentativas(palavra_secreta):
    quantidade_letras_palavra_secreta = len(palavra_secreta)
    quantidade_limite_tentativas = round(quantidade_letras_palavra_secreta / 2)
    print(quantidade_limite_tentativas)
    return quantidade_limite_tentativas

def solicitar_chute(tentativas, limite_tentativas):
    print("Tentativa {} de {}".format(tentativas + 1, limite_tentativas))
    # strip é equivalente ao trim()
    chute = input("Qual letra? ").strip().upper()
    return chute

def verificar_chute(chute, palavra_secreta, letras_acertadas, posicao_letra, erros):
    # Chute correto
    if (chute in palavra_secreta):
        for letra in palavra_secreta:
            if (chute == letra):
                letras_acertadas[posicao_letra] = letra
            posicao_letra += 1
    # Chute incorreto
    else:
        erros += 1

def arriscar_palavra():
    print("Deseja arriscar qual a palavra? (S) Sim / (N) Não")
    informar_palavra = input().strip().upper()
    return informar_palavra

def verificar_palpte_palavra(palavra_secreta):
    print("Agora é com você! Informe seu palpite de palavra: ")
    palpite_palavra = input().strip().upper()
    if (palpite_palavra == palavra_secreta):
        acertou = True
        enforcou = False
        print("Acertou!!")
    else:
        acertou = False
        enforcou = True
        print("Errou... A palavra secreta era {}".format(palavra_secreta))

    acertou_enforcou = [acertou, enforcou]
    return acertou_enforcou

def jogar():

    imprimir_mensagem_abertura()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    enforcou = False
    acertou = False
    tentativas = 0
    limite_tentativas = calcular_quantidade_limite_tentativas(palavra_secreta)
    posicao_letra = 0
    erros = 0
    lacuna_vazia = '_'


    # enquanto nao enforcou e nao acertou
    while(not enforcou and not acertou and tentativas < limite_tentativas):

        chute = solicitar_chute(tentativas, limite_tentativas)
        verificar_chute(chute, palavra_secreta, letras_acertadas, posicao_letra, erros)

        tentativas += 1
        enforcou = erros == limite_tentativas
        acertou = lacuna_vazia not in letras_acertadas
        print(letras_acertadas)

        informar_palavra = arriscar_palavra()
        if (informar_palavra == "S"):
            acertou_enforcou = verificar_palpte_palavra(palavra_secreta)
            acertou = acertou_enforcou[0]
            enforcou = acertou_enforcou[1]

    print("Fim de Jogo!")

if(__name__ == "__main__"):
    jogar()