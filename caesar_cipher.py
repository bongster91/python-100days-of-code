alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    new_text = ''
    
    for char in text:
        position = alphabet.index(char)
        next_letter = (position + shift) % 26
        new_text += alphabet[next_letter]

    print(new_text)

def decrypt(text, shift):
    new_text = ''
    
    for char in text:
        position = alphabet.index(char)
        next_letter = (position - shift + 26) % 26
        new_text += alphabet[next_letter]

    print(new_text)

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)
else:
    print("That's an invalid input.")