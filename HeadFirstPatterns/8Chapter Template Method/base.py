import abc
from typing import Protocol


class CaffeineBeverage(Protocol):
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.hook():
            self.add_condiments()

    @abc.abstractmethod
    def brew(self):
        pass

    @abc.abstractmethod
    def add_condiments(self):
        pass

    def hook(self):
        return True

    def boil_water(self):
        print("Кипятим воду")

    def pour_in_cup(self):
        print("Наливаем в чашку")


class Coffee(CaffeineBeverage):
    def brew(self):
        print("Завариваем кофе")

    def add_condiments(self):
        print("Добавляем сахар и молоко")

    def hook(self):
        message = input("Добавить сахар и молоко? (Yes\\No): ")
        print(message)
        if message.lower().startswith("y"):
            return True
        return False


class Tea(CaffeineBeverage):
    def brew(self):
        print("Кладем чайный пакетик")

    def add_condiments(self):
        print("Добавляем лимон")

    def hook(self):
        message = input("Добавить лимон? (Yes\\No): ")
        print(message)
        if message.lower().startswith("y"):
            return True
        return False
