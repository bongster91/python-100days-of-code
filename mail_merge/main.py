with open("./input/letters/starting_letter.txt") as letter:
    starting_letter = letter.read()
    
with open("./input/names/invited_names.txt") as names:
    invited_names = names.readlines()

for name in invited_names:
    stripped_name = name.strip()
    new_letter = starting_letter.replace('[name],', f'{stripped_name},')

    with open(f'./output/ready_to_send/{stripped_name}.txt', 'w') as completed_letter:
        completed_letter.write(new_letter)
    
