import random

def roll_dice():
    return random.randint(1, 6)

def play_round(player_num):
    input(f"Player {player_num}, press Enter to roll the dice...")
    roll = roll_dice()
    print(f"Player {player_num} rolled a {roll}")
    return roll

def determine_round_winner(roll1, roll2):
    if roll1 > roll2:
        return 1
    elif roll2 > roll1:
        return 2
    else:
        return 0  # Tie

def dice_rolling_game():
    player1_wins = 0
    player2_wins = 0

    print("Welcome to the Dice Rolling Game - Best of Three!")

    while player1_wins < 2 and player2_wins < 2:
        print("\nStarting a new round...")
        roll1 = play_round(1)
        roll2 = play_round(2)
        
        round_winner = determine_round_winner(roll1, roll2)
        if round_winner == 1:
            player1_wins += 1
            print("Player 1 wins this round!")
        elif round_winner == 2:
            player2_wins += 1
            print("Player 2 wins this round!")
        else:
            print("This round is a tie!")
        
        print(f"Score: Player 1 - {player1_wins}, Player 2 - {player2_wins}")

    if player1_wins == 2:
        print("\nCongratulations! Player 1 wins the game!")
    else:
        print("\nCongratulations! Player 2 wins the game!")

if __name__ == "__main__":
    dice_rolling_game()
