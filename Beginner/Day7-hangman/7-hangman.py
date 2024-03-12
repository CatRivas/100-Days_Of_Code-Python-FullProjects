import random

#importing external files
from hangman_words import word_list 
import hangman_art  


#WELCOME BI***
print(hangman_art.logo)

#ramdon word choose
chosen_word = random.choice(word_list)

#lives start
lives = 6

#empty list, that will contain the '_' (the blanks)
display = []

#adding '_' to the empty list
for _ in range(len(chosen_word)):
    display.append('_')

print(f"{' '.join(display)}")

#infite loop
while True:
    if '_' in display:
        #input from player
        guess = input('guess a letter: ').lower()

        if guess in display:
            print(f"You've already guessed {guess}. DUMB BI***")

        #cheking guessed letter and putting the right letters in display 
        index = 0
        for letter in chosen_word:
            if letter == guess: 
                display[index] = guess 

            index += 1

 
        #checking if display has the guessed letter
        if not (guess in display):
            lives -=1

            print(f"You guessed {guess}, that's not in the word. YOU LOSE A LIFE.")
            print(hangman_art.stages[lives])
    
        # print(display)
        join_display = ' '.join(display)
        print(join_display)

        #if lives goes down to 0 then the game should stop and it should print "You lose."
        if lives == 0:
            print('YOY LOSE')
            exit()

            
    else:
        break

print('YOU WIN')




