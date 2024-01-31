import random
words_list = ['apple', 'babboon', 'cars', 'drape', 'elephant', 'flamethrower', 'gorilla', 'highway']
answer = random.choice(words_list)
display = ['_' for i in range(0, len(answer))]
lives = 5
game_over = False

print('Welcome to hangman!\nYou have 5 lives.')
print(display)

def replace_display(input):
    for i in range(len(answer)):
        if answer[i] == input:
            display[i] = input

while lives > 0 and game_over == False:
    player_input = input('Guess a letter: ')
    
    if player_input in answer:
        replace_display(player_input)
    else:
        lives -= 1
        print(f'You have {lives}lives left.')
    
    if '_' not in display:
        print('You won!')
        game_over = True
    
    if lives == 0:
        print('You lost :(')
    print(display)