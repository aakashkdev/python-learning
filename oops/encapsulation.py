class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   # Private variable (hidden)

    def deposit(self, amount):
        self.__balance += amount   # Balance update internally

    def get_balance(self):
        return self.__balance      # Controlled access
