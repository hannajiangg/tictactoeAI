import random

def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

def get_player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column separated by space): ").split())
            if board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter valid row and column values.")

def get_ai_move(board):
    available_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(available_moves)

def make_move(board, player, row, col):
    board[row][col] = player

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_board_full(board):
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

def play_tic_tac_toe():
    board = initialize_board()
    current_player = 'O'  # 'O' goes first

    while True:
        print_board(board)

        if current_player == 'O':
            row, col = get_player_move(board)
        else:
            row, col = get_ai_move(board)
            print(f"AI chose row {row} and column {col}")

        make_move(board, current_player, row, col)

        if check_winner(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    play_tic_tac_toe()