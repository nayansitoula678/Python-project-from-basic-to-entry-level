print("Welcome to ATM of NMB BANK")

pin = int(input("Enter your PIN: "))
if pin == 4321:
    print("Welcome to your account")

    class BankAccount:
        def __init__(self, account, balance=0):
            self.account = account
            self.balance = balance

        def deposit(self, amount):
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")

        def withdraw(self, amount):
            if amount > self.balance:
                print("Insufficient funds")
            else:
                self.balance -= amount
                print(f"Withdrew {amount}. New balance: {self.balance}")

        def check_balance(self):
            print(f"Current balance: {self.balance}")

    account = BankAccount("NMB", 1000)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Currency Conversion (USD to NPR)")
        print("5. Currency Conversion (NPR to USD)")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            try:
                amount = int(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid integer amount.")

        elif choice == "2":
            try:
                amount = int(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid integer amount.")

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            try:
                usd_amount = float(input("Enter amount in USD to convert: "))
                conversion_rate = 140.75 
                npr_amount = usd_amount * conversion_rate  
                print(f"{usd_amount} USD is approximately {npr_amount:.2f} NPR.")
            except ValueError:
                print("Invalid amount entered. Please enter a numerical value.")

        elif choice == "5":
            try:
                npr_amount = float(input("Enter amount in NPR to convert: "))
                conversion_rate = 140.75  
                usd_amount = npr_amount / conversion_rate
                print(f"{npr_amount} NPR is approximately {usd_amount:.2f} USD.")
            except ValueError:
                print("Invalid amount entered. Please enter a numerical value.")

        elif choice == "6":
            print("Closing transaction. Thanks for using our bank.")
            break

        else:
            print("Invalid choice")
else:
    print("Wrong PIN")
