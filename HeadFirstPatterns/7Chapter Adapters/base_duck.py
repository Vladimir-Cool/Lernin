from typing import Protocol


class Duck(Protocol):
    """Класс интерфейса Утки"""

    def quack(self):
        pass

    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print("Кря")

    def fly(self):
        print("Летим")
