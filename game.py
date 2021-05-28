"""
Guess the number game
"""
import random
import sys

from art import game_title

difficulty_mode = None
the_number = 0


def pick_a_number():
    global the_number
    the_number = random.randint(1, 100)


def display_title():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")


def choose_mode():
    global difficulty_mode

    while True:
        difficulty_mode = input("Choose a difficulty. Type 'easy', 'hard' or 'quit': ").lower()

        if difficulty_mode == 'easy':
            return 10
        elif difficulty_mode == 'hard':
            return 5
        elif difficulty_mode == 'quit':
            sys.exit(0)


def game_loop(max_attempts):
    global the_number
    attempt = 1
    while attempt <= max_attempts:
        player_guess = int(input("Make a guess: "))

        if player_guess <= 0 or 100 < player_guess:
            print("Hackers always lose")
            return

        if player_guess == the_number:
            print("You win")
            return
        elif player_guess < the_number:
            print(f"Your guess is too low. The number is higher. Attempt {attempt} out of {max_attempts}")
        elif the_number < player_guess:
            print("Your guess is too high. The number is lower. Attempt {attempt} out of {max_attempts}")

        attempt = attempt + 1

    print("You lose")
    return


print(game_title)
pick_a_number()
display_title()
player_attempts = choose_mode()
game_loop(player_attempts)

# if __name__ == main:
