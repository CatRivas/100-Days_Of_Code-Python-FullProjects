from art import logo
import random

def random_number():
    """
    Generates a random number between 1 and 100.

    Returns:
        int: A random integer between 1 and 100.
    """
    random_number = random.randint(1, 100)

    return random_number

def level_dif():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()

    if difficulty == 'easy':
        gameplay(10)
    elif difficulty == 'hard':
        gameplay(5)
    else:
        print('Invalid input')
        exit()

def compare_guess(guess, npc_number):
    """
    Compares the user's guess with the randomly generated number.

    Args:
        guess (int): The user's guess.
        npc_number (int): The randomly generated number.
    """
    if guess > npc_number:
        print('Too high.')
    elif guess < npc_number:
        print('Too low.')
    else:
        print(f'You got it! The answer was {npc_number}')
    


def gameplay(attempst):
    """
    Manages the gameplay, allowing the user to make guesses.

    Args:
        attempts (int): The number of attempts the user has to guess the number.
    """
    result = random_number()
    print(f'the random number is: {result}')

    for _ in range(attempst):    
        print(f'You have {attempst} attempts remaining to guess the number.')
        choice = int(input('Make a guess: '))
        compare_guess(choice, result)

        if choice == result:
            break

        attempst -= 1

    if attempst == 0:
        print("You've run out of guesses, you lose.")

def start_game():
    #prints and calls
    print(logo)
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    level_dif()

start_game()