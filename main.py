#[[Dependencies]]
from decimal import Decimal
from Transaction import Transaction
from Bank import Bank,Account
from appStorage.storageModule import saveAccountData,loadAccountData

#================================================================

#[[Main]]

# def main():
#     account1 = Account("Bob")                                       #Create some accounts
#     account2 = Account("Joe")
#                                                             #Create&store some transactions
#     transactions = [
#         Transaction("deposit", Decimal("1500.00"), account1),
#         Transaction("withdraw", Decimal("220.50"), account1),
#         Transaction("deposit", Decimal("75.25"), account2),
#     ]

def main():
    Account("Test2")


#================================================================

loadAccountData()
main()
saveAccountData()
