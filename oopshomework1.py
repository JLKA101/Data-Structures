class Account:
    def __init__ (self, holder, balance):
        self.holder = holder
        self.balance = balance

    def deposit (self, amount):
        
        if amount >= 0:
            self.balance += amount
        else:
            print("Value cannot be negative.")

    def withdraw (self, amount):
        
        if amount >= 0:
            self.balance -= amount
        elif amount > self.balance:
                print("Insufficent funds.")
        else:
            print("Please exclude minus sign.")

    def checkBalance(self):
        print("Your current balance is: " + self.balance)

bank_account = Account("Me", 100)
query = input("Would you like to withdraw or deposit or check your balance? ")
if query == "withdraw":
    amount = int(input("How much would you like to withdraw?"))
    bank_account.withdraw(amount)
elif query == "deposit":
    amount = int(input("How much would you like to deposit?"))
    bank_account.deposit(amount)
elif query == "check my balance":
    bank_account.checkBalance()
else:
    print("Please input 'withdraw' or 'deposit'.")