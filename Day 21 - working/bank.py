# Welcome message for the bank
print("_______________ Welcome to MOST WANTED BANK _______________")

# Define a class for BankAccount
class BankAccount:
    def __init__(self):
        # Initialize account holder names and passwords
        self.account_holders = ["admin"]  # Changed from account_holder to account_holders for clarity
        self.balance = int(0)  # Initial balance
        self.account_passwords = ["123"]  # Changed from account_password to account_passwords for clarity
        
    def help(self):
        # Display available commands to the user
        print("\nEnter [add] To Add money: \n Enter [withdraw] to withdraw the money \n Enter [Balance] to see your bank balance :\n")

    def deposit(self, amount):
        # Add money to the account
        self.balance += int(amount)  # Simplified the addition
        print(f"\n {amount} adding to your Bank account\n")
        print(f"Your bank balance is {self.balance}\n")

    def withdraw(self, amount):
        # Withdraw money from the account
        if self.balance >= float(amount):
            self.balance -= float(amount)
            print(f"\n {amount} withdraw from your Bank account\n")                
            print(f"Your bank balance is {self.balance}\n")
        else:
            print(f"\n[Withdraw FAILED] You only have {self.balance} in your account. \n")

    def login_page(self):
        # Handle user login
        while True:
            account_holder_name_input = input("Enter your account holder name to Login: ")
            if account_holder_name_input not in self.account_holders:
                print("Account holder name not found in database.")
                mybank.signin_signup()
            else:
                account_number_input = input("Enter your account password: ")
                if account_number_input not in self.account_passwords:
                    print("\nYou entered the wrong password.\n")
                    mybank.signin_signup()
                else:
                    print(f"\nWelcome back {account_holder_name_input} to MOST WANTED Bank.\n")
                    mybank.logged_in()  # Corrected spelling from loged_in to logged_in
            break

    def logged_in(self):
        # Display help and handle user commands after login
        self.help()
        while True:
            main_input = input("Enter: ")

            if main_input == "add":
                add_amount = input("\nEnter the amount to [add] to your bank: ")
                if add_amount.isdigit():
                    mybank.deposit(add_amount)
                    self.help()
                else:
                    print("Enter a valid amount to deposit \n")
                    self.help()

            if main_input == "withdraw":
                withdraw_amount = input("Enter the amount to [withdraw] from your bank: ")
                if withdraw_amount.isdigit():  # Fixed the condition to call isdigit() correctly
                    mybank.withdraw(withdraw_amount)
                    self.help()
                else:
                    print("Enter a valid amount to withdraw \n")
                    self.help()

            if main_input == "balance":
                print(f"\n{self.account_holders} Your balance is {self.balance}")
                mybank.help()

            if main_input == "create":
                mybank.create_account()  # Corrected method name to create_account

            if main_input not in ["add", "withdraw", "balance"]:
                print("\n-----OOPS-----You entered a wrong command --------\n")
                self.help()

    def create_account(self):
        # Create a new account
        acc_name = input("Enter the account name: ")  # Take user input for account name

        if acc_name not in self.account_holders:
            acc_password = input("Enter the password: ")  # Password
            repeat_acc_password = input("Repeat the password: ")  # Repeat password

            if acc_password != repeat_acc_password:
                print("Enter the same password")
                mybank.create_account()  # Corrected method name to create_account
            else:
                self.account_holders.append(acc_name)
                self.account_passwords.append(acc_password)
                print(f"{acc_name}, your account is successfully created in MOST WANTED BANK")
                mybank.login_page()
        else:
            print("Account already exists")
            mybank.create_account()  # Corrected method name to create_account

    def signin_signup(self):
        # Handle sign in or sign up
        while True:
            signin_signup_input = input("Enter [sign in] to login \n[sign up] to create a new account\n INPUT: ")
            if signin_signup_input == "sign in":
                mybank.login_page()
            if signin_signup_input == "sign up":
                mybank.create_account()  # Corrected method name to create_account
            if signin_signup_input not in ['sign in', 'sign up']:
                print("Enter a valid input :-( ")

# Create an instance of the BankAccount class
mybank = BankAccount()
# Start the sign-in or sign-up process
mybank.signin_signup()

