# Declare Global variables
import os

balance = 0

transaction_file = open("TransactionLog.txt", "w")
transaction_file.write("\n ==============================Bank statement==============================")
transaction_file.write("\n Initial Amount: R" + str(balance))

bankData_file = open("Bank Data.txt", "w")

# Create files if they don't exixt
def create_files():
    if not os.path.exists(bankData_file):
        open("Bank Data.txt", "w")
    else:
        open("Bank Data.txt", "a+")

    if not os.path.exists(transaction_file):
        open("TransactionLog.txt", "w")
    else:
        open("TransactionLog.txt", "a+")

# Check account Balance
def chck_balance():

    print("Current Balance: R", balance)
    bankData_file.write("\n New Current Balance: R" + str(balance))

def deposit(amount):
    global balance # Add global keyword
    balance += amount
    transaction_file.write("\n =============================New Transaction=============================")
    transaction_file.write("\n Amount Deposited: R" + str(amount))
    transaction_file.write("\n New Balance: R" + str(balance))
    chck_balance()

# Make a withdrawal
def withdraw(amount):
    global balance # Add global keyword
    if amount <= balance:
        balance -= amount
        chck_balance()
    else:
        print("Insufficient balance.")

    transaction_file.write("\n =============================New Transaction=============================")
    transaction_file.write("\n Amount Deposited: R" + str(amount))
    transaction_file.write("\n New Balance: R" + str(balance))

# Function for transactions
def transactions():

    while True:

        # Asking user if they want to make a transaction
        make_transaction = input("Would you like to make a transaction? (Yes/No)")
        if make_transaction != "yes" and make_transaction != "no":
            print("Invalid input.")
            continue
        if make_transaction == "no":
            break

        # Making a deposit or withdrawal
        dep_or_withdrwl = input("Would you like to make a deposit or withdrawal? (Deposit/Withdraw)")
        if dep_or_withdrwl != "deposit" and dep_or_withdrwl != "withdraw":
            print("Invalid input.")
            continue
        if dep_or_withdrwl == "deposit":
            amnt = float(input("How much would you like to deposit?"))
            deposit(amnt)
            continue
        if dep_or_withdrwl == "withdraw":
            amnt = float(input("How much would you like to withdraw?"))
            withdraw(amnt)

transactions()
