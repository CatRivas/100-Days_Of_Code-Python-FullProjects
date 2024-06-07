starting_letter_path = 'Input\\Letters\\starting_letter.txt'
invited_names_path = 'Input\\Names\\invited_names.txt'

#saving the names
with open(invited_names_path) as f:
    names = f.readlines()

# print(names) #['Dobby\n', 'Harry\n', 'Hermione\n', 'Ron\n', 'Ginny\n', 'Fred\n', 'George\n', 'Hagrid']

#saving the template letter 
with open(starting_letter_path) as f:
    template = f.read()

#Generate and save a personalized letter for each invited
for name in names:
    guest = name.strip()
    new_invite = template.replace('[name]', guest)
    # print(new_invite)

    #creating each letter
    path = f'Output\\ReadyToSend\\letter_for_{guest}.txt'

    with open(path, mode='w') as f:
        f.write(new_invite)

print("SEND 📧")



