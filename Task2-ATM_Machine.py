balance = 5000
pin = 1234

def check_pin(entered_pin):
    return entered_pin == pin

def check_balance():
    print(f"\nYour current balance is: Rs. {balance}\n")

def deposit():
    global balance
    amount = float(input("Enter amount to deposit: Rs. "))
    if amount <= 0:
        print("\nInvalid amount. Please enter a positive value.\n")
    else:
        balance += amount
        print(f"\nRs. {amount} deposited successfully!")
        print(f"New balance: Rs. {balance}\n")

def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: Rs. "))
    if amount <= 0:
        print("\nInvalid amount. Please enter a positive value.\n")
    elif amount > balance:
        print("\nInsufficient balance. Transaction failed.\n")
    else:
        balance -= amount
        print(f"\nRs. {amount} withdrawn successfully!")
        print(f"Remaining balance: Rs. {balance}\n")

def change_pin():
    global pin
    old = int(input("Enter current PIN: "))
    if old != pin:
        print("\nIncorrect PIN. Cannot change PIN.\n")
        return
    new = int(input("Enter new PIN: "))
    confirm = int(input("Confirm new PIN: "))
    if new == confirm:
        pin = new
        print("\nPIN changed successfully!\n")
    else:
        print("\nPINs do not match. PIN not changed.\n")

def main():
    print("\nWelcome to the ATM")
    print("="*30)
    entered = int(input("Enter your PIN to continue: "))
    if not check_pin(entered):
        print("\nIncorrect PIN. Access denied.\n")
        return

    print("\nLogin successful!")

    while True:
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")
        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            check_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            change_pin()
        elif choice == "5":
            print("\nThank you for using the ATM. Goodbye!\n")
            break
        else:
            print("\nInvalid choice. Please enter 1-5.\n")

main()
