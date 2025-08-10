balance = 0

def show_balance():
    
    print(f"Your balance = ${balance:.2f}")

def deposite():
    amount = float(input("Enter your deposit amount: "))
    if amount < 0:
        print("This is not a valid amount.")
        return 0
    else:
        return amount

def withdraw():
    
    amount = float(input("Enter amount to withdraw: "))
    
    if amount < 0:
        print("This is not a valid amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print(f"${amount:.2f} withdrawn successfully.")
        print(f"Your new balance={balance}")

while True:
    print("\nBanking program")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice (1 2 3 4): ")
    if choice == "1":
        show_balance()
    elif choice == "2":
        balance += deposite()
    elif choice == "3":
        withdraw()
    elif choice == "4":
        break
    else:
        print("This is not a valid choice!!")
