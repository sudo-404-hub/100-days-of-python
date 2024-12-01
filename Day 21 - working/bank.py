# ask: Create a Simple Class for a BankAccount

print("Welcome to MOST WANTED BANK")


class BankAccount:
    def __init__(self):
        self.account_holder = ["admin"]
        self.balance = 0
        self.account_number = ["123"]
        
    def help(self):
        print("Enter [add] To Add money: \n Enter [withdraw] to withdraw the money \n Enter [Balance] to see ur bank balance :\n")

    def deposit(self, amount):
            self.balance = self.balance + int(amount)
            print(f"Your back balance is {self.balance}")

    def withdraw(self, amount):
        self.balance = self.balance - int(amount)
        print(f"Your back balance is {self.balance}")
            


    def login_page(self):
        
        while True:
            account_holder_name_input = input("Enter you account_holder name : ")
            if account_holder_name_input not in self.account_holder:
                print("Account holder name not fount in database.")
            else:
                account_number_input = input("Enter ur account nunber : ")
                if account_number_input not in self.account_number:
                    print("U enter wrong account number .")
                else:
                    print(f"welcome back {self.account_holder} to MOST WANTED Bank.")
                    mybank.loged_in()
            break


                        
    
    def loged_in(self):
        self.help()
        while True:
            main_input = input("Enter : ")

            if main_input == "add":
                add_amount = input("Enter the amount to add to ur bank : ")
                mybank.deposit(add_amount)
                print(f"\n{self.account_holder} adding {add_amount} to ur Bank account\n")

            if main_input == "withdraw":
                print("withdrawing")

            if main_input == "balance":
                print(f"\n {self.balance} Your balance is ")

            else:
                print("\n-----OOPS-----You enter wrong command --------\n")
                self.help()
            
 

mybank = BankAccount()
mybank.login_page()

# reaming feature ----------------------------
# create new BankAccount
# del BankAccount
# validation if user have infugh many to withdraw from account




