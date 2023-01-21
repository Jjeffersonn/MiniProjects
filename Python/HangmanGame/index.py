import recursos as rc
from time import sleep


def main():
    while True:
        Jogar = rc.jogador_deseja_jogar()

        while Jogar:
            Word = rc.generate_random_word(r'wordList\palavras.txt')
            Apresentacao = rc.apresentacao_de_palavra(Word)
            print(Apresentacao)
            Chances = rc.mostrar_chances(Word)
            sleep(1)
            apresentacao = rc.apresentacao_de_palavra(Word)
            ListaLetras = []
            while True:
                print(f"Você tem {Chances} chances para vencer!")
                sleep(1)
                Resposta = rc.validando_jogada()
                if Resposta in ListaLetras:
                    print(f"Você já tentou a letra {Resposta}")
                else:
                    ListaLetras.append(Resposta)
                    Chances -= 1
                Apresentacao = rc.letra_em_lista(Apresentacao, Word, Resposta)
                sleep(1)
                print(Apresentacao)
                sleep(0.5)
                print(f"Você já tentou estas letras{ListaLetras}")
                sleep(0.5)

                VerificandoAValidacao = len(set(Word) - set(Apresentacao))
                if VerificandoAValidacao < 5:
                    ValidandoPalavra = rc.validando_palavra(Word)
                    sleep(0.5)
                    print(Apresentacao)
                    if ValidandoPalavra:
                        sleep(0.5)
                        print(f"Você ganhou!!. A palavra é {Word}.")
                        break
                if Chances == 0:
                    sleep(0.5)
                    print(f"Você perdeu!! a palavra certa é {Word}")
                    break

            Jogar = rc.jogador_deseja_jogar()
        else:
            break

main()
