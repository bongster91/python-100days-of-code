import pandas

alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter:row.code for (index, row) in alphabet.iterrows()} 

user_input = input("Enter a word: ").upper()
input_dict = [alphabet_dict[letter] for letter in user_input]
print(input_dict)