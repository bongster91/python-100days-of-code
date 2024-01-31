import random
user_choice = input('What do you choose? Type 0 for rock, 1 for paper and 2 for scissors. ')
choices = ['rock', 'paper', 'scissors']
computer_choice = random.randint(0, 2)
print(f'Computer chose: {choices[computer_choice]}')

if user_choice == str(computer_choice):
    print('Tie!')
elif user_choice == '0' and computer_choice == 1 or user_choice == '1' and computer_choice == 2 or user_choice == '2' and computer_choice == 0:
    print('Your win!')
else:
    print('Your lose!')