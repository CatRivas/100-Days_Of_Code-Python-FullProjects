#HP⚡ version of fiding the philosopher's stone

print('''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡦⠬⠧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣠⣤⣤⣤⣀⠀⠀⠀⠙⠀⠀⠀⠀⢀⣠⣤⣤⣤⣀⠀⠀⠀⠀
⠀⠀⢀⣶⠟⠁⠀⠀⠈⠙⣷⡄⠀⠀⠀⠀⢀⣴⠟⠉⠀⠀⠈⠙⢷⡄⠀⠀
⠀⠀⣾⢣⡗⠀⠀⠀⠀⠀⠘⣷⣴⠾⠷⣶⣼⢧⡗⠀⠀⠀⠀⠀⠈⣿⠀⠀
⠘⠛⣿⢸⡄⠀⠀⠀⠀⠀⠀⣿⠁⠀⠀⠈⣿⡸⡇⠀⠀⠀⠀⠀⠀⣾⠟⠃
⠀⠀⠹⣧⡻⣦⠀⠀⠀⢀⣼⠏⠀⠀⠀⠀⠸⣧⡹⣦⠄⠀⠀⠀⣴⠏⠀⠀
⠀⠀⠀⠈⠻⢶⣦⣤⡶⠟⠉⠀⠀⠀⠀⠀⠀⠈⠻⠷⣦⣤⡶⠟⠋⠀⠀⠀''')


print("Welcome to your first fight with you know who.")
print("Your mission is to find the philosopher's stone.") 

#first challenge FLUFFY
play_harp = input('You are facing Fluffy the three-headed dog, do you want to play the harp? Type "yes" or "no"\n').lower()
if play_harp != 'yes':
    print('You and your friends are dead. GAME OVER!')
else:
    print('Fluffy is sleep, you have free access to the trapdoor')
#second challenge TENDRILS OF DEVIL'S SNARE
    behaviour = input("You and friends fall into the tendrils of Devil's Snare, what are you gonna do? Type 'relax' or 'yell' or 'Hermione'\n").lower() 
    if behaviour != 'relax' and behaviour != 'hermione':
        print('You and your friends are dead. GAME OVER!')   
    else:
        print("You pass the devil's snare so you are free to go to the next challenge")    
#third challenge FLYING KEYS
        fly = input("You're in a room full of flying keys, how would you open the close door? Type 'alohomora' or 'broomstick'\n").lower()
        if fly != 'broomstick':
            print("Don't be Ron... You and your friends are dead. GAME OVER!")
        else:
            print("You open the door with the key and almost died but you didn't... A huge chess game...")
            print('TO BE CONTINUED')
