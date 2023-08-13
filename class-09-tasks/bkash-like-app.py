code = '*123#'
password = '64414646'
balance = 10000


def show_balance():
    global balance

    print(f"Your balance is: {balance}")


def credit_account(new_balance):
    global balance

    balance = balance + new_balance
    show_balance()


def withdraw_account(amount):
    global balance

    if balance > amount:
        balance = balance - amount
        show_balance()
    else:
        print("Insufficient balance.")


user_code = input("Enter your code: ")
if user_code != code:
    print("Invalid code")
else:
    user_password = input("Enter your password: ")
    if user_password != password:
        print("Invalid password")
    else:
        print("Enter 1 for check balance")
        print("Enter 2 for credit account")
        print("Enter 3 for withdraw balance")
        action_method = int(input(" "))

        if action_method == 1:
            show_balance()

        elif action_method == 2:
            creditBalance = int(input("Enter new credit: "))
            credit_account(creditBalance)

        elif action_method == 3:
            withdrawBalance = int(input("Enter withdraw amount: "))
            withdraw_account(withdrawBalance)

        else:
            print("Invalid choice")
