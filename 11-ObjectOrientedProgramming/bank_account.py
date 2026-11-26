class BankAccount:
    def __init__ (self, account_number):
        self.balance = 0
        self.account_number = account_number

    def show_balance(self):
        print(f"Bank Account No: {self.account_number}")
        print(f"Balance: PLN {self.balance:.2f}".replace(".", ","))
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance < amount:
            print("Insufficient funds on the account")
        else:
            self.balance -= amount
            
        
