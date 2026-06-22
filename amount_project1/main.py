MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


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


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if total_bet > balance:
            print(f"You dont have enough amout of deposit, current balance is RM{balance}. ")
        else:
            break

main()