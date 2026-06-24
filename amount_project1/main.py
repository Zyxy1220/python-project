import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 2,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnings(columns,lines,bet,values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings,winning_lines


def get_slot_machine_spin(rows,cols,symbols): # this fucntion is adding a outside list of abc to a list
    all_symbols = []
    for symbol,symbol_count in symbols.items():  # represent key and value
        for _ in range(symbol_count):  # take the value out and repeat by value (2)
            all_symbols.append(symbol)

    columns = []  
    for _ in range(cols): 
        column = []
        current_symbols = all_symbols[:] # copy as a reference
        for _ in range(rows):
            value = random.choice(current_symbols)  
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):  # change the columns(horizontal) to vertical
    for row in range(len(columns[0])): # 假设一个list有三个list 我不要他给我3 而是要根据那三个list里面有几个abc
        for i, column in enumerate(columns): # i for index 比如一个list有三个list i的作用就是给你0，1，2 然后去那个list找【0】三个list的第一个list
            if i != len(columns) - 1 :
                print(column[row],end=" | ")
            else:
                print(column[row],end="")

        print()
###
#i = 0
#column = ["A", "B", "C"]
#print(column[0])  # A

#i = 1
#column = ["D", "E", "F"]
#print(column[0])  # D

#i = 2
#column = ["G", "H", "I"]
#print(column[0])  # G
###


def deposit():
    while True:
        amount = input("What would you like to deposit ? : RM")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount of deposit must be greater than 0. ")
        else:
            print("Please enter a valid and positive number. ")

    return amount

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+") : ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of line. ")
        else:
            print("Please enter a valid and positive number. ")

    return lines

def get_bet():
    while True:
        bet = input("What would you like to bet on each line ? : RM")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amout of bet must be between RM{MIN_BET} and RM{MAX_BET}")
        else:
            print("Please enter a valid and positive number. ")

    return bet


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"You dont have enough amout of deposit, current balance is RM{balance}. ")
        else:
            break
    slots = get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines = check_winnings(slots,lines,bet,symbol_value)
    print(f"You won RM{winnings}.")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is RM{balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with RM{balance}.")


main()
