class Account():
    def __init__(self, id, balance=10000):
        self.id = id
        self.balance = balance
    
    def withdraw(self, no_of_notes, per_note_amount):
        if (self.balance-(no_of_notes * per_note_amount))>5000:
            self.balance =  self.balance-(no_of_notes * per_note_amount)
            return self.getBalance()
        else:
            print("Require Min Balance of 5000")
    
    def deposit(self, no_of_notes, per_note_amount):
        self.balance = self.balance+(no_of_notes * per_note_amount)
        return self.getBalance()

    def getBalance(self):
        return self.balance

acc1 = Account(1)
print(acc1.withdraw(2,100))
print(acc1.deposit(2,100))
print(acc1.getBalance())


