import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

moves = [rock, paper, scissors]

user_move = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
if 0 <= user_move < 3:
    computer_move = random.randint(0,2)

    print(moves[user_move])
    print(f'Computer chose:\n{moves[computer_move]}')


    # RULES
    # Rock wins against scissors.
    # Scissors win against paper.
    # Paper wins against rock.

    if user_move != computer_move:
        if user_move == 0 and computer_move == 1:
            print('You lose.')
        elif user_move == 0 and computer_move == 2:
            print('You win.')
        elif user_move == 1 and computer_move == 0:
            print('You win.')
        elif user_move == 1 and computer_move == 2:    
            print('You lose.')
        elif user_move == 2 and computer_move == 0:
            print('You lose.')
        elif user_move == 2 and computer_move == 1:    
            print('You win.')   
    else:
        print('Tie')
else:
    print('invalid input')
