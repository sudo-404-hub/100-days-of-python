# ask: Create a Simple Class for a BankAccount
# Define a Class: Create a class named BankAccount.
# Attributes: The class should have the following attributes:
# account_holder (string): The name of the account holder.
# balance (float): The current balance of the account (initialize it to 0.0).
# account_number (string): A unique account number for the bank account.
# Methods: The class should have the following methods:
# deposit(amount): This method should add the specified amount to the balance and print a confirmation message.
# withdraw(amount): This method should subtract the specified amount from the balance if sufficient funds are available; otherwise, it should print an error message.
# get_balance(): This method should return the current balance of the account.
# transfer(amount, other_account): This method should transfer the specified amount to another BankAccount instance if sufficient funds are available; otherwise, it should print an error message.
# Create Instances: Create at least two instances of the BankAccount class, perform some deposits and withdrawals, and demonstrate transferring money between accounts.

# later on feature can be add
# user input interaction
# new account create , del 

class BankAccount:
    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.balance = ""
        self.account_number = account_number

    def deposit(self, amount):
        if self.account_number == self.account_holder:
            self.balance.append(amount)
            print(f"Your back balance is {self.balance}")

    def withdraw(self, amount):
        if self.account_number == self.account_holder and amount in self.balance:
            self.balance - amount








