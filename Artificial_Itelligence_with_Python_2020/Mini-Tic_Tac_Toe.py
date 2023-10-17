def verifica_quem(joj):
    contX = 0
    contO = 0
    for i in joj:
        for j in i:
            if j == "X":
                contX += 1
            elif j == "O":
                contO += 1
    if contX > contO:
        return "O"
    else:
        return "X"


while True:
    try:

        print("Bem vindo ao jogo da velha!")
        print("Para jogar, digite o número da linha e o número da coluna que você quer jogar.")

        while True:
            game = [
                ['', '', ''],
                ['', '', ''],
                ['', '', '']
            ]
            while True:
                jogadorAt = verifica_quem(game)
                print(f"É a vez do jogador {jogadorAt}.")
                for i in game:
                    for j in i:
                        print(f'[{j:^5}]', end='')
                    print()
                ondeColunm = int(input("Digite o número da coluna: "))
                ondeLine = int(input("Digite o número da linha: "))
                if 3 >= ondeColunm >= 1 and 3 >= ondeLine >= 1:
                    if game[ondeLine - 1][ondeColunm - 1] == "":
                        game[ondeLine - 1][ondeColunm - 1] = jogadorAt
                    else:
                        print("\nVocê não pode jogar ai.\n")
                        continue
                else:
                    print("\nDigite um número válido.\n")
                    continue
                if (game[0][0] == game[0][1] == game[0][2] != "") or (game[1][0] == game[1][1] == game[1][2] != "") or (
                        game[2][0] == game[2][1] == game[2][2] != ""):
                    print(f"O jogador {game[0][0]} ganhou!")
                    break
                elif (game[0][0] == game[1][0] == game[2][0] != "") or (
                        game[0][1] == game[1][1] == game[2][1] != "") or (game[0][2] == game[1][2] == game[2][2] != ""):
                    print(f"O jogador {game[0][0]} ganhou!")
                    break
                elif (game[0][0] == game[1][1] == game[2][2] != "") or (game[0][2] == game[1][1] == game[2][0] != ""):
                    print(f"O jogador {game[0][0]} ganhou!")
                    break
            while True:
                continuar = input("Deseja continuar? [S/N] ").upper()
                if continuar == "S" or continuar == "N":
                    break
                else:
                    print("Digite uma opção válida.")
                    continue
            if continuar == "N":
                break

    except KeyboardInterrupt:
        print("\033[91mO usuário interrompeu o programa.")
        break
    except ValueError:
        print("\033[91mOcorreu um erro: Digite um valor válido.\033[m")

    except Exception as erro:
        print(f"\033[91mOcorreu um erro: {erro.__class__}.\033[m")
