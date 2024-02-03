import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_random_card():
    random_object_position = random.randint(0, len(cards) - 1)
    random_card = cards[random_object_position]
    return random_card
        

def get_user_cards():
    user_cards = []
    user_cards.append(get_random_card())
    user_cards.append(get_random_card())
    return user_cards


def get_computer_card():
    computer_card = []
    computer_card.append(get_random_card())
    computer_card.append(get_random_card())
    return computer_card
    

def draw_another_card(user_cards, computer_cards):
    user_cards.append(get_random_card())
    print(f'Your cards: {user_cards}')
    print(f'Computer cards: {computer_cards}')
    
    if sum(user_cards) > 21:
        game_over('lose')
    else:
        calculate_cards(user_cards, computer_cards)

def game_over(status):
    if status == 'lose':
        print('You lost!')
    else:
        print('You won!')
        
    play_again = input("Would you like to play again? Type 'yes' or 'no'. ")
    if play_again == 'yes':
        start()
    else:
        exit()

def calculate_cards(user, computer):
    user_sum = sum(user)
    computer_sum = sum(computer)
    if user_sum > 21:
        game_over('lose')
    else:
        if user_sum > computer_sum:
            game_over('win')
        else:
            game_over('lose')

def start():
    user_cards = get_user_cards()
    computer_cards = get_computer_card()
    print(f'Your cards: {user_cards}')
    print(f"Computer's first card: {computer_cards[0]}")
    continue_game = input('Would you like to draw another card? Type yes or no. ')
    
    if continue_game == 'yes':
        draw_another_card(user_cards, computer_cards)
    else:
        calculate_cards(user_cards, computer_cards)

start()