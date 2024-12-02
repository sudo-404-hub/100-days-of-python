# ask: Create a Simple Class for a BankAccount




print("_______________ Welcome to MOST WANTED BANK _______________")


class BankAccount:
    def __init__(self):
        self.account_holder = ["admin"]
        self.balance = int(0)
        self.account_password = ["123"]
        
    def help(self):
        print("\nEnter [add] To Add money: \n Enter [withdraw] to withdraw the money \n Enter [Balance] to see ur bank balance :\n")


    def deposit(self, amount):
            self.balance = self.balance + int(amount)
            print(f"\n{self.account_holder} adding {amount} to ur Bank account\n")
            print(f"Your back balance is {self.balance}\n")


    def withdraw(self, amount):
        if self.balance >= float(amount):
            self.balance -= float(amount)
            print(f"\n{self.account_holder} withdraw {amount} to ur Bank account\n")                
            print(f"Your back balance is {self.balance}\n")
        else:
            print(f"\n[withdraw FAILD] You only have {self.balance} in ur account. \n")
                


    def login_page(self):
        
        while True:
            account_holder_name_input = input("Enter you account_holder name to Login in : ")
            if account_holder_name_input not in self.account_holder:
                print("Account holder name not fount in database.")
                mybank.signin_signup()
            else:
                account_number_input = input("Enter ur account Pasword : ")
                if account_number_input not in self.account_password:
                    print("\nU enter wrong account number .\n")
                    mybank.signin_signup()
                else:
                    print(f"\nwelcome back {account_holder_name_input} to MOST WANTED Bank.\n")
                    mybank.loged_in()
            break

    
    def loged_in(self):
        self.help()
        while True:
            main_input = input("Enter : ")

            if main_input == "add":
                add_amount = input("\nEnter the amount to [add] to ur bank : ")
                if add_amount.isdigit():
                    mybank.deposit(add_amount)
                    self.help()
                else:
                    print("Enter a valid amount to deposit \n")
                    self.help()
                    
                    

            if main_input == "withdraw":
                withdraw_amount = input("Enter the amount to [withdraw] from ur bank : ")
                if withdraw_amount.isdigit:
                    mybank.withdraw(withdraw_amount)
                    self.help()
                else:
                    print("Enter a valid amount to withdraw amount \n")
                    self.help()

            if main_input == "balance":
                print(f"\n {self.account_holder} Your balance is {self.balance}")
                mybank.help()

            if main_input == "create":
                mybank.Create_account()


            if main_input not in  ["add" , "withdraw" , "balance"]:
                print("\n-----OOPS-----You enter wrong command --------\n")
                self.help()
            
    def Create_account(self):
        acc_name = input("Enter the account name : ") # take user input for acc name

        if acc_name not in self.account_holder:

            acc_password = input("Enter the passowrd name : ") # password
            repeat_acc_password = input("Repeat the passowrd name : ") # repeate password

            if acc_password != repeat_acc_password:
                print("Enter the same password")
                mybank.Create_account()
            else:
                self.account_holder.append(acc_name)
                self.account_password.append(acc_password)
                print(f"{acc_name} Your account is successfully created in MOST WANTED BANK")
                mybank.login_page()
        else:
            print("Account already exist")
            mybank.Create_account()

    def signin_signup(self):
        while True:
            signin_signup_input = input("Enter [sign in] to login in \n[sign up] to create new account\n INPUT : ")
            if signin_signup_input == "sign in":
                mybank.login_page()
            if signin_signup_input == "sign up":
                mybank.Create_account()
            if signin_signup_input not in ['sign in' , 'sign up']:
                print("Enter the valid input :-( ")



mybank = BankAccount()
mybank.signin_signup()
