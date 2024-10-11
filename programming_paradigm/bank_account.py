class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
        
    def deposit(self, amount):
        return self.account_balance + amount
    
    def withdraw(self, amount):
        if amount <= self.account_balance:
            return amount
        else:
            return None

    def display_balance(self):
        return f"Your Current Balance Now: {self.account_balance}"