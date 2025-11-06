class BankAccount:
  def __init__(self, balance):
    self.__balance = balance 

  def deposit(self, amount):
    self.__amount += amount

  def get_balance(self):
    return self.__balance 