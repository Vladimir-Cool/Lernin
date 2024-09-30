
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def get_voice(self):
        pass

class Cat(Animal):
    def get_voice(self):
        print("мя")


cat = Cat()
cat.get_voice()