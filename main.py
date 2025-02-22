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
        self.balance -= amount

account = BankAccount("Silver", "100")
print(account.name, account.balance)

##################################################
'''
Q5:
'''
account.deposit(50, 100)
print(account.name, account.amount, account.balance)

##################################################
'''
Q6:
'''


##################################################
'''
Q7:
'''


##################################################
