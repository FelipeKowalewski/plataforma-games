import random
import string


def sorteia_palavra():
    with open('Lista-de-Palavras.txt', 'r') as arquivo:
        texto = arquivo.read()

    palavras = texto.splitlines()

    escolhida = random.choice(palavras)

    while '-' in escolhida or len(escolhida) < 3:
        escolhida = random.choice(palavras)

    return escolhida


def solicita_entrada(validas):

    entrada = input("Informe o seu palpite: ").upper()
    while entrada not in validas:
        print("Entrada inválida.\n A entrada deve ser uma letra!")
        entrada = input("Informe o seu palpite: ").upper()

    return entrada


def jogo_da_forca():
    print("Bem vindo(a) ao Jogo da Forca!")

    palavra = sorteia_palavra()

    resposta = set(palavra)
    tentativas = set()
    alfabeto = set(string.ascii_uppercase)

    vidas = 7

    while len(resposta) > 0 and vidas > 0:

        print("Voce tem ", vidas," vidas e ja tentou essas letras: ", ' '.join(tentativas))

        lista_palavra = [letra if letra in tentativas else '-' for letra in palavra]

        print("Voce acertou ate agora: ", ' '.join(lista_palavra))

        palpite = solicita_entrada(alfabeto)

        if palpite in alfabeto - tentativas:
            tentativas.add(palpite)
            if palpite in resposta:
                print("Voce acertou uma letra da palavra secreta!")
                resposta.remove(palpite)
            else:
                vidas = vidas - 1
                print("A palavra secreta não possui essa letra.")

        else:
            print("Esse palpite já foi feito anteriormente.")

    if vidas == 0:
        print("Voce morreu. A palavra era", palavra)
    else:
        print(f"Parabéns! Voce acertou a palavra {palavra}")

    return

