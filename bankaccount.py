class BankAccount:
    accounts = []
    def __init__(self, name, int_rate, balance): 
        self.name = name
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    
    def deposit(self, amount):
        self.balance + amount
        print("=======================================================")
        print(f"You have deposited: ${amount}")
        print("=======================================================")
        return self 
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("You have insufficient funds. Charging $5 fee")
            self.balance - 5
        else:    
            print("=======================================================")
            print(f"You have withdrawed: ${amount}")
            print("=======================================================")
        return self
    
    def display_account_info(self):
        print("=======================================================")
        print(f"Your {self.name} account has a current balance of: ${self.balance}")
        print(f"Your current interest rate is: ${self.int_rate}")
        print("=======================================================")
        return self
    
    def yield_interest(self):
        if self.balance > 0:
            self.balance + (self.balance * self.int_rate)
        else:
            print("=======================================================")
            print("Your balance is negative.")
            print("=======================================================")
        return self    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            account.display_account_info()

print("=======================================================")
print("Welcome to Dojo Bank")
print("=======================================================")
account1 = BankAccount("Checking", 0.05, 40)
account1.deposit(50).deposit(25).deposit(25).withdraw(30).yield_interest().display_account_info()

account2 = BankAccount("Savings", 0.03, 100)
account2.deposit(100).deposit(50).withdraw(30).withdraw(50).withdraw(15).withdraw(30).yield_interest().display_account_info()

BankAccount.print_all_accounts()

