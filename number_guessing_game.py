import random

def game_over(status):
    if status == 'win':
        print('You win.')
    else:
        print('You lose.')
        
    restart = input('Would you like to play again? Type y or n. ')
    if restart == 'n':
        exit()
    else:
        start_game()

def guess(number, lives):
    print(f'you have {lives} attempts remaining to guess the number.')
    if lives == 0:
        game_over('lose')
        
    user_guess = int(input('Make a guess: '))
    
    if user_guess == number:
        game_over('win')
    elif user_guess > number:
        print('Too high.\nGuess again.')
        guess(number, lives - 1)
    else:
        print('Too low.\nGuess again.')
        guess(number, lives - 1)
    

def get_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if difficulty == 'easy':
        return 10
    else:
        return 5

def start_game():
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1, 100)
    lives = get_difficulty()
    guess(number, lives)
    
start_game()