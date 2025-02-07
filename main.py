import random
# Here I want to follow the tutorial and build slot machine
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 300

ROWS = 3
COLUMNS = 3

letter_count = {
    'A' : 2,
    'B' : 4,
    'C' : 6,
    'D' : 8
}

multiplication_values = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
}

def check_winnings(columns, lines , bet, values):
    winning = 0
    winning_lines = []
    for line in range(lines):
        first_symbol = columns[0][line]
        for column in columns:
            column_to_check = column[line]
            if first_symbol != column_to_check:
                break
        else:
            winning += values[first_symbol] * bet
            winning_lines.append(line + 1)
    return winning, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    # We need to generate a list with all the letters
    all_letters = []
    for letter, count in symbols.items():
        for _ in range(count):
            all_letters.append(letter)
    # At this point we will have list like this [A, A, B, B, B, B, ...]

    # We need to create columns and populate them with values from generated list
    columns = []
    for _ in range(cols):
        column = []
        # Let's make a copy so we have initial list state preserved
        current_letters = all_letters[:]
        for _ in range(rows):
            letter = random.choice(current_letters)
            column.append(letter)
            # If we picked the value we won't take it second time
            current_letters.remove(letter)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    # [A, B, C]
    # [A, A, C]
    # [A, C, C]
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=' | ')
            else:
                print(column[row])

def depositMoney():
    while True:
        deposit = input('Please insert some cash to play $')
        if deposit.isdigit():
            deposit = int(deposit)
            if deposit > 0:
                break
            else:
                print('Cash can\'t be below 0')
        else:
            print('Please, enter numeric value')
    return deposit
            
def get_number_of_lines():
    while True:
        lines = input('Enter number of lines to bet on (1  - %s): ' % MAX_LINES)
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= 3:
                break
            else:
                print('Enter a valid number')
        else:
            print('Please, enter numeric value')
    return lines

def get_bet():
    while True:
        amount = input('How much do you like to bet on each line?')
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f'Amount must be beetween ${MIN_BET} - ${MAX_BET}.')
        else:
            print('Please, enter numeric value')
    return amount

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        totalBet = bet * lines
        if(totalBet > balance) :
            print(f'You have no enough balance to make this bet. Your current balance is ${balance}.')
        else:
            break

    print(f'You are betting ${bet} on {lines}. Total bet is: ${totalBet}')
    
    slots = get_slot_machine_spin(ROWS, COLUMNS, letter_count)
    print_slot_machine(slots)
    winings, winning_lines = check_winnings(slots, lines, bet, multiplication_values)
    print(f'You won ${winings}.')
    print(f'You won on lines: ', *winning_lines)
    return winings - totalBet

def main():
    balance = depositMoney()
    while True:
        print(f'Current balance is ${balance} ')
        answer = input('Press enter to play or q to quit ')
        if answer == 'q':
            break
        balance += spin(balance)
    print(f'You left with ${balance}', end='\n\n')
    input('Press Enter to close the terminal')

main()