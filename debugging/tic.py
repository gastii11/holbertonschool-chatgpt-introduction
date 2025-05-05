#!/usr/bin/python3

def print_board(board):
    """Imprime el tablero de juego en formato visual."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """Verifica si hay un ganador en el juego."""
    # Verificación de filas
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # Verificación de columnas
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Verificación de diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def get_valid_input():
    """Solicita una posición válida al usuario, evitando errores de entrada."""
    while True:
        try:
            value = int(input("Enter row (0, 1, or 2): "))
            if value in [0, 1, 2]:
                return value
            else:
                print("Invalid choice! Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input! Please enter a number.")

def tic_tac_toe():
    """Ejecuta el juego de Tic-Tac-Toe entre dos jugadores."""
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        print(f"Player {player}, it's your turn.")

        row = get_valid_input()
        col = get_valid_input()

        if board[row][col] == " ":
            board[row][col] = player
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins! 🎉")
                break
            # Alterna entre jugadores
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

tic_tac_toe()

