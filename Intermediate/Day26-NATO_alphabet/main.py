import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
#    letter      code
# 0       A      Alfa
# 1       B     Bravo
# 2       C   Charlie
# ...


# row == column == Series (remember a Series is just an array or a list)

# Dict comprehension approach with .iterrows() method that iterates over the df in pairs of index, row (Not recommended for larger data sets) 
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}


# But a faster and more direct approach is to use built in methods of Pandas, as .set_index('new index') to set the 'letter' column as an index and remove it as a feature  (Recommended for larger data sets)

# nato_dict = df.set_index('letter')
# print(nato_dict)
#             code
# letter
# A           Alfa
# B          Bravo
# C        Charlie


# nato_dict = df.set_index('letter')['code']
# print(nato_dict)
# letter
# A        Alfa
# B       Bravo
# C     Charlie


# nato_dict = df.set_index('letter')['code'].to_dict()
# print(nato_dict)
# {
#     "A": "Alfa",
#     "B": "Bravo",
#     "C": "Charlie",
#      ...
# }



# list_letters = [nato_dict[letter] for letter in word if letter in nato_dict]

while True:
    word = input('put a word: ').upper()
    try:
        list_letters = [nato_dict[letter] for letter in word]
    except KeyError:
        print('Sorry only letter in the alphabet please')
        continue
    else:
        print(list_letters)
        break



