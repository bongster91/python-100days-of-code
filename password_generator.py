import random
print('Welcome to the PyPassword Generator!')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
letters_input = int(input('How many letters would you like in your password?\n'))
symbols_input = int(input('How many symbols would you like?\n'))
numbers_input = int(input('How many numbers would you like?\n'))
password = ''

while letters_input > 0 or symbols_input > 0 or numbers_input > 0:
    next_char = random.randint(1, 3)
    if next_char == 1 and letters_input > 0:
        password += letters[ random.randint(0, len(letters) - 1) ]
        letters_input -= 1
    elif next_char == 2 and symbols_input > 0:
        password += symbols[ random.randint(0, len(symbols) - 1) ]
        symbols_input -= 1
    elif next_char == 3 and numbers_input > 0:
        password += numbers[ random.randint(0, len(numbers) - 1) ]
        numbers_input -= 1

print(f'Here is your password: {password}')