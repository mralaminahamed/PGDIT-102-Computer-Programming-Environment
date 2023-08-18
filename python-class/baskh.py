def checkBalance(balance):
    return print("Your current balance: ", balance)


def moneyWithdraw(balance, userAmount):
    if 0 < userAmount <= balance:
        balance = balance - userAmount
        print(f'Withdraw successful. Remaining balance: {balance}')
    else:
        print('Insufficient funds or invalid amount.')


def moneyCredited(balance, userAmount):
    if userAmount > 0:
        balance = balance + userAmount
        print(f'Amount credited successful. Updated balance: {balance}')
    else:
        print('Invalid amount for credit.')


new_pin = input("Enter your PIN: ")
entered_password = input("Enter your password: ")

pin = "*123#"
password = "123123"
initial_balance = 10000

if new_pin == pin and entered_password == password:
    print("Login successful.")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Credit Money")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        checkBalance(initial_balance)

    elif choice == 2:
        amount = int(input("Enter withdrawal amount: "))
        moneyWithdraw(initial_balance, amount)

    elif choice == 3:
        amount = int(input("Enter credit amount: "))
        moneyCredited(initial_balance, amount)

    else:
        print("Invalid choice.")

else:
    print("Unauthorized.")