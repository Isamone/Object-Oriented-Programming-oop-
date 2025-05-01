"""
Create a class called "Account" that has the following attributes:

account_number (string)
account_balance (float)
account_holder (string)
The class should have the following methods:

deposit(amount: float) - This method should add the amount passed as an argument to the account balance.
withdraw(amount: float) - This method should subtract the amount passed as an argument from the account balance, but only if the account balance is greater than the amount being withdrawn.
check_balance() - This method should return the current account balance.

Instructions

 

Define the Account class and its attributes as specified above.
Define the deposit() method. It should take in one argument, the amount to be deposited, and add it to the account balance.
Define the withdraw() method. It should take in one argument, the amount to be withdrawn, and subtract it from the account balance. The method should only execute the withdrawal if the account balance is greater than or equal to the amount to be withdrawn.
Define the check_balance() method. It should return the current account balance.
Create an instance of the Account class, and assign it to a variable called "my_account".
Use the methods of the class to deposit and withdraw money from the account, and check the account balance.
Test the program by creating multiple instances of the class and performing different transactions on them.
"""

class account:

    def __init__(self, account_number, account_balance, account_holder):
        self.account_number = int(account_number)
        self.account_balance = float(account_balance)
        self.account_holder = str(account_holder)
    def deposit(self, amount=float(0)):
        self.account_balance += amount
        return f"The amount of {amount} has been deposited into {self.account_holder} account and the balance is {self.account_balance}"
    def withdraw(self, amount =float(0)): 
        if self.account_balance > amount:
            self.account_balance -= amount
            return f"The amount of {amount} has been withdrew from {self.account_holder} account and the balance is now {self.account_balance}"
        else:
            return f"Your account is insuffient to make this transaction"
    def check_balance(self):
        return f"The account balance is {self.account_balance}"
    def __str__(self):
         return f"Account name: {self.account_holder}\n Account number: {self.account_number} \n Account balance: {self.account_balance} \n"
    
Ismail = account(account_number= 8033024209, account_balance= 100000.00, account_holder="Ismail")
Saddiqah = account(account_number= 684532, account_balance= 569823.45, account_holder= "Saddiqah")
habiba = account(account_number= 633073, account_balance= 23000, account_holder= "Habiba")

print(Ismail) 
print(Ismail.account_balance)
print(Ismail.account_holder)
print(Ismail.deposit(4000))
print(Ismail.withdraw(467))
print(Ismail.check_balance())
