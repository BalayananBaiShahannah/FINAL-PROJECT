def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def check_tie(board):
    return all(all(cell != ' ' for cell in row) for row in board)

def get_player_input(player, board):
    while True:
        try:
            row = int(input(f"{player}, enter the row (1-3): ")) - 1
            col = int(input(f"{player}, enter the column (1-3): ")) - 1
            if board[row][col] == ' ':
                return row, col
            else:
                print("Cell is already taken. Choose another one.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 1 and 3.")

def main():
    print("Welcome to Tic-Tac-Toe!")

    player1 = input("Enter the name of Player 1 (X): ")
    player2 = input("Enter the name of Player 2 (O): ")
    
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = player1
    current_symbol = 'X'

    while True:
        print_board(board)
        row, col = get_player_input(current_player, board)
        board[row][col] = current_symbol

        if check_winner(board, current_symbol):
            print_board(board)
            print(f"Congratulations, {current_player}! You have won!")
            break
        elif check_tie(board):
            print_board(board)
            print("The game is a tie!")
            break

        current_player = player2 if current_player == player1 else player1
        current_symbol = 'O' if current_symbol == 'X' else 'X'

if __name__ == "__main__":
    main()
