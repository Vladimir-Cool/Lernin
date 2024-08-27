from typing import Protocol


class Turkey(Protocol):
    """Класс интерфейса индюка"""

    def gobble(self):
        pass

    def fly(self):
        pass


class WildTurkey(Turkey):
    def gobble(self):
        print("Губбл губбл")

    def fly(self):
        print("Полетилииии")
