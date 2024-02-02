print('Welcome to the secret auction program.')

bid_list = []

def get_highest_bid():
    highest = ['', 0]
    for entry in bid_list:
        if entry['bid'] > highest[1]:
            highest[0] = entry['name']
            highest[1] = entry['bid']
    
    print(f'{highest[0]} is the winner!')

def take_bid():
    name = input('What is your name? ')
    bid = input('What is your bid? $')
    other_bidders = input('Are there any other bidders? Type yes or no. ')
    
    bid_list.append({
        'name': name,
        'bid': int(bid)
    })
    
    if other_bidders == 'yes':
        take_bid()
    else:
        get_highest_bid()

take_bid()