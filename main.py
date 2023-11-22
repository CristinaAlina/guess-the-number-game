import random
from art import logo
from replit import clear

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5


def set_difficulty():
    """Get number of attempts according to difficulty"""
    # Ask the user which difficulty wants to play
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while not difficulty in ['easy', 'hard']:
        difficulty = input(
            "Invalid input. Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS


def decrease_attempts(num_attempts):
    """Decrease number of attempts by 1"""
    return num_attempts - 1


def is_num_guessed(guessed_number, target_number):
    """Returns True if number is guessed and False otherwise"""
    """Prints info for user according to case"""
    if guessed_number == target_number:
        print(f"You got it! The answer was {target_number}.")
        return True
    else:
        if guessed_number < target_number:
            print("Too low.")
        else:
            print("Too high.")
        return False


def play_the_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Choosing a random number between 1 and 100
    target_number = random.randint(1, 100)

    # Get the number of attempts according to difficulty
    num_attempts = set_difficulty()

    game_over = False
    while not game_over:
        print(
            f"You have {num_attempts} attempts remaining to guess the number.")

        guessed_number = int(input("Make a guess: "))

        while guessed_number < 1 or guessed_number > 100:
            guessed_number = int(
                input(
                    "Number has to be between 1 and 100. Make a guess again: ")
            )

        game_over = is_num_guessed(guessed_number, target_number)

        if not game_over:
            num_attempts = decrease_attempts(num_attempts)
            if num_attempts == 0:
                print("You've run out of guesses, you lose.")
                print(f"The number was: {target_number}")
                return
            else:
                print("Guess again.")


play_the_game()
while input(
        "Do you want to play another game? Type 'y' for yes, or 'n' for no: "
).lower() == 'y':
    clear()
    play_the_game()
