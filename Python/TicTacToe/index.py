import numpy as np


# Avaliando se o jogador está disposto a jogar.
while True:
    print("Vamos jogar o jogo da mais esperiente")
    Resposta = input("Digite S ou N.")

# Condicional de validação de input
    if Resposta == "s":

        Contador = 0
        Tabuleiro = np.matrix("0 0 0 ; 0 0 0; 0 0 0")

        while True:
            print(
                f"[{Tabuleiro.item(0,0)}] [{Tabuleiro.item(0,1)}] [{Tabuleiro.item(0,2)}]\n"
                f"[{Tabuleiro.item(1,0)}] [{Tabuleiro.item(1,1)}] [{Tabuleiro.item(1,2)}]\n"
                f"[{Tabuleiro.item(2,0)}] [{Tabuleiro.item(2,1)}] [{Tabuleiro.item(2,2)}]"
                .replace("0", " ").replace("1", "X").replace("2", "O")
            )

            if Contador % 2 == 0:
                Jogador = 1
            else:
                Jogador = 2

            Jogada = ""
            while Jogada == "":
                try:
                    Jogada = tuple(map(int, input(f"Digite a linha e a coluna separados por vírgula.\nJogador {Jogador} > ").replace(" ", "").split(",")))

                    Linha = Jogada[0] - 1
                    Coluna = Jogada[1] - 1

                    if (Linha > 2 or Linha < 0) or (Coluna > 2 or Coluna < 0):
                        raise ValueError

                except ValueError:
                    Jogada = ""
                    print("Erro")
                except IndexError:
                    Jogada = ""
                    print("Erro")



            if Tabuleiro.item(Linha, Coluna) == 0:
                Tabuleiro.itemset((Linha,Coluna), Jogador)
                Contador += 1

            else:
                print("Escolha um local ainda não selecionado")
                
            PossibilidadesVitoria = [
                Tabuleiro.item(0, 0) == 1 and Tabuleiro.item(0, 1) == 1 and Tabuleiro.item(0, 2) == 1,
                Tabuleiro.item(0, 0) == 2 and Tabuleiro.item(0, 1) == 2 and Tabuleiro.item(0, 2) == 2,
                Tabuleiro.item(1, 0) == 1 and Tabuleiro.item(1, 1) == 1 and Tabuleiro.item(1, 2) == 1,
                Tabuleiro.item(1, 0) == 2 and Tabuleiro.item(1, 1) == 2 and Tabuleiro.item(1, 2) == 2,
                Tabuleiro.item(2, 0) == 1 and Tabuleiro.item(2, 1) == 1 and Tabuleiro.item(2, 2) == 1,
                Tabuleiro.item(2, 0) == 2 and Tabuleiro.item(2, 1) == 2 and Tabuleiro.item(2, 2) == 2,
                Tabuleiro.item(0, 0) == 1 and Tabuleiro.item(1, 0) == 1 and Tabuleiro.item(2, 0) == 1,
                Tabuleiro.item(0, 0) == 2 and Tabuleiro.item(1, 0) == 2 and Tabuleiro.item(2, 0) == 2,
                Tabuleiro.item(0, 1) == 1 and Tabuleiro.item(1, 1) == 1 and Tabuleiro.item(2, 1) == 1,
                Tabuleiro.item(0, 1) == 2 and Tabuleiro.item(1, 1) == 2 and Tabuleiro.item(2, 1) == 2,
                Tabuleiro.item(0, 2) == 1 and Tabuleiro.item(1, 2) == 1 and Tabuleiro.item(2, 2) == 1,
                Tabuleiro.item(0, 2) == 2 and Tabuleiro.item(1, 2) == 2 and Tabuleiro.item(2, 2) == 2,
                Tabuleiro.item(0, 0) == 1 and Tabuleiro.item(1, 1) == 1 and Tabuleiro.item(2, 2) == 1,
                Tabuleiro.item(0, 0) == 2 and Tabuleiro.item(1, 1) == 2 and Tabuleiro.item(2, 2) == 2,
                Tabuleiro.item(2, 0) == 1 and Tabuleiro.item(1, 1) == 1 and Tabuleiro.item(0, 2) == 1,
                Tabuleiro.item(2, 0) == 2 and Tabuleiro.item(1, 1) == 2 and Tabuleiro.item(0, 2) == 2
            ]
                
            CamposPreenchidos = [
                Tabuleiro.item(0,0) != 0, 
                Tabuleiro.item(0,1) != 0,
                Tabuleiro.item(0,2) != 0,
                Tabuleiro.item(1,0) != 0,
                Tabuleiro.item(1,1) != 0,
                Tabuleiro.item(1,2) != 0,
                Tabuleiro.item(2,0) != 0,
                Tabuleiro.item(2,1) != 0,
                Tabuleiro.item(2,2) != 0
            ]
            if True in PossibilidadesVitoria:
                print(
                    f"[{Tabuleiro.item(0, 0)}] [{Tabuleiro.item(0, 1)}] [{Tabuleiro.item(0, 2)}]\n"
                    f"[{Tabuleiro.item(1, 0)}] [{Tabuleiro.item(1, 1)}] [{Tabuleiro.item(1, 2)}]\n"
                    f"[{Tabuleiro.item(2, 0)}] [{Tabuleiro.item(2, 1)}] [{Tabuleiro.item(2, 2)}]"
                    .replace("0", " ").replace("1", "X").replace("2", "O")
                )
                print(f"Jogador {Jogador} ganhou!")
                break

            else:
                QtdCamposPreenchidos = 0
                for Campo in CamposPreenchidos:
                    if Campo:
                        QtdCamposPreenchidos += 1
                if QtdCamposPreenchidos == 9:
                    print("Jogo empatado!")
                    break

    elif Resposta == "n":
        break

    else:
        print("Digite S ou N porfavor.")
