# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random


simbolos = {'*': 'pedra', '#': 'papel', '%': 'tesoura'}


def pedrapapeltesoura():

    user = input("Digite '*' para jogar pedra, '|' para papel ou '%' para tesoura: ")
    computer = random.choice(['*', '#', '%'])

    if user != '*' and user != '#' and user != '%':
        return "Jogada Invalida!"

    print(f'O computador escolheu {simbolos[computer]}.\n\n')

    if user == computer:
        return "---EMPATE---"

    elif (user == 'r' and computer == 't') or (user == 'p' and computer == 'r') or \
            (user == 't' and computer == 'p'):
        return "---VITORIA---"

    return "---DERROTA---"


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
