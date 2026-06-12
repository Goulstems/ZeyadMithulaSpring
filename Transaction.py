#[[Dependencies]]
from decimal import Decimal
from Bank import Account

#[[Transaction class]]: reponsible for financial exchange data between Accounts
class Transaction:
    def __init__(self, kind: str, amount: Decimal, account: Account)-> None:
        if kind=="withdraw":
            amount=-amount
        self.kind = kind
        self.amount = Decimal(amount)
        self.account = account
        account.changeBalance(amount)

    def receipt(self) -> str:
        return (
            "- - - - - - - - - - -\n"
            "Transaction Receipt\n"
            f"Type: {self.kind}\n"
            f"Amount: {self.amount}\n"
            f"Account Name: {self.account.name}"
            "\n- - - - - - - - - - -"
        )


