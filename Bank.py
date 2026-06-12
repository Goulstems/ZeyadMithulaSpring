#[[Dependencies]]
from decimal import Decimal

#[[Bank class]] : responsible for account storage. 
class Bank:
    storage = []
    nextID=0
    @staticmethod
    def addAccount(newAccount:"Account")->None:
        Bank.nextID+=1
        Bank.storage.append(newAccount)
    @staticmethod
    def removeAccount(accountToRemove:"Account")->None:
        for account in Bank.storage:
            if account == accountToRemove:
                Bank.storage.remove(account)

#[[Account class]] : responsible for independent transactions
class Account:
    def __init__(self,name:str,startingBalance:Decimal=0):
        self.name = name
        self.balance = startingBalance
        self.accountID=Bank.nextID
        Bank.addAccount(self)
    def changeBalance(self,amount:Decimal=0):
        self.balance+=amount
    