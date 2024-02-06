#5
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"new balance :{self.balance}")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"New balance: {self.balance}")
account1 = Account(owner="Doszhan", balance=1000)

account1.deposit(500)
account1.withdraw(200)
account1.deposit(1000)
account1.withdraw(1500)
