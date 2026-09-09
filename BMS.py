
from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, holder_name: str, amount: float) -> None:
        self.holder_name = holder_name
        self.amount = amount

    def deposit(self, money: float) -> None:
        self.amount += money

    @abstractmethod
    def withdraw(self, money: float) -> None:
        pass


class Savings(Account):
    def withdraw(self, money: float) -> None:
        if money <= self.amount:
            self.amount -= money
        else:
            print("Insufficient balance")


class Current(Account):
    def withdraw(self, money: float) -> None:
        self.amount -= money


# Banking Management System
my_account: Account = Savings("Sunitha", 8000)

my_account.deposit(1500)
my_account.withdraw(1000)

print("Account Holder:", my_account.holder_name)
print("Balance:", my_account.amount)
