from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def get_voice(self):
        pass


class Cat(Animal):

    def get_voice(self):
        print("мя")


class Dog(Animal):

    def get_voice(self):
        print("гав")


def voice(animal: Animal):
    animal.get_voice()


cat = Cat()
dog = Dog()

voice(cat)
voice(dog)

