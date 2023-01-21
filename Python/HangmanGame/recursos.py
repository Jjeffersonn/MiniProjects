from random import randint

def generate_random_word(word_list_path):
    word_list = open(word_list_path).read().split("\n")
    word = word_list[randint(0, len(word_list) - 1)]
    word = list(word)
    return word



def apresentacao_de_palavra(word):
    palavra = len(word)
    apresentacao = "_" * palavra
    apresentacao = list(apresentacao)
    return apresentacao


def jogador_deseja_jogar():
    while True:
        resposta = input("Vamos jogar um jogo da forca? S/N \n > ").strip().upper()
        if resposta == "S" or resposta == "N":
            if resposta == "S":
                return True
            else:
                return False
        else:
            print("Quando quiser jogar digite 'S'. ")


def mostrar_chances(word):
    qnt_de_letras = len(word)
    if qnt_de_letras < 5:
        chances = 4
        return chances
    elif qnt_de_letras < 10:
        chances = 8
        return chances
    elif qnt_de_letras >= 10:
        chances = 10
        return chances


def validando_jogada():
    while True:
        try:
            validacao = True
            print()
            resposta = input("Digite uma letra. \n > ").strip().lower()
            if not resposta.isalpha():
                raise ValueError
            return resposta
        except ValueError:
            print("Digite uma letra.")



def validando_palavra(word):
    resposta = input("Agora tente acertar a palavra. \n >").strip().lower()

    if list(resposta) == word:
        return True
    else:
        return False


def letra_em_lista(apresentacao, word, resposta):
    for index, letter in enumerate(word):
        if letter == resposta:
            apresentacao[index] = letter
    return apresentacao







