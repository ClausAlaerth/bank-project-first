# Bank Project - Part 1

# Class Containing the Options ###################################

class Bank:

    main_menu = """
	Bank System - Your Account
    
[1] - Deposit
[2] - Withdraw
[3] - Transactions
[4] - Exit
	"""

    loop_system = True

    balance = 0
    limit_per_withdrawal = 500
    withdrawal_limit_per_day = 0
    transaction_list = []

    WITHDRAWAL_LIMIT_PER_DAY = 3

    def __init__(self, client):
        self.client = client
        self.deposit_amount = 0
        self.withdraw_amount = 0
        self.show_transactions = None

    def deposit(self):

        self.deposit_amount = float(input("\nInsert deposit amount: "))

        if self.deposit_amount > 0:

            Bank.balance += self.deposit_amount

            Bank.transaction_list.append(
                {"Operation": "Deposit", "Amount": self.deposit_amount}
            )

            print(f"\nR$ {self.deposit_amount:.2f} deposited.")
            print(f"Current balance: {Bank.balance:.2f}")

        else:
            print("\nIncorrect value inserted.")
            return

    def withdraw(self):

        if Bank.withdrawal_limit_per_day == Bank.WITHDRAWAL_LIMIT_PER_DAY:
            print("\nDaily limit reached.")
            return

        self.withdraw_amount = float(input("\nInsert withdrawal amount: "))

        if self.withdraw_amount > 500:
            print("\nThe limit allowed per withdrawal is R$ 500,00.")
            return

        elif self.withdraw_amount > Bank.balance:
            print("\nBalance is insufficient.")
            return

        elif (self.withdraw_amount > 0) and (self.withdraw_amount <= Bank.balance):

            Bank.balance -= self.withdraw_amount

            Bank.withdrawal_limit_per_day += 1

            Bank.transaction_list.append(
                {"Operation": "Withdraw", "Amount": self.withdraw_amount}
            )

            print(f"\nYou withdrawed R$ {self.withdraw_amount:.2f}.")
            print(f"Current balance: {Bank.balance:.2f}")

        else:
            print("\nIncorrect value inserted.")
            return

    def transactions(self):

        if not Bank.transaction_list:
            print("\nThere are no transactions in your account.")
            print(f"Current balance: {Bank.balance:.2f}")
            return

        print("\nYour transactions:")

        for operation in Bank.transaction_list:
            print(f"\nOperation: {operation["Operation"]}")
            print(f"Amount: {operation["Amount"]}")

    def exit(self):
        print("\nShutting down...\n")
        Bank.loop_system = False
        return


client = Bank("client")

# Bank System ####################################################

while Bank.loop_system:

    options = {
        "1": lambda: client.deposit(),
        "2": lambda: client.withdraw(),
        "3": lambda: client.transactions(),
        "4": lambda: client.exit()
    }

    print(Bank.main_menu)

    choice = input("=> ")

    command = options.get(choice)

    command()
