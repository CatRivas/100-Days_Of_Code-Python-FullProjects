from art import logo, vs
from game_data import data
import random

#index random
def get_random():
    random_influencer = random.choice(data)
    # index_random = data.index(random_influencer)   
    return random_influencer


def get_players():
    players = []

    for _ in range(2):
        random_item = get_random()
        players.append(random_item)

    return players

def compare_players(gamers):
    player_1 = gamers[0]
    player_2 = gamers[1]

    if player_1['follower_count'] > player_2['follower_count']:
        gamers.pop(1)
    else:
        gamers.pop(0)
    
    print(gamers)

def gameplay():
    while True:
        score = 0
        lista_players = get_players()
        print(logo)
        print(f"Compare A: {lista_players[0]['name']}, a {lista_players[0]['description']}, from {lista_players[0]['country']}")
        print(vs)
        print(f"Against B: {lista_players[1]['name']}, a {lista_players[1]['description']}, from {lista_players[1]['country']}")
        guess = input("Who has more followers? Type 'A' or 'B' ").upper().strip()
            # compare_players(guess)

            
# gameplay()

lista_players = get_players()
print(lista_players)
compare_players(lista_players)


            # break







 





