'''BankAccountManager – Simple Deposit & Withdrawal System'''
class BankAccount:
    def __init__(self, account_holder, initial_balance=0):
        self.account_holder = account_holder
        self.__balance = initial_balance  # Private variable

    def deposit(self, amount):
        if amount <= 0:
            return "Deposit amount must be positive."
        self.__balance += amount
        return f"Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}"

    def withdraw(self, amount):
        if amount <= 0:
            return "Withdrawal amount must be positive."
        if amount > self.__balance:
            return "Insufficient funds."
        self.__balance -= amount
        return f"Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}"

    def get_balance(self):
        return f"Current balance: ${self.__balance:.2f}"


class BankAccountManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder, initial_balance=0):
        if account_holder in self.accounts:
            return "Account already exists."
        self.accounts[account_holder] = BankAccount(account_holder, initial_balance)
        return f"Account created for {account_holder}."

    def get_account(self, account_holder):
        return self.accounts.get(account_holder, None)


# Example Usage
if __name__ == "__main__":
    manager = BankAccountManager()
    
    print(manager.create_account("Alice", 1000))
    account = manager.get_account("Alice")
    
    print(account.deposit(500))
    print(account.withdraw(200))
    print(account.withdraw(2000))  # Should show insufficient funds
    print(account.get_balance())

'''
Output:
Account created for Alice.
Deposited $500.00. New balance: $1500.00
Withdrew $200.00. New balance: $1300.00
Insufficient funds.
Current balance: $1300.00'''


