from bankingSystem import *
from admin import *

admin_user = admin()  # create admin instance

while True:
    print("\n=== Welcome to the Bank System ===")
    print("1. Create a new Bank Account")
    print("2. Login to your Account")
    print("3. Admin Login")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter account name: ")
        password = input("Set your account password: ")
        amount = float(input("Enter initial deposit amount: "))
        BankAccount(name, password, amount)

    elif choice == '2':
        name = input("Enter your account name: ")
        account = None
        for acc in BankAccount.all_accounts:
            if acc.name == name:
                account = acc
                break

        if account:
            if not account.authenticate():
                print("Wrong password. Access denied.")
                continue

            while True:
                print(f"\n--- Account Menu for {account.name} ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Transfer")
                print("4. Show Balance")
                print("5. Logout")

                acc_choice = input("Choose an option: ")

                if acc_choice == '1':
                    amt = float(input("Enter amount to deposit: "))
                    account.deposit(amt)
                elif acc_choice == '2':
                    amt = float(input("Enter amount to withdraw: "))
                    account.withdraw(amt)
                elif acc_choice == '3':
                    recipient_name = input("Enter recipient account name: ")
                    recipient = None
                    for acc in BankAccount.all_accounts:
                        if acc.name == recipient_name:
                            recipient = acc
                            break
                    if recipient:
                        amt = float(input("Enter amount to transfer: "))
                        account.transfer(recipient, amt)
                    else:
                        print("Recipient account not found.")
                elif acc_choice == '4':
                    account.get_balance()
                elif acc_choice == '5':
                    print("Logging out...")
                    break
                else:
                    print("Invalid option.")
        else:
           print("Account not found.")

    elif choice == '3':
        username = input("Enter admin username: ")
        password = input("Enter admin password: ")
        if admin_user.login(username, password):
            while(True):
                print ("\n1.show all acounts")
                print ("2.Remove account.")
                print ("3.Exit")
        
                choice = input("Enter your choice.")
                if choice == '1':
                    admin_user.showAllAcct()
                elif choice == '2':
                    name = input("Enter name: ")
                    admin_user.remove_account(name)
                elif choice == '3':
                    print("Logging out...")
                    break
        else:
            print("Invalid admin credentials.")

    elif choice == '4':
        print("\nThank you for using the Bank System. Goodbye!")
        break
    else:
        print("\nInvalid option. Please try again.")
