import pandas

alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet_dict = {row.letter:row.code for (index, row) in alphabet.iterrows()} 

def generate_phonetic():
    user_input = input("Enter a word: ").upper()
    try:
        input_dict = [alphabet_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(input_dict)
        
generate_phonetic()