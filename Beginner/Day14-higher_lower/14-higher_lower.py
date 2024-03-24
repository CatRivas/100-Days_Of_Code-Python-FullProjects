from art import logo, vs
from game_data import data
import random
import os

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls')


def get_random():
    """Returns a random influencer from the data list."""
    random_influencer = random.choice(data)

    return random_influencer

def gameplay():
    """Starts the game and allows the user to guess who has more followers."""
    score = 0
    lista_players = [get_random(), get_random()]
    while True:
        # print(lista_players)
        player_1 = lista_players[0]
        player_2 = lista_players[1]
        
        # If players are the same, get another player for player_2
        if player_1 == player_2:
            player_2 = get_random()

        print(logo)

        # If the player has a score greater than 0, show the current score
        if score > 0:
            print(f"You're right! Current score: {score}")
        
        print(f"Compare A: {player_1['name']}, a {player_1['description']}, from {player_1['country']}")
        print(vs)
        print(f"Against B: {player_2['name']}, a {player_2['description']}, from {player_2['country']}")
        
        # The user guess who has more followers
        guess = input("Who has more followers? Type 'A' or 'B' ").upper().strip()
  
        # Check if the user's guess is correct
        if guess == 'A' and player_1['follower_count'] > player_2['follower_count'] or guess == 'B' and player_1['follower_count'] < player_2['follower_count']:
            lista_players.pop(0)
            lista_players.append(get_random())
            score += 1
            clear_screen()
        elif guess == 'A' and player_1['follower_count'] < player_2['follower_count'] or guess == 'B' and player_1['follower_count'] > player_2['follower_count']:
            print(f"Sorry, that's wrong. Final score: {score}")
            break
            
gameplay()
















 





