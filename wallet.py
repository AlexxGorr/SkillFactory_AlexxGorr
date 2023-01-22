"""
Кредитка/обычная/PRO
Баланс
Лимиты
Перевод

ООП
Наследование
ABC классы
Паттерн стратегия
"""

from abc import ABC


class Wallet(ABC):
    def __init__(self, name: str, type: str = 'General'):
        self.name: str = name
        self.type: str = type
        self.balance: int = 0

    def get_balance(self) -> int:
        return self.balance

    def change_balance(self, value: int):
        if self.balance + value < 0:
            print(f'Баланс отрицательный: {self.balance}')
        else:
            self.balance += value


class ProBalance:
    def change_balance(self, value: int):
        if self.balance + value * 0.95 < 0:
            print(f'Баланс отрицательный: {self.balance}')
        else:
            self.balance += value * 0.95 if self.balance + value * 0.95 < self.balance else value


class CreditBalance:
    def change_balance(self, value: int):
        if self.balance + value < self.limit:
            print(f'Баланс отрицательный: {self.balance}')
        else:
            self.balance += value


class CreditCard(CreditBalance, Wallet):
    def __init__(self, name, limit: int = -1000):
        self.limit = limit
        super().__init__(name)


class Card(Wallet):
    def __init__(self, name):
        super().__init__(name)

    def change_type(self):
        if self.balance < 100:
            print(f'Баланс отрицательный: {self.balance}')
        else:
            self.balance -= 100
            card = ProCard(self.name)
            card.balance = self.balance
            return card


class ProCard(ProBalance, Wallet):
    def __init__(self, name, type = 'PRO'):
        super().__init__(name, type)


class Main:
    def loop(self):
        pass

    def start(self):
        Main()

g = Main()
g.start()

card = ProCard('User')
print(card.get_balance())
card.change_balance(1000)
print(card.get_balance())
card.change_balance(-800)
print(card.get_balance())
card.change_balance(-250)
print(card.get_balance())




































