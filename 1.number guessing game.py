import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print("Try to guess it!")

    number_to_guess = random.randint(1, 100)
    guess = None

    # Loop 
    while guess != number_to_guess:
        try:
            guess = int(input("Enter your guess: "))
            
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
                continue

            if guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

number_guessing_game()
