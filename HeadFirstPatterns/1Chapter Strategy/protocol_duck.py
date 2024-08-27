from typing import Protocol


class FlyBehavior(Protocol):
    """Интерфейс для поведения 'Полет'"""

    @staticmethod
    def fly():
        pass


class QuackBehavior(Protocol):
    """Интерфейс для поведения 'Крякать'"""

    @staticmethod
    def quack():
        pass
