import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
#    letter      code
# 0       A      Alfa
# 1       B     Bravo
# 2       C   Charlie
# ...


# row == Series (remember a Series is just an array or list)
nato_dict = {row.letter: row.code for (index, row) in df.iterrows()}
# A faster approach is to use .set_index('new index') to set the 'letter' column as an index and remove it as a feature  
# nato_dict = df.set_index('letter')['code'].to_dict()

# {
#     "A": "Alfa",
#     "B": "Bravo",
#     "C": "Charlie",
#     "D": "Delta",
#     "E": "Echo",
# ...
#     "U": "Uniform",
#     "V": "Victor",
#     "W": "Whiskey",
#     "X": "X-ray",
#     "Y": "Yankee",
#     "Z": "Zulu",
# }


word = input('put a word: ').upper()

list_letters = [nato_dict[letter] for letter in word if letter in nato_dict]
print(list_letters)