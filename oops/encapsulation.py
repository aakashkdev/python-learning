class Account:
  def _init_(self, balance):
    self._balance = balance

  def deposit(self, amount):
    self._balance +=amount