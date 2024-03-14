import string
from art import logo

print(logo)

alphabet = string.ascii_lowercase  #abcdefghijklmnopqrstuvwxyz


def caesar(original_text, steps, choose):
    #empty list for the new text
    new_text = []

    for character in original_text:
        if character.isalpha():
            index_letter = alphabet.index(character)

            if choose == 'encode':
                new_index = (index_letter + steps) % 26

            elif choose == 'decode':
                new_index = (index_letter - steps) % 26    
        
            new_letter = alphabet[new_index]
            new_text.append(new_letter)
        
        else:
            new_text.append(character)

    print(f"The {choose}d text is {''.join(new_text)}")

#inputs from user
def inputs():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input('Type your message: ').lower()
    shift = int(input('Type the shift number: '))

    return direction, text, shift


while True:
        direction, text, shift = inputs()
        
        caesar(text, shift, direction)

        user_input = input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
        
        if user_input != 'yes':
             print('Goodbye, go outside please...')
             break

    


