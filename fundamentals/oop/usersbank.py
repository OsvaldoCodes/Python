class user:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 500)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display(self):
        self.account.display_account_info()
        return self
    
    def displaybalance(self):
        self.account.display_my_balance()
        return self
class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance): 
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
    
    def display_my_balance(self):
        print(f"Your current balance is: {self.balance}")
    
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

user1 = user("ozzy", "myemail@")
user1.make_deposit(100)
user1.make_withdraw(100)
user1.displaybalance()