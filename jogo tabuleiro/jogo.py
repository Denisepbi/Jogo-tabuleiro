def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))

def verificar_vitoria(tabuleiro, jogador):
    # Verifica linhas, colunas e diagonais
    for i in range(3):
        if all(tabuleiro[i][j] == jogador for j in range(3)):
            return True
        if all(tabuleiro[j][i] == jogador for j in range(3)): 
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    return False

def jogar_jogo_da_velha():
    tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
    jogador_atual = "X"

    while True:
        exibir_tabuleiro(tabuleiro)
        linha, coluna = map(int, input(f"Jogador {jogador_atual}, escolha a posição (linha coluna): ").split())
        if tabuleiro[linha][coluna] == " ":
            tabuleiro[linha][coluna] = jogador_atual
            if verificar_vitoria(tabuleiro, jogador_atual):
                print(f"Jogador {jogador_atual} venceu!")
                break
            jogador_atual = "O" if jogador_atual == "X" else "X"
        else:
            print("Posição já ocupada. Escolha outra.")

if __name__ == "__main__":
    jogar_jogo_da_velha()
