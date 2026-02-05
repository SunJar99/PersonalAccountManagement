from datetime import datetime

class Amount:
    def __init__(self, amount, transaction_type):
        self.amount = float(amount)
        self.time = datetime.now()
        self.transaction_type = transaction_type 

    def __str__(self):
        return f"{self.time.strftime('%Y-%m-%d %H:%M:%S')} | {self.transaction_type}: ${self.amount}"

class PersonalAccount:
    def __init__(self, account_number, account_holder):
        self.account_num = int(account_number)
        self.account_hold = str(account_holder)
        self.balance = 0.0
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            transaction = Amount(amount, 'DEPOSIT')
            self.transactions.append(transaction)
            self.balance += amount
            print(f"Deposited ${amount} successfully.")
            print(f"Your Current Balance is ${self.balance}")
        else:
            print("Depositing wasnt complete.")
            print(f"Your Current Balance is ${self.balance}")
        
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            transaction = Amount(amount, 'WITHDRAW')
            self.transactions.append(transaction)
            self.balance -= amount
            print(f"Withdrawal of ${amount} is completed.")
            print(f"Your Current Balance is ${self.balance}")
        else: 
            print("Withdrawal wasnt complete.")
            print(f"Your Current Balance is ${self.balance}")

    def print_transaction_history(self):
        print(f"\nTransaction History: ")
        for i in self.transactions:
            print(i)

    def get_balance(self):
        return self.balance
        
    def get_account_number(self):
        print(f"The Account number is {self.account_num}.")

    def set_account_number(self, account_number):
        self.account_number = account_number
        print(f"Your current account number is {self.account_number} now.")

    def get_account_holder(self):
        print(f"Your Current Name is {self.account_hold}.")

    def set_account_holder(self, account_holder):
        self.account_hold = account_holder
        print(f"Your Current Name is {self.account_hold} now.")
    
    def __str__(self):
        return f"{self.account_hold} {self.account_num} {self.balance}"
    
    def __add__(self, amount):
        self.deposit(amount)
        return self
    
    def __sub__(self, amount):
        self.withdraw(amount)
        return self
    

acc = PersonalAccount(987654, "John Doe")

acc.deposit(500.0)
acc + 200.0

acc.withdraw(500.0)
acc - 200.0

print(f"Final Balance: ${acc.get_balance()}")

acc.print_transaction_history()

acc.get_account_holder()
acc.get_account_number()
