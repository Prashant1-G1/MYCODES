import random


symbols = ["🍒", "🍋", "🔔", "💎", "7️⃣", "🍀"]


def spin_slots():
    return [random.choice(symbols) for _ in range(3)]


def calculate_multiplier(result):
    if result[0] == result[1] == result[2]:
        return 10 
    elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2]:
        return 3  
    else:
        return 0   


def play():
    balance = 50
    print("🎰 Welcome to the Python Slot Machine! 🎰")
    print("You start with $50.")
    print("Match all 3 symbols to win 10x your bet.")
    print("Match 2 symbols to win 3x your bet.\n")

    while balance > 0:
        print(f"💰 Current Balance: ${balance}")
        
        while True:
            try:
                bet = int(input("Enter your bet amount: $"))
                if bet <= 0:
                    print("Bet must be greater than zero.")
                elif bet > balance:
                    print("You can't bet more than your current balance.")
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")

        balance -= bet
        input("Press Enter to spin...")

        result = spin_slots()
        multiplier = calculate_multiplier(result)
        winnings = bet * multiplier
        balance += winnings

        print(" | ".join(result))
        if multiplier == 10:
            print(f"🎉 JACKPOT! You won ${winnings}!")
        elif multiplier == 3:
            print(f"👍 You matched 2 symbols and won ${winnings}.")
        else:
            print("🙁 No win this time.")

        if balance == 0:
            print("You're out of money! Game over.")
            break

        cont = input("Do you want to keep playing? (y/n): ").lower()
        if cont != 'y':
            print(f"You cashed out with ${balance}. Thanks for playing!")
            break

if __name__ == "__main__":
    play()
