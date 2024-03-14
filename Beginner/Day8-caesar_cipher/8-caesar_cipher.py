import string
from art import logo

print(logo)

alphabet = string.ascii_lowercase  #abcdefghijklmnopqrstuvwxyz

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
text = input('Type your message: ').lower()
shift = int(input('Type the shift number: '))

#empty list for the new text
new_text = []

def caesar(original_text, steps, choose):
    for letter in original_text:
        index_letter = alphabet.index(letter)

        if choose == 'encode':
            new_index = index_letter + steps
            if new_index >= 26:
                new_index -= 26

        elif choose == 'decode':
            new_index = index_letter - steps
            if new_index < 0:
                new_index += 26
        
        else:
            print('invalid input... dumb bitch') 
            exit() 
    
        new_letter = alphabet[new_index]
        new_text.append(new_letter)

    print(f"The {choose}d text is {''.join(new_text)}")


caesar(text, shift, direction)


