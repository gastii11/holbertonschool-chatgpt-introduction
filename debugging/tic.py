#!/usr/bin/python3

def print_board(board):
    """Print the current Tic Tac Toe board."""
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < len(board) - 1:
            print("-" * 5)


def check_winner(board):
    """Check if there is a winner."""
    # check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return row[0]

    # check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_full(board):
    """Check if the board is full (tie)."""
    for row in board:
        if " " in row:
            return False
    return True


def tic_tac_toe():
    """Main game loop."""
    board = [[" "] * 3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Input handling with validation
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
        except ValueError:
            print("❌ Invalid input! Please enter numbers only (0, 1, or 2).")
            continue

        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("❌ Out of range! Please enter values between 0 and 2.")
            continue

        if board[row][col] != " ":
            print("❌ That spot is already taken! Try again.")
            continue

        # Make the move
        board[row][col] = player

        # Check winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"🎉 Player {winner} wins!")
            break

        # Check tie
        if is_full(board):
            print_board(board)
            print("🤝 It's a tie!")
            break

        # Switch player
        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
