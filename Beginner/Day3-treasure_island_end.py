print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
first_choice = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'\n").lower()
if first_choice != 'left':
    print('Fall into a hole. XX GAME OVER.')
else:
     second_choice = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim acroos.\n').lower()
     if second_choice != 'wait':
         print('Attacked by a trout. XX GAME OVER.')
     else:
         third_choice = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n').lower()
         if third_choice == 'yellow':
             print('YOU WIN!')
         elif third_choice == 'red':
             print('Burned by fire. XX GAME OVER')
         elif third_choice == 'blue':
             print('Eaten by beasts. XX GAME OVER')
         else:
             print('XX GAME OVER')
        
         

#my HP⚡ version of fiding the philosopher's stone
# print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡦⠬⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⢀⣠⣤⣤⣤⣀⠀⠀⠀⠙⠀⠀⠀⠀⢀⣠⣤⣤⣤⣀⠀⠀⠀⠀
# ⠀⠀⢀⣶⠟⠁⠀⠀⠈⠙⣷⡄⠀⠀⠀⠀⢀⣴⠟⠉⠀⠀⠈⠙⢷⡄⠀⠀
# ⠀⠀⣾⢣⡗⠀⠀⠀⠀⠀⠘⣷⣴⠾⠷⣶⣼⢧⡗⠀⠀⠀⠀⠀⠈⣿⠀⠀
# ⠘⠛⣿⢸⡄⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠈⣿⡸⡇⠀⠀⠀⠀⠀⠀⣾⠟⠃
# ⠀⠀⠹⣧⡻⣦⠀⠀⠀⢀⣼⠏⠀⠀⠀⠀⠸⣧⡹⣦⠄⠀⠀⠀⣴⠏⠀⠀
# ⠀⠀⠀⠈⠻⢶⣦⣤⡶⠟⠉⠀⠀⠀⠀⠀⠀⠈⠻⠷⣦⣤⡶⠟⠋⠀⠀⠀''')


# print("Welcome to your first fight with you know who.")
# print("Your mission is to find the philosopher's stone.") 

# #first challenge FLUFFY
# play_harp = input('You are facing Fluffy the three-headed dog, do you want to play the harp? Type "yes" or "no"\n').lower()
# if play_harp != 'yes':
#     print('You and your friends are dead. GAME OVER!')
# else:
#     print('Fluffy is sleep, you have free access to the trapdoor')
# #second challenge TENDRILS OF DEVIL'S SNARE
#     behaviour = input("You and friends fall into the tendrils of Devil's Snare, what are you gonna do? Type 'relax' or 'yell' or 'Hermione'\n").lower() 
#     if behaviour != 'relax' and behaviour != 'hermione':
#         print('You and your friends are dead. GAME OVER!')   
#     else:
#         print("You pass the devil's snare so you are free to go to the next challenge")    
# #third challenge FLYING KEYS
#         fly = input("You're in a room full of flying keys, how would you open the close door? Type 'alohomora' or 'broomstick'\n").lower()
#         if fly != 'broomstick':
#             print("Don't be Ron... You and your friends are dead. GAME OVER!")
#         else:
#             print("You open the door with the key and almost died but you didn't... A huge chess game...")
#             print('TO BE CONTINUED')
