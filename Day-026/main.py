import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
match = {row.letter:row.code for(index, row) in df.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter a word: ")
result = [match[character.upper()] for character in user_input]
print(result)
