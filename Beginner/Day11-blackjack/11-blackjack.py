from art import logo
import random
import os 

def clear_screen():
    # Windows
    os.system('cls')


def get_card():
    deck  = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(deck)
    
    return random_card

def hands():
    #user
    user_hand = []
    computer_hand = []
    for _ in range(2):
        user_hand.append(get_card())
        computer_hand.append(get_card())

    return user_hand, computer_hand


def calculate_score(cards):
    score = sum(cards)
    
    #Blackjack
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    elif 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)    

    return score

#compare user_score and computer_score
def compare_scores(u_score, c_score):
    if u_score == c_score:
        return 'Draw'
    elif u_score == 0:
        return 'Win with a Blackjack'
    elif u_score > 21:
        return 'You went over. You lose'
    elif c_score == 0:
        return 'Lose, opponent has Blackjack'
    elif c_score > 21:
        return 'Opponent went over. You win'
    elif u_score > c_score:
        return 'You win'
    else:
        return 'You lose'

    
# play_again
while True:
    play_again = input('Do you want to play a game of Blackjack? Type "y" or "n": ').lower().strip()
    clear_screen()

    if play_again != 'y':
        break

    #GAME 
    print(logo)
    #calls 
    get_card()
    user_cards, computer_cards = hands()

    #user
    while True: 
        user_score = calculate_score(user_cards)
        computer_score =calculate_score(computer_cards)

        #prints
        print(f'    Your cards: {user_cards}, current score: {user_score}')
        print(f"    Computer first card: {computer_cards[0]}")

        if user_score > 21 or computer_score > 21 or user_score == 0 or computer_score == 0:
            break
        else:
            hit_me = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()  
            if hit_me == 'y':
                user_cards.append(get_card())
            else:
                break

    #computer 
    while computer_score < 17 and computer_score != 0:
        computer_cards.append(get_card())
        computer_score = calculate_score(computer_cards)

    result = compare_scores(user_score, computer_score)

    print(f'    Your final hand: {user_cards}, final score: {user_score}')
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(result)

