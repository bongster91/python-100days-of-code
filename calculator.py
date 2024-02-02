def start():
    first_number = int(input("What's the first number?: "))
    calculate(first_number)

def get_answer(first, operation, second):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


def calculate(first_number):
    operation = input('+\n-\n*\n/\nPick an operation: ')
    second_number = int(input("What's the next number?: "))

    answer = get_answer(first_number, operation, second_number)
    print(f'{first_number} {operation} {second_number} = {answer}')
    
    new_calculation = input("Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    if new_calculation == 'y':
        calculate(answer)
    else:
        start()
    
start()