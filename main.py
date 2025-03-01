##################################################
'''
Q1a: 
'''
9, 2

##################################################
'''
Q1b: 
'''
27, 2
##################################################
'''
Q2:
'''
class Name:
    def __init__(self,first,last):
        self.first = first
        self.last = last

    def normal_order(self):
        print(self.first, self.last)

    def reverse_order(self):
        print(self.last, self.first)


identity = Name("one", "two")
print(identity.first, identity.last)

##################################################
'''
Q3:
'''
identity.reverse_order()

##################################################
'''
Q4:
'''
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance  = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
            if (self.balance -2) < 0:
                self.balance = self.balance
            else: 
                self.balance -= 2
        else:
            self.balance = 0

    def transfer(self, name2, amount):
        transfer_fee = 5
        if amount > 0:
            if self.name != name2:
                if (self.balance - amount - transfer_fee) > 0:
                    self.balance -= (amount + transfer_fee)
                    name2.balance += amount
                else:
                    print("Not enough balance")



            




account = BankAccount("Silver", 100)
print(account.name, account.balance)

##################################################
'''
Q5:
'''
account.deposit(100)
print(account.name, account.balance)
##################################################
'''
Q6:
'''
account.withdraw(90)
print(account.name, account.balance)
##################################################
'''
Q7:
'''
secondAcc = BankAccount("Star", 300)
secondAcc.transfer(account, 300)


print(secondAcc.name, secondAcc.balance)
print(account.name, account.balance)
##################################################
