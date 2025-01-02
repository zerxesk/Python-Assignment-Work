#name: Hammad Kalmati
#roll no: 334211
#Batch - 08
accounts = {}
import json
def main_menu():
    _load_acc()
    print("Welcome to SMIT Bank.")
    print("""	Main Menu
Please select an option:
1. Create an Account
2. Deposit Money
3. Withdraw Money
4. Check Balance
5. Print Transaction Statement
6. Exit""")

    choice = input("Enter choice here: ").strip()
    
    while True:

        if choice == "1":
            _create_account()
            break
        elif choice == "2":
            _deposit()
            break
        elif choice == "3":
            _withdraw()
            break
        elif choice == "4":
            _check_balance()
            break
        elif choice == "5":
            _transaction_statement()
            break
        elif choice == "6":
            print("Thank you for using SMIT bank, Goodbye.")
            _save_acc()
            break
        else:
            print("Invalid input. Please try again")
            main_menu()
            break

def _load_acc(): 
    global accounts
    try:
        with open("accounts.json", "r") as f:
            accounts = json.load(f)
    except FileNotFoundError:
        print("No existing accounts found.")
    except json.JSONDecodeError:
        print("Error reading accounts file.")
        accounts = {}

def _save_acc():
    global accounts
    with open("accounts.json", "w") as f:
        json.dump(accounts, f, indent=4)


def _create_account():
    global accounts    
    while True:
        username = input('Create a username or enter 6 to quit: ').lower().strip()
        if username == "6": 
            print("Exiting account creation.")
            break
        elif username in accounts:
            print("This username is already taken. Please try a different one.")
        else:
            full_name = input('Enter your full name: ').strip()
            if not full_name:
                print("Full name cannot be empty. Please try again.")
                continue
            
            try:
                initial_balance = float(input('Enter your balance: '))
                if initial_balance > 0:
                    accounts[username] = {
                        "Full Name": full_name,
                        "Balance": initial_balance,
                        "Transactions": [("Deposit", initial_balance)]}
                    with open(f"{username}_transactions.txt", "w") as f:
                        f.write(f"Deposit: {initial_balance}, Balance: {accounts[username]['Balance']}\n")
                    print("Account created successfully.")
                    _save_acc()
                    break
            except ValueError:
                print("Invalid balance. Please enter a numeric value.")

def _withdraw():
    username = input("Enter your username: ").strip().lower()
    if username in accounts:
        try:
            withdraw_amount = input("Enter the amount of money you wish to withdraw.")
            withdraw_amount = float(withdraw_amount)
            
            if withdraw_amount > float(accounts[username]["Balance"]):
                print('Insufficient Balance')
            elif withdraw_amount < 0:
                print("You can't withdraw negative amount")
            else:
                file = f"{username}_transactions.txt"
                accounts[username]["Balance"] = float(accounts[username]["Balance"]) - withdraw_amount
                accounts[username]["Transactions"].append(("Withdrawal", withdraw_amount))
                with open (file,'a') as f:
                        f.write(f'Withdrawal: {withdraw_amount},  Balance: {accounts[username]["Balance"]}\n')
                print(f"You withdrawed: {withdraw_amount}. New balance: {accounts[username]["Balance"]}")
                _save_acc()
        except ValueError:
            print("Invalid input. Enter only numeric values")
    else:
        print("Invalid username.")

def _deposit():
    username = input("Enter your usename: ").strip().lower()
    if username in accounts:
        try:
            deposit_amount = input ("Enter the amount you want to deposit in.")
            deposit_amount = float(deposit_amount)
            if deposit_amount < 0:
                print("You can't deposit negative amount.")
            else:
                file = f"{username}_transactions.txt"
                accounts[username]["Balance"] = float(accounts[username]["Balance"]) + deposit_amount
                accounts[username]["Transactions"].append(("Deposit", deposit_amount ))
                with open (file,'a') as f:
                    f.write(f'Deposit: {deposit_amount},  Balance: {accounts[username]["Balance"]}\n')
                print(f"You deposited: {deposit_amount}. New balance: {accounts[username]["Balance"]}")
                _save_acc()
        except ValueError:
            print("Invalid input. Enter only numeric values")
    else:
        print("Invalid usename.")

def _check_balance():
    username = input("Enter your usename: ").strip().lower()
    if username in accounts:
        print(f"Your current balance is: {accounts[username]["Balance"]}")
    else:
        print("Invalid username.")

def _transaction_statement():
    username = input("Enter your usename: ").strip().lower()
    if username in accounts:
        file = f'{username}_transactions.txt'
        with open(file,'r') as f:
            transactions = f.read().strip()
            print(f"Account Statement for {accounts[username]['Full Name']}: ")
            print("Type     Amount     Balance")
            print(transactions)
    else:
        print('Invalid username.')

if __name__ == "__main__":
    main_menu()

