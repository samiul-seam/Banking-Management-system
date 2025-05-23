class BalanceException(Exception):
    pass

class BankAccount:
    all_accounts = []

    def __init__(self, name, password, amount):
        self.name = name
        self.password = password
        self.balance = amount
        BankAccount.all_accounts.append(self)
        print(f"\nAccount '{name}' is created successfully with amount {self.balance:.2f} taka.")

    def get_balance(self):
        print(f"Account '{self.name}' has balance: {self.balance:.2f} taka")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposited {amount:.2f} taka successfully ✅")
        self.get_balance()

    def viable_transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\n❌ Sorry! Your account has only {self.balance:.2f} taka."
            )

    def authenticate(self):
        attempt = input(f"Enter your password for account {self.name}: ")
        return attempt == self.password

    def withdraw(self, amount):
        if not self.authenticate():
            print("\nWrong password. Withdraw canceled.")
            return
        try:
            self.viable_transaction(amount)
            self.balance -= amount
            print(f"\nWithdrawal complete.")
            self.get_balance()
        except BalanceException as error:
            print(f"\n❌ Withdrawal interrupted: {error}")

    def transfer(self, recipient_account, amount):
        try:
            self.viable_transaction(amount)
            print(f"\n***** Beginning Transfer... *****")
            self.withdraw(amount)
            recipient_account.deposit(amount)
            print(f"\n✅ Transfer successful *****")
        except BalanceException as error:
            print(f"\n❌ Transfer interrupted: {error}")


class InterestRewardAccount(BankAccount):
    def deposit(self, amount):
        self.balance += amount * 1.05
        print(f"Deposit with interest complete.")
        self.get_balance()


class SavingsAccount(InterestRewardAccount):
    def __init__(self, name, password, amount):
        super().__init__(name, password, amount)
        self.fee = 5

    def withdraw(self, amount):
        if not self.authenticate():
            print("\nWrong password. Withdraw canceled.")
            return
        try:
            total = amount + self.fee
            self.viable_transaction(total)
            self.balance -= total
            print("\nWithdrawal successful (including fee).")
            self.get_balance()
        except BalanceException as error:
            print(f"\n❌ Withdrawal interrupted: {error}")

