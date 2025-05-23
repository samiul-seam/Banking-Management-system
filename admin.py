from bankingSystem import *

class admin:
    def __init__(self):
        self.name = "admin"
        self.password = "1234"

    def login(self, username, password):
        return username == self.name and password == self.password

    def showAllAcct(self):
        print (f"\nAccount Name\tBalance")
        for ac in BankAccount.all_accounts:
            print(f"{ac.name}\t\t{ac.balance:.2f}")

    def remove_account(self, name):
        account = None
        for acc in BankAccount.all_accounts:
            if acc.name == name:
                account = acc
                break
        if account:
            BankAccount.all_accounts.remove(account)
            print(f"\n✅ Account '{name}' removed successfully.")
        else:
            print(f"\n❌ Account '{name}' not found.")